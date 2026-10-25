// Rend un fichier HTML en PDF A4 (Chromium headless).
// Usage : node render_pdf.js <fichier_html> <fichier_pdf>
const { chromium } = require('playwright-core');
const path = require('path');
(async () => {
  const [src, out] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(src));
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true });
  await browser.close();
  console.log('ok', out);
})();
