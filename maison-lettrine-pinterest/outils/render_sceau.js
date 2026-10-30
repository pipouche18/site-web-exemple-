// Rend chaque HTML « nom__LxH » en PDF (vectoriel) et PNG haute définition.
// Usage : node render_sceau.js <dossier_html> <dossier_sortie>
const { chromium } = require('playwright-core');
const fs = require('fs');
const path = require('path');
const toPx = (v) => (v.endsWith('mm') ? (parseFloat(v) * 96) / 25.4 : parseFloat(v));
(async () => {
  const [src, out] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const file of fs.readdirSync(src).filter((f) => f.endsWith('.html'))) {
    const [name, size] = file.replace('.html', '').split('__');
    const [w, h] = size.includes('mm') ? [size, size] : size.split('x').map((v) => v + 'px');
    const wpx = toPx(w), hpx = toPx(h);
    const scale = size.includes('mm') ? 2400 / wpx : 1;  // cachets : PNG ~2400 px
    const page = await browser.newPage({ viewport: { width: Math.ceil(wpx), height: Math.ceil(hpx) }, deviceScaleFactor: scale });
    await page.goto('file://' + path.resolve(src, file));
    await page.evaluate(() => document.fonts.ready);
    if (size.includes('mm')) await page.pdf({ path: path.join(out, name + '.pdf'), width: w, height: h, printBackground: true, pageRanges: '1' });
    await page.screenshot({ path: path.join(out, name + '.png'), omitBackground: true, clip: { x: 0, y: 0, width: wpx, height: hpx } });
    console.log('ok', name);
    await page.close();
  }
  await browser.close();
})();
