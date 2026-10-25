// Rend chaque fichier HTML du dossier en PNG 1000×1500 (Chromium headless).
// Usage : node render.js <dossier_html> <dossier_png>
const { chromium } = require('playwright-core');
const fs = require('fs');
const path = require('path');
(async () => {
  const [src, out] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage({ viewport: { width: 1000, height: 1500 } });
  for (const file of fs.readdirSync(src).filter((f) => f.endsWith('.html')).sort()) {
    await page.goto('file://' + path.resolve(src, file));
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(out, file.replace('.html', '.png')) });
    console.log('ok', file);
  }
  await browser.close();
})();
