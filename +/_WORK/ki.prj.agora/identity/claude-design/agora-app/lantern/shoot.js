// Screenshots each mock at iPhone size (393x852, 2x), measures data-region boxes and checks for clipped text.
// Usage: node shoot.js   (run from lantern/ after build.py)
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const mocks = path.join(__dirname, 'mocks');
  const out = path.join(__dirname, 'shots');
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const regions = {};
  for (const f of fs.readdirSync(mocks).filter((n) => n.endsWith('.html')).sort()) {
    const name = f.replace('.html', '');
    const page = await browser.newPage({ viewport: { width: 393, height: 852 }, deviceScaleFactor: 2 });
    await page.goto('file://' + path.join(mocks, f));
    await page.screenshot({ path: path.join(out, `${name}.png`), clip: { x: 0, y: 0, width: 393, height: 852 } });
    regions[name] = await page.$$eval('[data-region]', (els) => els.map((el) => {
      const r = el.getBoundingClientRect();
      return { code: el.dataset.region, label: el.dataset.label, x: +r.left.toFixed(1), y: +r.top.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) };
    }));
    // Clipped text: ellipsised or overflowing single-line elements, and any element past the right edge.
    const warn = await page.$$eval('.id, .state, .l2 .t, .l2 .f, .l2 .w, .gs, .sum, .key span, .name, .barnote', (els) => els
      .filter((el) => el.getBoundingClientRect().top < 740 && el.scrollWidth > el.clientWidth + 1 || el.getBoundingClientRect().right > 393)
      .map((el) => `${el.className}: ${el.textContent.trim().slice(0, 40)}`));
    if (warn.length) console.log(name, 'clipped:', warn);
    await page.close();
  }
  fs.writeFileSync(path.join(out, 'regions.json'), JSON.stringify(regions, null, 1));
  await browser.close();
  console.log('shot', Object.keys(regions).length);
})();
