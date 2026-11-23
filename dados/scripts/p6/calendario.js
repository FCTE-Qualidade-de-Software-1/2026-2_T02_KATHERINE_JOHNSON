// Escolhe uma data pelo calendário (mat-datepicker) do campo com o rótulo dado: ano → mês → dia.
const espera = ms => new Promise(r => setTimeout(r, ms));
// No Chrome do celular o acionamento é por toque; no computador, por clique.
// No celular, o toque sintético sai deslocado pela barra do Chrome; aciona pelo evento de clique da página.
const acionar = el => (process.env.TOQUE ? el.evaluate(e => e.click()) : el.click());
async function clicarCelula(page, texto) {
  for (let i = 0; i < 30; i++) {
    const h = await page.evaluateHandle(t => [...document.querySelectorAll('.mat-calendar-body-cell:not(.mat-calendar-body-disabled)')]
      .find(c => c.innerText.trim().toUpperCase().replace('.', '') === t) || null, texto);
    if (h.asElement()) { await acionar(h.asElement()); await espera(350); return; }
    await espera(200);
  }
  throw new Error(`calendário sem a opção ${texto}`);
}
async function escolherData(page, rotulo, ano, mes, dia) {
  const botao = await page.evaluateHandle(r => [...document.querySelectorAll('mat-form-field')].find(f => f.innerText.includes(r))?.querySelector('mat-datepicker-toggle button') || null, rotulo);
  if (!botao.asElement()) throw new Error(`sem calendário em ${rotulo}`);
  // Logo após o formulário aparecer, o primeiro clique pode não abrir o calendário: tenta até 4 vezes.
  let periodo = null;
  for (let i = 0; i < 4 && !periodo; i++) {
    await acionar(botao.asElement());
    periodo = await page.waitForSelector('.mat-calendar-period-button', { timeout: 3000 }).catch(() => null);
  }
  if (!periodo) throw new Error(`calendário de ${rotulo} não abriu`);
  await acionar(periodo); await espera(400);
  await clicarCelula(page, String(ano));
  await clicarCelula(page, mes);
  await clicarCelula(page, String(dia));
  return page.evaluate(r => [...document.querySelectorAll('mat-form-field')].find(f => f.innerText.includes(r))?.querySelector('input')?.value, rotulo);
}
module.exports = { escolherData };
if (require.main === module) (async () => {
  const { conectar } = require('./conectar');
  const { browser, page } = await conectar('chrome');
  console.log('inicio', await escolherData(page, 'Data início', 2024, 'JAN', 1));
  console.log('final', await escolherData(page, 'Data final', 2024, 'DEZ', 31));
  await browser.disconnect();
})().catch(e => { console.error(e.message); process.exit(1); });
