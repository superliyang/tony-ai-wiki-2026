const ROUND_PACKS = [
  {
    id: 'alpha',
    name: 'Board Alpha',
    rows: [
      'SWIFTAF',
      'REWARDO',
      'CLEVELC',
      'OGLIDEU',
      'MTIMESS',
      'BPUZZLE',
      'OVECTOR',
    ],
    words: [
      { word: 'SWIFT', cells: [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]] },
      { word: 'FOCUS', cells: [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6]] },
      { word: 'GLIDE', cells: [[3, 1], [3, 2], [3, 3], [3, 4], [3, 5]] },
      { word: 'COMBO', cells: [[2, 0], [3, 0], [4, 0], [5, 0], [6, 0]] },
    ],
  },
  {
    id: 'bravo',
    name: 'Board Bravo',
    rows: [
      'MATCHUP',
      'SIGNALR',
      'ETEMPOH',
      'ACLIPSY',
      'SHARPIT',
      'LADDERH',
      'QLEVELM',
    ],
    words: [
      { word: 'MATCH', cells: [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]] },
      { word: 'SIGNAL', cells: [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5]] },
      { word: 'LADDER', cells: [[5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]] },
      { word: 'RHYTHM', cells: [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6]] },
    ],
  },
  {
    id: 'charlie',
    name: 'Board Charlie',
    rows: [
      'PIXELUP',
      'PUZZLES',
      'XTARGET',
      'IMPACTS',
      'STREAKO',
      'GLIDERS',
      'AMOTION',
    ],
    words: [
      { word: 'PIXEL', cells: [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]] },
      { word: 'TARGET', cells: [[2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6]] },
      { word: 'STREAK', cells: [[4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5]] },
      { word: 'MOTION', cells: [[6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6]] },
    ],
  },
  {
    id: 'delta',
    name: 'Board Delta',
    rows: [
      'REWARDX',
      'OTEMPOY',
      'GRESULT',
      'ICLIPSO',
      'CTARGET',
      'STREAKP',
      'QPUZZLE',
    ],
    words: [
      { word: 'REWARD', cells: [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]] },
      { word: 'TEMPO', cells: [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]] },
      { word: 'RESULT', cells: [[2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6]] },
      { word: 'TARGET', cells: [[4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6]] },
      { word: 'STREAK', cells: [[5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]] },
    ],
  },
  {
    id: 'echo',
    name: 'Board Echo',
    rows: [
      'ARCADES',
      'LVECTOR',
      'EMOTION',
      'VTIMING',
      'EGLIDEX',
      'LLEVELS',
      'RREWARD',
    ],
    words: [
      { word: 'ARCADE', cells: [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]] },
      { word: 'MOTION', cells: [[2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6]] },
      { word: 'TIMING', cells: [[3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6]] },
      { word: 'LEVEL', cells: [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5]] },
      { word: 'REWARD', cells: [[6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6]] },
    ],
  },
];

const HISTORY_KEY = 'word-search-duel-history-v1';
const MAX_HISTORY = 6;
const AUDIO_KEY = 'word-search-duel-audio-v1';

const screens = {
  start: document.getElementById('screen-start'),
  tutorial: document.getElementById('screen-tutorial'),
  match: document.getElementById('screen-match'),
  result: document.getElementById('screen-result'),
};

const ui = {
  timer: document.getElementById('timer'),
  score: document.getElementById('score'),
  streak: document.getElementById('streak'),
  wordsFound: document.getElementById('words-found'),
  soundToggleBtn: document.getElementById('sound-toggle-btn'),
  comboBanner: document.getElementById('combo-banner'),
  countdownOverlay: document.getElementById('countdown-overlay'),
  countdownValue: document.getElementById('countdown-value'),
  boardName: document.getElementById('board-name'),
  boardProgress: document.getElementById('board-progress'),
  boardWrap: document.getElementById('board-wrap'),
  selectionOverlay: document.getElementById('selection-overlay'),
  board: document.getElementById('board'),
  selectionWord: document.getElementById('selection-word'),
  feedback: document.getElementById('feedback'),
  targetList: document.getElementById('target-list'),
  bestScoreStat: document.getElementById('best-score-stat'),
  gamesPlayedStat: document.getElementById('games-played-stat'),
  lastOutcomeStat: document.getElementById('last-outcome-stat'),
  recentMatches: document.getElementById('recent-matches'),
  recentSummaryText: document.getElementById('recent-summary-text'),
  resultTitle: document.getElementById('result-title'),
  finalScore: document.getElementById('final-score'),
  opponentScore: document.getElementById('opponent-score'),
  deltaScore: document.getElementById('delta-score'),
  finalWordsFound: document.getElementById('final-words-found'),
  finalErrors: document.getElementById('final-errors'),
  bestStreak: document.getElementById('best-streak'),
  resultExplainer: document.getElementById('result-explainer'),
  breakdownList: document.getElementById('breakdown-list'),
};

const state = {
  durationSeconds: 60,
  matchId: null,
  currentPackIndex: 0,
  currentPack: null,
  foundWordsInPack: new Set(),
  foundCells: new Set(),
  selectedCells: [],
  wordsFoundCount: 0,
  errors: 0,
  streak: 0,
  bestStreak: 0,
  streakBonus: 0,
  secondsLeft: 60,
  timerId: null,
  startedAt: null,
  dragging: false,
  activePointerId: null,
  flashCells: new Set(),
  comboBannerTimer: null,
  audioEnabled: true,
  audioContext: null,
};

function showScreen(name) {
  Object.values(screens).forEach((screen) => screen.classList.add('hidden'));
  screens[name].classList.remove('hidden');
}

async function api(path, options = {}) {
  const res = await fetch(path, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  });
  if (!res.ok) {
    throw new Error(`API ${path} failed: ${res.status}`);
  }
  return res.json();
}

function keyForCell(row, col) {
  return `${row}:${col}`;
}

function selectionWord() {
  if (!state.currentPack || state.selectedCells.length === 0) return '';
  return state.selectedCells
    .map(([row, col]) => state.currentPack.rows[row][col])
    .join('');
}

function loadHistory() {
  try {
    const raw = localStorage.getItem(HISTORY_KEY);
    if (!raw) return [];
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed : [];
  } catch (error) {
    console.warn('failed to load history', error);
    return [];
  }
}

function saveHistory(entries) {
  localStorage.setItem(HISTORY_KEY, JSON.stringify(entries.slice(0, MAX_HISTORY)));
}

function loadAudioPreference() {
  try {
    const raw = localStorage.getItem(AUDIO_KEY);
    return raw === null ? true : raw === 'on';
  } catch {
    return true;
  }
}

function saveAudioPreference(enabled) {
  localStorage.setItem(AUDIO_KEY, enabled ? 'on' : 'off');
}

function renderAudioToggle() {
  ui.soundToggleBtn.textContent = `音效：${state.audioEnabled ? '开' : '关'}`;
}

function formatHistoryTime(playedAt) {
  const date = new Date(playedAt);
  return new Intl.DateTimeFormat('zh-CN', {
    month: 'numeric',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  }).format(date);
}

function renderHistoryPanel() {
  const history = loadHistory();
  ui.gamesPlayedStat.textContent = String(history.length);
  ui.bestScoreStat.textContent = history.length ? String(Math.max(...history.map((item) => item.score))) : '--';
  ui.lastOutcomeStat.textContent = history.length ? (history[0].outcome === 'win' ? '最近赢了' : '最近惜败') : '暂无';
  ui.recentSummaryText.textContent = history.length
    ? `最近 ${Math.min(history.length, MAX_HISTORY)} 局的试玩表现`
    : '首轮试玩后会在这里留下历史记录。';

  ui.recentMatches.innerHTML = '';
  if (!history.length) {
    const li = document.createElement('li');
    li.innerHTML = '<div><strong>还没有历史战绩</strong><small>先打一局，看看分数和对手差值。</small></div><span class="outcome-badge">empty</span><span>准备开始</span>';
    ui.recentMatches.appendChild(li);
    return;
  }

  history.forEach((entry) => {
    const li = document.createElement('li');
    li.innerHTML = `
      <div>
        <strong>${entry.score} 分 · ${entry.wordsFound} 词</strong>
        <small>${formatHistoryTime(entry.playedAt)}</small>
      </div>
      <span class="outcome-badge ${entry.outcome}">${entry.outcome === 'win' ? 'win' : 'loss'}</span>
      <span>${entry.bestStreak}x 连击</span>
    `;
    ui.recentMatches.appendChild(li);
  });
}

function appendHistoryEntry(result) {
  const history = loadHistory();
  history.unshift({
    matchId: state.matchId,
    score: result.total_score,
    wordsFound: state.wordsFoundCount,
    errors: state.errors,
    bestStreak: state.bestStreak,
    delta: result.delta_to_opponent,
    outcome: result.outcome,
    playedAt: new Date().toISOString(),
  });
  saveHistory(history);
  renderHistoryPanel();
}

function computeScore() {
  return state.wordsFoundCount * 10 + state.streakBonus - state.errors * 2;
}

async function ensureAudioReady() {
  if (!state.audioEnabled) return null;
  const AudioContextClass = window.AudioContext || window.webkitAudioContext;
  if (!AudioContextClass) return null;
  if (!state.audioContext) {
    state.audioContext = new AudioContextClass();
  }
  if (state.audioContext.state === 'suspended') {
    await state.audioContext.resume();
  }
  return state.audioContext;
}

async function playTone({ frequency, duration = 0.08, type = 'sine', gain = 0.04, delay = 0 }) {
  const ctx = await ensureAudioReady();
  if (!ctx) return;
  const osc = ctx.createOscillator();
  const amp = ctx.createGain();
  const start = ctx.currentTime + delay;
  const stop = start + duration;
  osc.type = type;
  osc.frequency.setValueAtTime(frequency, start);
  amp.gain.setValueAtTime(0.0001, start);
  amp.gain.exponentialRampToValueAtTime(gain, start + 0.01);
  amp.gain.exponentialRampToValueAtTime(0.0001, stop);
  osc.connect(amp);
  amp.connect(ctx.destination);
  osc.start(start);
  osc.stop(stop);
}

function playHitSound() {
  playTone({ frequency: 620, duration: 0.08, type: 'triangle', gain: 0.035 });
  playTone({ frequency: 780, duration: 0.09, type: 'triangle', gain: 0.028, delay: 0.04 });
}

function playMissSound() {
  playTone({ frequency: 230, duration: 0.1, type: 'sawtooth', gain: 0.03 });
}

function playBoardClearSound() {
  playTone({ frequency: 523, duration: 0.08, type: 'triangle', gain: 0.03 });
  playTone({ frequency: 659, duration: 0.08, type: 'triangle', gain: 0.03, delay: 0.05 });
  playTone({ frequency: 784, duration: 0.12, type: 'triangle', gain: 0.035, delay: 0.1 });
}

function playCountdownTick(isGo = false) {
  if (isGo) {
    playTone({ frequency: 880, duration: 0.12, type: 'square', gain: 0.028 });
    return;
  }
  playTone({ frequency: 440, duration: 0.06, type: 'square', gain: 0.022 });
}

function playResultSound(outcome) {
  if (outcome === 'win') {
    playTone({ frequency: 523, duration: 0.08, type: 'triangle', gain: 0.03 });
    playTone({ frequency: 659, duration: 0.08, type: 'triangle', gain: 0.03, delay: 0.05 });
    playTone({ frequency: 880, duration: 0.14, type: 'triangle', gain: 0.035, delay: 0.1 });
  } else {
    playTone({ frequency: 280, duration: 0.08, type: 'sine', gain: 0.028 });
    playTone({ frequency: 220, duration: 0.12, type: 'sine', gain: 0.024, delay: 0.06 });
  }
}

function renderHud() {
  ui.timer.textContent = String(state.secondsLeft);
  ui.score.textContent = String(computeScore());
  ui.streak.textContent = String(state.streak);
  ui.wordsFound.textContent = String(state.wordsFoundCount);
}

function setFeedback(message, tone = 'neutral') {
  ui.feedback.textContent = message;
  ui.feedback.className = 'feedback';
  if (tone === 'success') ui.feedback.classList.add('success');
  if (tone === 'error') ui.feedback.classList.add('error');
}

function showComboBanner(message) {
  if (state.comboBannerTimer) {
    window.clearTimeout(state.comboBannerTimer);
  }
  ui.comboBanner.textContent = message;
  ui.comboBanner.classList.remove('hidden');
  ui.comboBanner.classList.remove('show');
  void ui.comboBanner.offsetWidth;
  ui.comboBanner.classList.add('show');
  state.comboBannerTimer = window.setTimeout(() => {
    ui.comboBanner.classList.add('hidden');
    ui.comboBanner.classList.remove('show');
  }, 1100);
}

async function runCountdown() {
  const sequence = ['3', '2', '1', 'GO'];
  ui.countdownOverlay.classList.remove('hidden');
  for (const step of sequence) {
    ui.countdownValue.textContent = step;
    ui.countdownOverlay.classList.remove('show');
    void ui.countdownOverlay.offsetWidth;
    ui.countdownOverlay.classList.add('show');
    playCountdownTick(step === 'GO');
    await new Promise((resolve) => window.setTimeout(resolve, step === 'GO' ? 260 : 420));
  }
  ui.countdownOverlay.classList.add('hidden');
  ui.countdownOverlay.classList.remove('show');
}

function renderSelection() {
  ui.selectionWord.textContent = selectionWord() || '-';
}

function renderSelectionOverlay() {
  ui.selectionOverlay.innerHTML = '';
  if (state.selectedCells.length === 0) return;

  const boardRect = ui.board.getBoundingClientRect();
  const points = state.selectedCells.map(([row, col]) => {
    const cell = ui.board.querySelector(`[data-row="${row}"][data-col="${col}"]`);
    if (!cell) return null;
    const rect = cell.getBoundingClientRect();
    return {
      x: ((rect.left + rect.width / 2 - boardRect.left) / boardRect.width) * 100,
      y: ((rect.top + rect.height / 2 - boardRect.top) / boardRect.height) * 100,
    };
  }).filter(Boolean);

  if (!points.length) return;

  if (points.length > 1) {
    const polyline = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
    polyline.setAttribute('class', 'selection-path');
    polyline.setAttribute('points', points.map((point) => `${point.x},${point.y}`).join(' '));
    ui.selectionOverlay.appendChild(polyline);
  }

  points.forEach((point) => {
    const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    circle.setAttribute('class', 'selection-dot');
    circle.setAttribute('cx', String(point.x));
    circle.setAttribute('cy', String(point.y));
    circle.setAttribute('r', '2.8');
    ui.selectionOverlay.appendChild(circle);
  });
}

function renderBoard() {
  ui.board.innerHTML = '';
  state.currentPack.rows.forEach((rowText, rowIndex) => {
    rowText.split('').forEach((letter, colIndex) => {
      const key = keyForCell(rowIndex, colIndex);
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'cell';
      button.dataset.row = String(rowIndex);
      button.dataset.col = String(colIndex);
      if (state.selectedCells.some(([r, c]) => r === rowIndex && c === colIndex)) {
        button.classList.add('selected');
      }
      if (state.foundCells.has(key)) {
        button.classList.add('found');
        button.disabled = true;
      }
      if (state.flashCells.has(key)) {
        button.classList.add('flash');
      }
      button.textContent = letter;
      ui.board.appendChild(button);
    });
  });
}

function renderTargetList() {
  ui.targetList.innerHTML = '';
  state.currentPack.words.forEach((entry) => {
    const li = document.createElement('li');
    if (state.foundWordsInPack.has(entry.word)) {
      li.classList.add('found');
    }
    li.innerHTML = `<span>${entry.word}</span><span class="badge">${state.foundWordsInPack.has(entry.word) ? 'found' : 'target'}</span>`;
    ui.targetList.appendChild(li);
  });
}

function renderMatch() {
  ui.boardName.textContent = state.currentPack.name;
  ui.boardProgress.textContent = `${(state.currentPackIndex % ROUND_PACKS.length) + 1} / ${ROUND_PACKS.length}`;
  renderHud();
  renderSelection();
  renderBoard();
  renderSelectionOverlay();
  renderTargetList();
}

async function emit(eventName, payload = {}) {
  try {
    await api('/events', {
      method: 'POST',
      body: JSON.stringify({
        events: [{
          event_name: eventName,
          player_id: 'local-player',
          match_id: state.matchId,
          emitted_at: new Date().toISOString(),
          payload,
        }],
      }),
    });
  } catch (error) {
    console.error('emit failed', error);
  }
}

async function loadTournament() {
  const tournament = await api('/tournament/current');
  state.durationSeconds = tournament.duration_seconds;
}

function resetSession() {
  state.matchId = `match-${Date.now()}`;
  state.currentPackIndex = 0;
  state.wordsFoundCount = 0;
  state.errors = 0;
  state.streak = 0;
  state.bestStreak = 0;
  state.streakBonus = 0;
  state.secondsLeft = state.durationSeconds;
  state.startedAt = Date.now();
  state.flashCells = new Set();
  ui.comboBanner.classList.add('hidden');
  ui.comboBanner.classList.remove('show');
}

function loadPack(index) {
  state.currentPack = ROUND_PACKS[index % ROUND_PACKS.length];
  state.foundWordsInPack = new Set();
  state.foundCells = new Set();
  state.selectedCells = [];
  renderMatch();
  emit('board_loaded', { board_id: state.currentPack.id, board_name: state.currentPack.name });
}

function isAdjacent(a, b) {
  return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]) === 1;
}

function directionOf(cells) {
  if (cells.length < 2) return null;
  const [r1, c1] = cells[cells.length - 2];
  const [r2, c2] = cells[cells.length - 1];
  return [Math.sign(r2 - r1), Math.sign(c2 - c1)];
}

function canAppendCell(row, col) {
  const next = [row, col];
  const existingIndex = state.selectedCells.findIndex(([r, c]) => r === row && c === col);
  if (existingIndex !== -1) {
    return false;
  }
  if (state.selectedCells.length === 0) return true;
  const last = state.selectedCells[state.selectedCells.length - 1];
  if (!isAdjacent(last, next)) return false;
  if (state.selectedCells.length === 1) return true;
  const direction = directionOf(state.selectedCells);
  const candidateDirection = [Math.sign(next[0] - last[0]), Math.sign(next[1] - last[1])];
  return direction[0] === candidateDirection[0] && direction[1] === candidateDirection[1];
}

function getCellFromTarget(target) {
  const cell = target instanceof Element ? target.closest('.cell') : null;
  if (!cell || !ui.board.contains(cell)) return null;
  return cell;
}

function getCoordsFromCell(cell) {
  return [Number(cell.dataset.row), Number(cell.dataset.col)];
}

function getCellFromPoint(clientX, clientY) {
  const element = document.elementFromPoint(clientX, clientY);
  return getCellFromTarget(element);
}

function onCellSelected(row, col) {
  const key = keyForCell(row, col);
  if (state.foundCells.has(key)) return;

  if (!canAppendCell(row, col)) {
    setFeedback('保持一条连续直线滑动选词。', 'error');
    return;
  }

  state.selectedCells.push([row, col]);
  renderMatch();
}

function clearSelection() {
  state.dragging = false;
  state.activePointerId = null;
  state.selectedCells = [];
  renderMatch();
  setFeedback('已清空选择，换一条线试试。');
}

function flashFoundCells(cells) {
  state.flashCells = new Set(cells.map(([row, col]) => keyForCell(row, col)));
  renderBoard();
  window.setTimeout(() => {
    state.flashCells = new Set();
    renderBoard();
  }, 380);
}

function pulseBoardWrap() {
  ui.boardWrap.classList.remove('board-cleared');
  void ui.boardWrap.offsetWidth;
  ui.boardWrap.classList.add('board-cleared');
  window.setTimeout(() => {
    ui.boardWrap.classList.remove('board-cleared');
  }, 500);
}

function shakeBoardWrap() {
  ui.boardWrap.classList.remove('board-miss');
  void ui.boardWrap.offsetWidth;
  ui.boardWrap.classList.add('board-miss');
  window.setTimeout(() => {
    ui.boardWrap.classList.remove('board-miss');
  }, 320);
}

function pathSignature(cells) {
  return cells.map(([row, col]) => keyForCell(row, col)).join('|');
}

function reverseSignature(cells) {
  return [...cells].reverse().map(([row, col]) => keyForCell(row, col)).join('|');
}

async function advanceBoardIfNeeded() {
  if (state.foundWordsInPack.size !== state.currentPack.words.length) return;
  await emit('board_cleared', { board_id: state.currentPack.id, words_found: state.foundWordsInPack.size });
  pulseBoardWrap();
  showComboBanner(`Board Cleared · ${state.currentPack.name}`);
  playBoardClearSound();
  state.currentPackIndex += 1;
  loadPack(state.currentPackIndex);
  setFeedback('字母盘完成，自动切到下一盘。', 'success');
}

function beginDrag(row, col, pointerId) {
  state.dragging = true;
  state.activePointerId = pointerId;
  state.selectedCells = [];
  onCellSelected(row, col);
}

async function endDrag(pointerId) {
  if (!state.dragging) return;
  if (state.activePointerId !== null && pointerId !== undefined && pointerId !== state.activePointerId) {
    return;
  }
  state.dragging = false;
  state.activePointerId = null;
  if (state.selectedCells.length < 2) {
    state.selectedCells = [];
    renderMatch();
    setFeedback('至少滑过两个字母再松手。', 'error');
    return;
  }
  await submitSelection();
}

async function submitSelection() {
  if (state.selectedCells.length === 0) {
    setFeedback('先选一条词线再提交。', 'error');
    return;
  }

  const currentSignature = pathSignature(state.selectedCells);
  const currentReverse = reverseSignature(state.selectedCells);
  const matched = state.currentPack.words.find((entry) => {
    if (state.foundWordsInPack.has(entry.word)) return false;
    const sig = pathSignature(entry.cells);
    return sig === currentSignature || sig === currentReverse;
  });

  if (matched) {
    state.foundWordsInPack.add(matched.word);
    matched.cells.forEach(([row, col]) => state.foundCells.add(keyForCell(row, col)));
    state.wordsFoundCount += 1;
    state.streak += 1;
    state.bestStreak = Math.max(state.bestStreak, state.streak);
    if (state.streak >= 2) {
      state.streakBonus += state.streak - 1;
    }
    await emit('word_found', {
      board_id: state.currentPack.id,
      word: matched.word,
      streak: state.streak,
      words_found_total: state.wordsFoundCount,
    });
    state.selectedCells = [];
    flashFoundCells(matched.cells);
    renderMatch();
    playHitSound();
    if (state.streak >= 2) {
      showComboBanner(`${state.streak}x Combo · ${matched.word}`);
    }
    setFeedback(`找到了 ${matched.word}，继续连击！`, 'success');
    await advanceBoardIfNeeded();
    return;
  }

  state.errors += 1;
  state.streak = 0;
  await emit('selection_miss', {
    board_id: state.currentPack.id,
    attempted_word: selectionWord(),
    error_count: state.errors,
  });
  state.selectedCells = [];
  renderMatch();
  shakeBoardWrap();
  playMissSound();
  setFeedback('这条词线不在目标列表里，再扫一眼。', 'error');
}

async function finishRound() {
  if (state.timerId) {
    clearInterval(state.timerId);
    state.timerId = null;
  }
  await emit('match_end', {
    words_found: state.wordsFoundCount,
    errors: state.errors,
    streak_bonus: state.streakBonus,
    best_streak: state.bestStreak,
  });
  const submit = await api('/match/submit-score', {
    method: 'POST',
    body: JSON.stringify({
      match_id: state.matchId,
      player_id: 'local-player',
      correct_count: state.wordsFoundCount,
      error_count: state.errors,
      streak_bonus: state.streakBonus,
      error_penalty: 2,
      duration_ms: Date.now() - state.startedAt,
      client_version: 'demo-web-0.2',
    }),
  });
  await emit('score_submitted', { total_score: submit.total_score });
  const result = await api(`/result/${state.matchId}`);
  await emit('result_received', { outcome: result.outcome, total_score: result.total_score });
  appendHistoryEntry(result);
  playResultSound(result.outcome);
  renderResult(result);
}

function renderResult(result) {
  showScreen('result');
  ui.resultTitle.textContent = result.outcome === 'win' ? '你赢了这轮扫描对决' : '这局还可以更快一点';
  ui.finalScore.textContent = String(result.total_score);
  ui.opponentScore.textContent = String(result.opponent_score);
  ui.deltaScore.textContent = result.delta_to_opponent > 0 ? `+${result.delta_to_opponent}` : `${result.delta_to_opponent}`;
  ui.finalWordsFound.textContent = String(state.wordsFoundCount);
  ui.finalErrors.textContent = String(state.errors);
  ui.bestStreak.textContent = String(state.bestStreak);
  ui.resultExplainer.textContent = result.explanation;
  ui.breakdownList.innerHTML = '';
  result.breakdown.forEach((item) => {
    const li = document.createElement('li');
    li.textContent = `${item.label}: ${item.value}`;
    ui.breakdownList.appendChild(li);
  });
}

async function startRound() {
  resetSession();
  showScreen('match');
  loadPack(0);
  renderMatch();
  setFeedback('准备开始，第一盘先找最明显的词。');
  emit('match_start', { duration_seconds: state.durationSeconds, mode: 'word_search_duel' });
  await runCountdown();
  state.timerId = setInterval(async () => {
    state.secondsLeft -= 1;
    renderHud();
    if (state.secondsLeft <= 0) {
      await finishRound();
    }
  }, 1000);
}

ui.board.addEventListener('pointerdown', (event) => {
  const cell = getCellFromTarget(event.target);
  if (!cell) return;
  if (cell.disabled) return;
  event.preventDefault();
  const [row, col] = getCoordsFromCell(cell);
  beginDrag(row, col, event.pointerId);
});

window.addEventListener('pointermove', (event) => {
  if (!state.dragging) return;
  if (state.activePointerId !== null && event.pointerId !== state.activePointerId) return;
  const cell = getCellFromPoint(event.clientX, event.clientY);
  if (!cell || cell.disabled) return;
  const [row, col] = getCoordsFromCell(cell);
  const last = state.selectedCells[state.selectedCells.length - 1];
  if (last && last[0] === row && last[1] === col) return;
  onCellSelected(row, col);
});

window.addEventListener('pointerup', async (event) => {
  await endDrag(event.pointerId);
});

window.addEventListener('pointercancel', async (event) => {
  await endDrag(event.pointerId);
});

document.getElementById('start-btn').addEventListener('click', async () => {
  await ensureAudioReady();
  await loadTournament();
  await emit('tutorial_start');
  showScreen('tutorial');
});

document.getElementById('tutorial-btn').addEventListener('click', async () => {
  await ensureAudioReady();
  await emit('tutorial_complete');
  await startRound();
});

document.getElementById('clear-selection-btn').addEventListener('click', clearSelection);

document.getElementById('rematch-btn').addEventListener('click', async () => {
  await ensureAudioReady();
  await emit('rematch_clicked');
  await startRound();
});

document.getElementById('home-btn').addEventListener('click', () => {
  renderHistoryPanel();
  showScreen('start');
});

ui.soundToggleBtn.addEventListener('click', async () => {
  state.audioEnabled = !state.audioEnabled;
  saveAudioPreference(state.audioEnabled);
  if (state.audioEnabled) {
    await ensureAudioReady();
    playHitSound();
  }
  renderAudioToggle();
});

window.addEventListener('resize', () => {
  if (!screens.match.classList.contains('hidden')) {
    renderSelectionOverlay();
  }
});

window.__wordSearchDuelTest = {
  async selectPath(cells) {
    state.selectedCells = [];
    cells.forEach(([row, col]) => onCellSelected(row, col));
    await submitSelection();
  },
  snapshot() {
    return {
      score: computeScore(),
      wordsFound: state.wordsFoundCount,
      streak: state.streak,
      bestStreak: state.bestStreak,
      feedback: ui.feedback.textContent,
    };
  },
  clearHistory() {
    localStorage.removeItem(HISTORY_KEY);
    renderHistoryPanel();
  },
};

state.audioEnabled = loadAudioPreference();
renderAudioToggle();
renderHistoryPanel();
showScreen('start');
