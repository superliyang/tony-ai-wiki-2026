#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "00-Home" / "阅读控制台.html"
MD_OUT = ROOT / "00-Home" / "阅读控制台.md"

SCAN_ROOTS = [
    ROOT / "00-Home",
    ROOT / "20-Maps",
    ROOT / "10-Knowledge" / "AI",
    ROOT / "10-Knowledge" / "AI-Engineering",
    ROOT / "10-Knowledge" / "AI-Open-Source",
    ROOT / "10-Knowledge" / "Security",
    ROOT / "10-Knowledge" / "International-Payments",
    ROOT / "10-Knowledge" / "Advertising",
]

PINNED = [
    "00-Home/今日入口.md",
    "20-Maps/AI 学习入口.md",
    "10-Knowledge/AI-Engineering/06-Projects/Mac AI Expert Path/Mac AI 深度实战学习总纲.md",
    "10-Knowledge/AI-Engineering/06-Projects/Mac AI Expert Path/Mac AI 深度实战 16 周路径.md",
    "10-Knowledge/AI-Engineering/06-Projects/Mac AI Expert Path/第 1 周启动任务：模型与本地推理闭环.md",
    "10-Knowledge/AI-Engineering/07-Topics/AI 基础设施平台学习框架.md",
    "10-Knowledge/AI-Open-Source/03-Projects/Cube Studio.md",
    "20-Maps/内容更新雷达.md",
]


@dataclass
class Note:
    title: str
    rel: str
    domain: str
    status: str
    tags: list[str]
    mtime: float
    summary: str
    kind: str
    priority: int


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end].strip()
    body = text[end + 4 :]
    data: dict[str, object] = {}
    current_key = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - ") and current_key:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(line[4:].strip().strip('"'))
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            current_key = key
            if value.startswith("[") and value.endswith("]"):
                try:
                    data[key] = json.loads(value.replace("'", '"'))
                except Exception:
                    data[key] = [v.strip() for v in value[1:-1].split(",") if v.strip()]
            elif value:
                data[key] = value.strip('"')
            else:
                data[key] = []
    return data, body


def first_paragraph(body: str) -> str:
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    body = re.sub(r"---+", "", body)
    lines = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("|") or line.startswith("```"):
            if lines:
                break
            continue
        if line.startswith("- ") or line.startswith(">"):
            line = line.lstrip("> ").lstrip("- ").strip()
        line = re.sub(r"\[\[([^|\]]+)\|?([^\]]*)\]\]", lambda m: m.group(2) or m.group(1), line)
        line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        lines.append(line)
        if len(" ".join(lines)) > 120:
            break
    return " ".join(lines)[:180]


def domain_for(rel: str) -> str:
    parts = rel.split("/")
    if parts[0] == "10-Knowledge" and len(parts) > 1:
        return parts[1]
    if parts[0] == "20-Maps":
        return "Maps"
    if parts[0] == "00-Home":
        return "Home"
    return parts[0]


def kind_for(rel: str, title: str) -> str:
    name = Path(rel).stem
    if "学习路径" in name or "路径" in title:
        return "学习路径"
    if "专题总览" in name or "总览" in title:
        return "专题总览"
    if "索引" in name:
        return "索引"
    if "Runbook" in name or "Playbook" in name:
        return "动作"
    if "地图" in name or rel.startswith("20-Maps"):
        return "地图"
    if "第 " in name or "第" in name and "周" in name:
        return "任务"
    return "笔记"


def note_priority(rel: str, status: str, kind: str, title: str) -> int:
    score = 0
    if rel in PINNED:
        score += 100
    if status in {"active", "learning"}:
        score += 20
    if kind in {"学习路径", "专题总览", "任务", "地图"}:
        score += 15
    hot_words = ["深度实战", "基础设施", "Cube Studio", "内容更新", "今日入口", "AI 学习"]
    if any(w in title or w in rel for w in hot_words):
        score += 25
    return score


def collect_notes() -> list[Note]:
    notes: list[Note] = []
    seen: set[Path] = set()
    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            if path in seen or " - 旧库" in path.name:
                continue
            seen.add(path)
            rel = path.relative_to(ROOT).as_posix()
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            fm, body = parse_frontmatter(text)
            title = str(fm.get("title") or Path(rel).stem)
            status = str(fm.get("status") or "unknown")
            tags_obj = fm.get("tags") or []
            tags = tags_obj if isinstance(tags_obj, list) else [str(tags_obj)]
            kind = kind_for(rel, title)
            notes.append(
                Note(
                    title=title,
                    rel=rel,
                    domain=domain_for(rel),
                    status=status,
                    tags=[str(t) for t in tags],
                    mtime=path.stat().st_mtime,
                    summary=first_paragraph(body),
                    kind=kind,
                    priority=note_priority(rel, status, kind, title),
                )
            )
    return notes


def obsidian_uri(rel: str) -> str:
    return "obsidian://open?vault=tony-ai-wiki-2026&file=" + quote(rel, safe="")


def render_html(notes: list[Note]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    pinned = sorted([n for n in notes if n.rel in PINNED], key=lambda n: PINNED.index(n.rel))
    recent = sorted(notes, key=lambda n: n.mtime, reverse=True)[:36]
    domains: dict[str, int] = {}
    for n in notes:
        domains[n.domain] = domains.get(n.domain, 0) + 1

    payload = [
        {
            "title": n.title,
            "rel": n.rel,
            "domain": n.domain,
            "status": n.status,
            "tags": n.tags[:6],
            "summary": n.summary,
            "kind": n.kind,
            "priority": n.priority,
            "mtime": datetime.fromtimestamp(n.mtime).strftime("%Y-%m-%d"),
            "obsidian": obsidian_uri(n.rel),
            "relative": "../" + quote(n.rel),
        }
        for n in notes
    ]
    payload_json = json.dumps(payload, ensure_ascii=False)

    pinned_cards = "\n".join(card_html(n) for n in pinned)
    recent_cards = "\n".join(card_html(n) for n in recent[:12])
    domain_rows = "\n".join(
        f"<button class='chip' data-domain='{html.escape(k)}'>{html.escape(k)}<span>{v}</span></button>"
        for k, v in sorted(domains.items(), key=lambda x: (-x[1], x[0]))
    )

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Tony 阅读控制台</title>
  <style>{CSS}</style>
</head>
<body>
  <aside class="sidebar">
    <div class="brand">
      <div class="brand-icon">T</div>
      <div><strong>阅读控制台</strong><span>Tony AI Wiki</span></div>
    </div>
    <nav>
      <a href="#today" class="active">今日待读</a>
      <a href="#recent">最近更新</a>
      <a href="#domains">领域入口</a>
      <a href="#search">主题检索</a>
      <a href="#digest">沉淀动作</a>
    </nav>
    <div class="side-note">生成时间<br>{html.escape(now)}</div>
  </aside>
  <main>
    <header class="topbar">
      <div>
        <h1>今天先读什么？</h1>
        <p>把知识库从“目录导航”变成“阅读、判断、沉淀”的工作台。</p>
      </div>
      <a class="ghost" href="./今日入口.md">返回今日入口</a>
    </header>

    <section class="stats">
      <div><span>{len(notes)}</span><label>可读页面</label></div>
      <div><span>{len(domains)}</span><label>领域</label></div>
      <div><span>{len(pinned)}</span><label>推荐入口</label></div>
      <div><span>{len(recent)}</span><label>最近更新</label></div>
    </section>

    <section id="today" class="panel">
      <div class="section-title">
        <div><h2>今日待读</h2><p>不是按文件树读，而是按当前主线读。</p></div>
        <span class="badge">Fangbm-style digest</span>
      </div>
      <div class="grid">{pinned_cards}</div>
    </section>

    <section id="recent" class="panel">
      <div class="section-title">
        <div><h2>最近更新</h2><p>最近 7 天最可能值得回看的页面。</p></div>
      </div>
      <div class="grid compact">{recent_cards}</div>
    </section>

    <section id="domains" class="panel">
      <div class="section-title">
        <div><h2>按领域进入</h2><p>先选领域，再选路径、索引或地图。</p></div>
      </div>
      <div class="chips">{domain_rows}</div>
      <div id="domain-results" class="list"></div>
    </section>

    <section id="search" class="panel">
      <div class="section-title">
        <div><h2>主题检索</h2><p>输入关键词，快速找入口页、索引页和最近沉淀。</p></div>
      </div>
      <div class="searchbar">
        <input id="q" placeholder="例如：Mac AI、Cube Studio、Agent Memory、支付、Security">
        <button id="clear">清空</button>
      </div>
      <div id="results" class="list"></div>
    </section>

    <section id="digest" class="panel actions">
      <div class="section-title">
        <div><h2>读完之后</h2><p>每次阅读只做一个沉淀动作，避免越读越散。</p></div>
      </div>
      <div class="action-grid">
        <div><strong>保留</strong><p>这页值得以后复用，补到最近的专题总览或学习路径。</p></div>
        <div><strong>放大</strong><p>这只是一个点，应该扩成一条 line 或 surface。</p></div>
        <div><strong>丢弃</strong><p>低价值、重复、过期，记录原因，不继续追。</p></div>
        <div><strong>发布</strong><p>需要手机或公司电脑阅读时，再生成 output-feishu projection。</p></div>
      </div>
    </section>
  </main>
  <script>const NOTES = {payload_json};{JS}</script>
</body>
</html>
"""


def card_html(n: Note) -> str:
    tags = "".join(f"<span>{html.escape(t)}</span>" for t in ([n.kind, n.status, n.domain] + n.tags[:2]) if t)
    return f"""
    <article class="card">
      <div class="meta">{tags}</div>
      <h3>{html.escape(n.title)}</h3>
      <p>{html.escape(n.summary or "打开阅读，补一条自己的判断。")}</p>
      <div class="card-actions">
        <a href="{html.escape(obsidian_uri(n.rel))}">Obsidian 打开</a>
        <a href="../{quote(n.rel)}">浏览器查看</a>
      </div>
    </article>"""


CSS = r"""
*{box-sizing:border-box}body{margin:0;background:#f6f7f8;color:#172033;font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",Arial,sans-serif}a{color:inherit}.sidebar{position:fixed;inset:0 auto 0 0;width:244px;background:#fff;border-right:1px solid #e6e9ef;padding:18px 14px;display:flex;flex-direction:column}.brand{display:flex;gap:12px;align-items:center;padding:6px 8px 18px;border-bottom:1px solid #eef1f4}.brand-icon{width:40px;height:40px;border-radius:12px;background:#0f9f6e;color:white;display:grid;place-items:center;font-weight:800;box-shadow:0 14px 30px -14px #0f9f6e}.brand strong{display:block;font-size:15px}.brand span{display:block;color:#8a93a3;font-size:12px;margin-top:2px}nav{padding:18px 0;display:grid;gap:4px}nav a{padding:10px 12px;text-decoration:none;border-radius:10px;color:#536074;font-size:14px}nav a:hover,nav a.active{background:#eaf8f2;color:#08764e}.side-note{margin-top:auto;color:#98a2b3;font-size:12px;line-height:1.7;padding:12px}main{margin-left:244px;min-height:100vh}.topbar{position:sticky;top:0;z-index:3;background:rgba(255,255,255,.86);backdrop-filter:blur(12px);border-bottom:1px solid #e6e9ef;padding:22px 34px;display:flex;justify-content:space-between;gap:18px;align-items:center}.topbar h1{margin:0;font-size:24px;letter-spacing:0}.topbar p{margin:6px 0 0;color:#748094}.ghost{border:1px solid #dfe5ec;background:#fff;border-radius:10px;padding:9px 13px;text-decoration:none;color:#475569;font-size:14px;white-space:nowrap}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;padding:26px 34px 0}.stats div{background:#fff;border:1px solid #edf0f4;border-radius:14px;padding:18px 20px;box-shadow:0 8px 24px -20px #0f172a}.stats span{display:block;font-size:27px;font-weight:800;color:#0f9f6e}.stats label{display:block;margin-top:4px;color:#8b95a5;font-size:12px}.panel{margin:24px 34px;background:#fff;border:1px solid #e9edf2;border-radius:18px;padding:22px;box-shadow:0 10px 32px -28px #0f172a}.section-title{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;margin-bottom:18px}.section-title h2{margin:0;font-size:18px}.section-title p{margin:5px 0 0;color:#7a8597;font-size:13px}.badge{font-size:12px;background:#eaf8f2;color:#08764e;border-radius:999px;padding:6px 10px}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.grid.compact{grid-template-columns:repeat(3,minmax(0,1fr))}.card{border:1px solid #eef1f4;border-radius:14px;padding:16px;background:linear-gradient(180deg,#fff,#fbfcfd);transition:all .15s}.card:hover{border-color:#a6ead0;box-shadow:0 14px 30px -24px #059669;transform:translateY(-1px)}.card h3{margin:10px 0 8px;font-size:16px;line-height:1.35}.card p{margin:0;color:#647084;font-size:13px;line-height:1.65;min-height:42px}.meta{display:flex;flex-wrap:wrap;gap:6px}.meta span{font-size:11px;background:#f1f5f9;color:#5c6676;border-radius:999px;padding:3px 7px}.card-actions{display:flex;gap:10px;margin-top:14px}.card-actions a{font-size:13px;color:#08764e;text-decoration:none}.chips{display:flex;flex-wrap:wrap;gap:9px}.chip{border:1px solid #e0e6ed;background:#fff;border-radius:999px;padding:8px 12px;color:#465469;cursor:pointer}.chip:hover{border-color:#0f9f6e;color:#08764e}.chip span{margin-left:6px;color:#99a3b2}.searchbar{display:flex;gap:10px}.searchbar input{flex:1;border:1px solid #dfe5ec;border-radius:12px;padding:12px 14px;font-size:14px;outline:none}.searchbar input:focus{border-color:#0f9f6e;box-shadow:0 0 0 3px rgba(15,159,110,.12)}.searchbar button{border:0;border-radius:12px;padding:0 16px;background:#eef2f6;color:#4b586b}.list{display:grid;gap:10px;margin-top:16px}.row{border:1px solid #edf0f4;border-radius:12px;padding:13px 14px;display:grid;grid-template-columns:1fr auto;gap:12px;align-items:center}.row strong{display:block;font-size:14px}.row p{margin:4px 0 0;color:#7a8597;font-size:12px}.row a{color:#08764e;text-decoration:none;font-size:13px}.action-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.action-grid div{background:#f8fafc;border:1px solid #edf0f4;border-radius:14px;padding:16px}.action-grid strong{font-size:15px}.action-grid p{font-size:13px;color:#6b7688;line-height:1.6;margin:8px 0 0}@media(max-width:980px){.sidebar{position:static;width:auto}.brand{border:0}nav{grid-template-columns:repeat(3,1fr)}main{margin:0}.stats,.grid,.grid.compact,.action-grid{grid-template-columns:1fr}.topbar{position:static;align-items:flex-start;flex-direction:column}}
"""


JS = r"""
function row(n){return `<div class="row"><div><strong>${escapeHtml(n.title)}</strong><p>${escapeHtml(n.domain)} · ${escapeHtml(n.kind)} · ${escapeHtml(n.mtime)}<br>${escapeHtml(n.summary||'打开阅读，补一条自己的判断。')}</p></div><a href="${n.obsidian}">打开</a></div>`}
function escapeHtml(s){return String(s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]))}
const q=document.getElementById('q'), results=document.getElementById('results'), clear=document.getElementById('clear'), domainResults=document.getElementById('domain-results');
function renderSearch(){const term=q.value.trim().toLowerCase(); if(!term){results.innerHTML='<p class="muted">输入关键词后显示结果。</p>'; return} const out=NOTES.filter(n=>(n.title+n.rel+n.domain+n.summary+n.tags.join(' ')).toLowerCase().includes(term)).sort((a,b)=>b.priority-a.priority).slice(0,24); results.innerHTML=out.length?out.map(row).join(''):'<p class="muted">没有匹配结果。</p>'}
q.addEventListener('input',renderSearch); clear.onclick=()=>{q.value='';renderSearch();q.focus()};
document.querySelectorAll('.chip').forEach(btn=>btn.addEventListener('click',()=>{const d=btn.dataset.domain; const out=NOTES.filter(n=>n.domain===d).sort((a,b)=>b.priority-a.priority).slice(0,18); domainResults.innerHTML=out.map(row).join('')}));
renderSearch();
"""


def render_md() -> str:
    return """---
title: 阅读控制台
created: 2026-06-23
updated: 2026-06-23
status: active
tags:
  - home
  - reading
  - dashboard
---

# 阅读控制台

这是一版受 `fangbm.cc` 启发的本地阅读工作台。它不替代 Obsidian 知识库，只负责回答：

```text
我现在打开知识库，先看什么？
哪些内容最近更新？
读完之后该保留、放大、丢弃还是发布？
```

## 打开

- [阅读控制台 HTML](阅读控制台.html)

## 生成方式

```bash
python3 scripts/build-reading-console.py
```

## 当前定位

- `00-Home/今日入口`：每日第一屏；
- `00-Home/阅读控制台.html`：像信息流工作台一样阅读；
- `20-Maps/知识导航门户`：按领域和问题进入；
- `10-Knowledge/*`：正式知识资产。
"""


def main() -> None:
    notes = collect_notes()
    OUT.write_text(render_html(notes), encoding="utf-8")
    MD_OUT.write_text(render_md(), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(f"wrote {MD_OUT.relative_to(ROOT)}")
    print(f"notes {len(notes)}")


if __name__ == "__main__":
    main()
