// Takes each mock-up's screenshot, measures its regions, and takes each component's element screenshots.
// Usage: node shoot.js plan.json ../shots
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const [, , planPath, outDir] = process.argv;
  const plan = JSON.parse(fs.readFileSync(planPath, 'utf8'));
  fs.mkdirSync(path.join(outDir, 'components'), { recursive: true });
  const browser = await chromium.launch();
  const regions = {};
  const byShot = Object.fromEntries(plan.shots.map((s) => [s.shot, s]));
  for (const s of plan.shots) {
    const page = await browser.newPage({ viewport: { width: s.width, height: 900 }, deviceScaleFactor: 1 });
    await page.goto('file://' + s.html);
    await page.screenshot({ path: path.join(outDir, `${s.shot}.png`), fullPage: true });
    const size = await page.evaluate(() => ({ w: document.documentElement.scrollWidth, h: document.documentElement.scrollHeight }));
    const found = await page.$$eval('[data-region]', (els) => els.map((el) => {
      const r = el.getBoundingClientRect();
      return { code: el.dataset.region, label: el.dataset.label, x: Math.round(r.left + scrollX), y: Math.round(r.top + scrollY), w: Math.round(r.width), h: Math.round(r.height) };
    }));
    regions[s.shot] = { size, regions: found };
    await page.close();
  }
  for (const c of plan.components) {
    for (const [state, shot] of c.states) {
      const s = byShot[shot];
      const page = await browser.newPage({ viewport: { width: s.width, height: 900 }, deviceScaleFactor: 1 });
      await page.goto('file://' + s.html);
      const el = await page.$(c.selector);
      const name = `${c.id}-${state.replace(/[^a-z0-9]+/gi, '-').toLowerCase()}.png`;
      if (el) await el.screenshot({ path: path.join(outDir, 'components', name) });
      await page.close();
    }
  }
  fs.writeFileSync(path.join(outDir, 'regions.json'), JSON.stringify(regions, null, 2));
  await browser.close();
  console.log(`shot ${plan.shots.length} mock-ups`);
})();
