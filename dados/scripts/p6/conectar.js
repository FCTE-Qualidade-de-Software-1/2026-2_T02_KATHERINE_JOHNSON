// Conecta ao Chrome (CDP, 9222) ou ao Firefox (BiDi, 9223) já abertos pelo usuário.
const puppeteer = require('puppeteer-core');
async function conectar(nav) {
  const browser = nav === 'android'
    ? await puppeteer.connect({ browserURL: 'http://127.0.0.1:9224', defaultViewport: null })  // adb forward do Chrome do celular
    : nav === 'chrome'
    ? await puppeteer.connect({ browserURL: 'http://127.0.0.1:9222', defaultViewport: null })
    : await puppeteer.connect({ browserWSEndpoint: 'ws://127.0.0.1:9223/session', protocol: 'webDriverBiDi', defaultViewport: null });
  const pages = await browser.pages();
  const page = pages.find(p => p.url().includes('portal.detran.df.gov.br')) || pages.find(p => p.url().includes('detran')) || pages[0];
  return { browser, page };
}
module.exports = { conectar };
if (require.main === module) (async () => {
  for (const nav of ['chrome', 'firefox']) {
    const { browser, page } = await conectar(nav);
    console.log(nav, await browser.version(), page.url(), await page.title());
    await browser.disconnect();
  }
})().catch(e => { console.error(e.message); process.exit(1); });
