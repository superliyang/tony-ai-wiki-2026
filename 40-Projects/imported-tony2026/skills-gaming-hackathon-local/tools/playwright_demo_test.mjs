import { chromium } from 'playwright';

const baseUrl = process.argv[2] || 'http://127.0.0.1:8000';

async function dragAcross(page, selectors) {
  const coords = selectors.map((selector) => {
    const match = selector.match(/data-row="(\d+)".*data-col="(\d+)"/);
    if (!match) throw new Error(`Unable to parse selector ${selector}`);
    return [Number(match[1]), Number(match[2])];
  });
  await page.evaluate(async (pathCoords) => {
    await window.__wordSearchDuelTest.selectPath(pathCoords);
  }, coords);
}

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1440, height: 1280 } });

try {
  await page.addInitScript(() => window.localStorage.clear());
  await page.route('**/tournament/current', async (route) => {
    const response = await route.fetch();
    const data = await response.json();
    data.duration_seconds = 3;
    await route.fulfill({
      response,
      json: data,
    });
  });

  await page.goto(baseUrl, { waitUntil: 'networkidle' });

  await page.getByRole('button', { name: '开始对局' }).click();
  await page.getByRole('button', { name: '开始首局' }).click();

  await page.waitForSelector('#board .cell');
  await page.waitForSelector('#countdown-overlay.hidden', { timeout: 4000 });
  await page.waitForTimeout(180);

  const submitButtonCount = await page.locator('#submit-selection-btn').count();
  if (submitButtonCount !== 0) {
    throw new Error('Submit button should not be visible in swipe mode');
  }

  await dragAcross(page, [
    '[data-row="0"][data-col="0"]',
    '[data-row="0"][data-col="1"]',
    '[data-row="0"][data-col="2"]',
    '[data-row="0"][data-col="3"]',
    '[data-row="0"][data-col="4"]'
  ]);

  await page.waitForTimeout(300);

  const score = await page.locator('#score').textContent();
  const found = await page.locator('#words-found').textContent();
  const feedback = await page.locator('#feedback').textContent();
  const foundBadge = await page.locator('#target-list li.found').count();
  const boardProgress = await page.locator('#board-progress').textContent();

  if (Number(score) < 10) {
    throw new Error(`Expected score to increase after swipe, got ${score}`);
  }
  if (Number(found) < 1) {
    throw new Error(`Expected at least one found word, got ${found}`);
  }
  if (foundBadge < 1) {
    throw new Error('Expected target list to mark a found word');
  }
  if (!boardProgress || !boardProgress.includes('/')) {
    throw new Error(`Expected board progress to render, got ${boardProgress}`);
  }

  await page.waitForSelector('#screen-result:not(.hidden)', { timeout: 6000 });
  const finalScore = await page.locator('#final-score').textContent();
  if (Number(finalScore) < 10) {
    throw new Error(`Expected final score on result page, got ${finalScore}`);
  }

  await page.getByRole('button', { name: '返回首页' }).click();
  await page.waitForSelector('#screen-start:not(.hidden)');
  const recentCount = await page.locator('#recent-matches li').count();
  const gamesPlayed = await page.locator('#games-played-stat').textContent();
  const bestScore = await page.locator('#best-score-stat').textContent();
  if (recentCount < 1) {
    throw new Error('Expected recent matches list to contain at least one entry');
  }
  if (Number(gamesPlayed) < 1) {
    throw new Error(`Expected games played stat to increment, got ${gamesPlayed}`);
  }

  console.log(JSON.stringify({
    ok: true,
    mode: 'word_search_duel',
    score: Number(score),
    wordsFound: Number(found),
    finalScore: Number(finalScore),
    feedback,
    boardProgress,
    gamesPlayed: Number(gamesPlayed),
    bestScore,
    recentCount,
    submitButtonCount,
    baseUrl,
  }, null, 2));
} finally {
  await browser.close();
}
