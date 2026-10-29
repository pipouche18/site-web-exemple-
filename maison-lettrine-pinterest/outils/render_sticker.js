// Rend les autocollants HTML en PDF 44 × 44 mm et en PNG 1200 dpi environ.
// Usage : node render_sticker.js <dossier_html> <dossier_sortie>
const { chromium } = require('playwright-core');
const fs = require('fs');
const path = require('path');
(async () => {
  const [src, out] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const file of fs.readdirSync(src).filter((f) => f.endsWith('.html'))) {
    const page = await browser.newPage({ viewport: { width: 166, height: 166 }, deviceScaleFactor: 12.5 });
    await page.goto('file://' + path.resolve(src, file));
    await page.evaluate(() => document.fonts.ready);
    const base = path.join(out, file.replace('.html', ''));
    await page.pdf({ path: base + '.pdf', width: '44mm', height: '44mm', printBackground: true, pageRanges: '1' });
    await page.screenshot({ path: base + '.png', clip: { x: 0, y: 0, width: 166.3, height: 166.3 } });
    console.log('ok', base);
    await page.close();
  }
  await browser.close();
})();
