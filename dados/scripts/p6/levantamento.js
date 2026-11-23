// Levantamento da massa de dados: consulta o histórico em janelas de 1 ano nos últimos 5 anos e conta
// as infrações por janela (quantidade, ano/mês da infração e situação), sem guardar auto, placa ou valores.
const { conectar } = require('./conectar');
const { escolherData } = require('./calendario');
const espera = ms => new Promise(r => setTimeout(r, ms));
const MESES = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'];
const botao = (page, t) => page.evaluateHandle(t => [...document.querySelectorAll('button')].find(b => b.innerText.trim() === t && b.getBoundingClientRect().width > 0) || null, t);
async function irAoFiltro(page) {
  for (let i = 0; i < 40; i++) {
    if (await page.evaluate(() => [...document.querySelectorAll('mat-form-field')].some(f => f.innerText.includes('Data início')))) return;
    const sel = await botao(page, 'Selecionar');
    if (sel.asElement()) { await sel.asElement().click(); await espera(1500); continue; }
    if (i === 0 || i === 20) await page.goto('https://portal.detran.df.gov.br/#/servicos/detran-digital/infracoes/consulta/historico-infracao-veiculo');
    await espera(500);
  }
  throw new Error('filtro não apareceu');
}
(async () => {
  const { browser, page } = await conectar('chrome');
  let ultima = null;
  page.on('response', async r => { if (r.url().includes('/veiculo/lista-infracao/') && r.request().method() === 'POST') { try { ultima = { status: r.status(), n: (await r.json()).length }; } catch (e) { ultima = { status: r.status(), n: 'nao-json' }; } } });
  const janelas = [[2025, 11, 22, 2026, 11, 21], [2024, 11, 22, 2025, 11, 21], [2023, 11, 22, 2024, 11, 21], [2022, 11, 22, 2023, 11, 21], [2021, 11, 22, 2022, 11, 21]];
  for (const [a1, m1, d1, a2, m2, d2] of janelas) {
    try {
      await irAoFiltro(page);
      const fim = await escolherData(page, 'Data final', a2, MESES[m2 - 1], d2);
      const ini = await escolherData(page, 'Data início', a1, MESES[m1 - 1], d1);
      ultima = null;
      await (await botao(page, 'Consultar')).asElement().click();
      for (let i = 0; i < 60 && !ultima; i++) await espera(500);
      await espera(1500);
      const linhas = await page.evaluate(() => [...document.querySelectorAll('tr.mat-row')].map(tr => {
        const c = [...tr.cells].map(x => x.innerText.trim());
        return { data: (c[3] || '').replace(/^\d{2}\//, ''), status: c[2], situacao: (c[4] || '').replace(/\s+/g, ' ') };
      }));
      const paginacao = await page.evaluate(() => document.querySelector('.mat-paginator-range-label')?.textContent.trim() || '');
      console.log(JSON.stringify({ periodo: `${ini} a ${fim}`, api: ultima, linhas: linhas.length, paginacao, infracoes: linhas }));
      const v = await botao(page, 'Voltar'); if (v.asElement()) { await v.asElement().click(); await espera(1500); }
    } catch (e) { console.log(JSON.stringify({ janela: `${d1}/${m1}/${a1}`, erro: e.message })); }
  }
  console.log('logado_ao_fim', await page.evaluate(() => !!document.querySelector('.header-toolbar-userMenu')));
  await browser.disconnect();
})().catch(e => { console.error(e.message); process.exit(1); });
