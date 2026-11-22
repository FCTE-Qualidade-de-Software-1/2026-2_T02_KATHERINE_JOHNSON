// S02 no portal (CT01, Chrome do D01): apoio a P1/P2 (campos), P3 (fluxo), P4 (tempo) e P5 (volume).
// Valores pessoais, gravações e listas de requisições vão só para dados/privado/S02/ (fora do Git);
// a saída padrão traz apenas presença, contagens, tempos e bytes.
//
// Uso (Chrome aberto com --remote-debugging-port=9222 e titular logado):
//   VEICULO_HASH=<sha256 da placa> node portal_s02.js campos <data-da-infracao>
//   VEICULO_HASH=... node portal_s02.js fluxo <repeticao>
//   VEICULO_HASH=... node portal_s02.js tempo M2.1.1|M2.1.2 <repeticao> <data-da-infracao>
//   VEICULO_HASH=... node portal_s02.js volume <repeticao>
// Opcional: CAPTURAS=<pasta> para as capturas tarjadas de P1 (padrão: dados/privado/S02).
const path = require('path');
const fs = require('fs');
const puppeteer = require(path.join(__dirname, '..', 'p6', 'node_modules', 'puppeteer-core'));

const RAIZ = path.resolve(__dirname, '..', '..', '..');
const PRIV = path.join(RAIZ, 'dados', 'privado', 'S02');
fs.mkdirSync(PRIV, { recursive: true });
const espera = ms => new Promise(r => setTimeout(r, ms));
const LIMITE = 60000;
const HOME = 'https://portal.detran.df.gov.br/#/home';
const agora = () => { const d = new Date(Date.now() - 3 * 3600e3); return d.toISOString().slice(0, 19) + '-03:00'; };

// Círculo vermelho no ponto de cada clique, para a gravação indicar o clique (P3/P4).
const MARCA = () => { if (window.__marca) return; window.__marca = 1; document.addEventListener('click', e => {
  const d = document.createElement('div');
  d.style.cssText = 'position:fixed;z-index:2147483647;pointer-events:none;width:36px;height:36px;border-radius:50%;' +
    'border:4px solid red;background:rgba(255,0,0,.25);left:' + (e.clientX - 18) + 'px;top:' + (e.clientY - 18) + 'px';
  document.body.appendChild(d); setTimeout(() => d.remove(), 700); }, true); };

async function aguardar(page, fn, arg) {
  const fim = Date.now() + LIMITE;
  while (Date.now() < fim) {
    const h = await page.evaluateHandle(fn, arg).catch(() => null);
    if (h && h.asElement && h.asElement()) return h.asElement();
    await espera(200);
  }
  throw new Error('tempo_limite');
}
async function clicar(page, fn, arg, rotulos, rotulo) {
  const el = await aguardar(page, fn, arg);
  await el.evaluate(e => e.scrollIntoView({ block: 'center' }));
  await espera(400);
  await el.click();
  if (rotulos) rotulos.push(rotulo);
  return Date.now() / 1000;
}
const botao = t => [...document.querySelectorAll('button')].find(b => b.innerText.trim() === t && b.getBoundingClientRect().width > 0) || null;

async function conectar() {
  const b = await puppeteer.connect({ browserURL: 'http://127.0.0.1:9222', defaultViewport: null });
  const page = (await b.pages()).find(x => x.url().includes('portal.detran.df.gov.br'));
  if (!page) throw new Error('aba do portal não encontrada');
  await page.evaluateOnNewDocument(MARCA);
  return { b, page };
}
async function logado(page) {
  return page.evaluate(() => !!document.querySelector('.header-toolbar-userMenu'));
}
async function inicio(page) {
  await page.goto(HOME);
  await aguardar(page, () => document.querySelector('.header-toolbar-userMenu') ||
    [...document.querySelectorAll('button')].find(b => /Fazer login/.test(b.innerText)) || null);
  if (!(await logado(page))) throw new Error('sessao_expirada');
  await page.evaluate(MARCA);
  await espera(1200);
  for (let i = 0; i < 8; i++) {  // aviso "É GOLPE!"
    const a = await page.evaluateHandle(() => [...document.querySelectorAll('button.alerta-fraude-botao')].find(b => b.getBoundingClientRect().width > 0) || null);
    if (a.asElement()) { await a.asElement().click(); await espera(600); break; }
    await espera(300);
  }
}
async function irAoHistorico(page, rotulos) {
  await clicar(page, () => [...document.querySelectorAll('button.mat-menu-trigger')].find(b => b.innerText.trim().startsWith('Infração')) || null, null, rotulos, 'Infração');
  await espera(600);
  await clicar(page, () => [...document.querySelectorAll('.menu-item-title')].find(t => t.textContent.trim() === 'Histórico de infrações por veículo' && t.getBoundingClientRect().width > 0) || null, null, rotulos, 'Histórico de infrações por veículo');
  await aguardar(page, () => [...document.querySelectorAll('button')].find(b => b.innerText.trim() === 'Selecionar') || null);
  await espera(800);
}
async function indiceVeiculo(page) {
  const h = process.env.VEICULO_HASH;
  if (!h) return 0;
  const i = await page.evaluate(async h => {
    const bs = [...document.querySelectorAll('button')].filter(b => b.innerText.trim() === 'Selecionar');
    const sha = async t => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))].map(x => x.toString(16).padStart(2, '0')).join('');
    for (let i = 0; i < bs.length; i++) for (const t of (bs[i].closest('tr, mat-card, div').innerText.match(/[A-Z]{3}[0-9][A-Z0-9][0-9]{2}/g) || [])) if (await sha(t) === h) return i;
    return -1;
  }, h);
  if (i < 0) throw new Error('veículo não encontrado na lista');
  return i;
}
async function selecionar(page, rotulos) {
  const i = await indiceVeiculo(page);
  const t = await clicar(page, i => [...document.querySelectorAll('button')].filter(b => b.innerText.trim() === 'Selecionar' && b.getBoundingClientRect().width > 0)[i] || null, i, rotulos, 'Selecionar');
  await aguardar(page, () => [...document.querySelectorAll('mat-form-field')].find(f => f.innerText.includes('Data início')) || null);
  await espera(600);
  return t;
}
const listaVisivel = () => document.querySelector('tr.mat-row') ||
  [...document.querySelectorAll('mat-card *')].find(e => e.children.length === 0 && /Nenhuma infração/.test(e.textContent)) || null;
const detalheVisivel = () => [...document.querySelectorAll('mat-form-field')].find(f => /Descrição da Infração/.test(f.innerText) && (f.querySelector('input,textarea') || {}).value) || null;
const seta = d => { const tr = [...document.querySelectorAll('tr.mat-row')].find(t => [...t.cells].some(c => c.innerText.trim() === d)); return tr ? tr.querySelector('mat-icon.icone-seta') : null; };

async function tarjarECapturar(page, arquivo) {
  await page.evaluate(() => {
    const t = e => { e.style.setProperty('background', '#000', 'important'); e.style.setProperty('color', '#000', 'important'); };
    document.querySelectorAll('.header-toolbar-userMenu, .header-toolbar-userMenu *, input, textarea, td.mat-cell').forEach(t);
    document.querySelectorAll('.header-toolbar-userMenu img').forEach(i => i.style.setProperty('visibility', 'hidden', 'important'));  // foto do perfil
    document.querySelectorAll('mat-card *').forEach(e => {
      const proprio = [...e.childNodes].some(c => c.nodeType === 3 && c.textContent.trim());
      if (proprio && !e.closest('mat-label, label, th, button, .mat-step-label')) t(e);
    });
  });
  await page.screenshot({ path: arquivo, fullPage: true });
}

// Gravação: screencast do Chrome, um JPEG com horário a cada mudança da tela (taxa variável).
async function gravar(page, pasta) {
  fs.rmSync(pasta, { recursive: true, force: true }); fs.mkdirSync(pasta, { recursive: true });
  const cdp = await page.createCDPSession(); const quadros = [];
  cdp.on('Page.screencastFrame', f => {
    fs.writeFileSync(path.join(pasta, String(quadros.length).padStart(5, '0') + '.jpg'), Buffer.from(f.data, 'base64'));
    quadros.push(f.metadata.timestamp); cdp.send('Page.screencastFrameAck', { sessionId: f.sessionId }).catch(() => {});
  });
  await cdp.send('Page.startScreencast', { format: 'jpeg', quality: 70, everyNthFrame: 1 });
  return async () => { await cdp.send('Page.stopScreencast'); await espera(300);
    fs.writeFileSync(path.join(pasta, 'timestamps.json'), JSON.stringify(quadros)); return quadros; };
}
// Proposta de primeira leitura: primeiro quadro depois do clique e primeiro quadro depois do fim visual.
function proposta(quadros, tClique, tFim) {
  const ini = quadros.findIndex(t => t >= tClique), fim = quadros.findIndex(t => t >= tFim);
  return { quadro_inicial: ini, quadro_final: fim, inicio_s: ini >= 0 ? +(quadros[ini] - quadros[0]).toFixed(3) : null,
    fim_s: fim >= 0 ? +(quadros[fim] - quadros[0]).toFixed(3) : null,
    tempo_s: ini >= 0 && fim >= 0 ? +(quadros[fim] - quadros[ini]).toFixed(3) : null };
}

async function campos(page, data) {
  const cap = process.env.CAPTURAS || PRIV;
  await inicio(page); await irAoHistorico(page); await selecionar(page);
  await clicar(page, () => [...document.querySelectorAll('button')].find(b => b.innerText.trim() === 'Consultar' && b.getBoundingClientRect().width > 0) || null);
  await aguardar(page, listaVisivel); await espera(1500);
  const hLista = agora();
  const lista = await page.evaluate(d => {
    const th = [...document.querySelectorAll('th')].map(t => t.innerText.trim());
    const tr = [...document.querySelectorAll('tr.mat-row')].find(t => [...t.cells].some(c => c.innerText.trim() === d));
    return tr ? [...tr.cells].map((c, i) => [th[i] || '', c.innerText.trim()]) : null;
  }, data);
  if (!lista) throw new Error('infração de referência não está na lista');
  await tarjarECapturar(page, path.join(cap, 'S02-portal-lista-infracoes-V2.png'));
  await clicar(page, seta, data);
  await aguardar(page, detalheVisivel); await espera(1500);
  const hDetalhe = agora();
  const detalhe = await page.evaluate(() => [...document.querySelectorAll('mat-form-field')].map(f => {
    const r = f.querySelector('mat-label, label'); const v = f.querySelector('input, textarea');
    return [r ? r.innerText.replace(/\*/g, '').trim() : '', v ? v.value.trim() : ''];
  }).filter(p => p[0]));
  await tarjarECapturar(page, path.join(cap, 'S02-portal-detalhe-V2-I1.png'));
  fs.writeFileSync(path.join(PRIV, 'portal-campos.json'), JSON.stringify({ data_hora_lista: hLista, data_hora_detalhe: hDetalhe, lista, detalhe }, null, 1));
  return { data_hora_lista: hLista, data_hora_detalhe: hDetalhe, rotulos_lista: lista.map(p => p[0]), rotulos_detalhe: detalhe.map(p => p[0]), privado: 'dados/privado/S02/portal-campos.json' };
}

async function fluxo(page, rep) {
  const rotulos = [], rotas = [];
  await inicio(page);
  const parar = await gravar(page, path.join(PRIV, `fluxo-portal-${rep}`));
  let u = page.url(); const t0 = Date.now() / 1000;
  const obs = setInterval(() => { if (page.url() !== u) { u = page.url(); rotas.push(+(Date.now() / 1000 - t0).toFixed(2)); } }, 100);
  await espera(800);
  await irAoHistorico(page, rotulos); await selecionar(page, rotulos);
  await clicar(page, () => [...document.querySelectorAll('button')].find(b => b.innerText.trim() === 'Consultar' && b.getBoundingClientRect().width > 0) || null, null, rotulos, 'Consultar');
  await aguardar(page, listaVisivel); await espera(1500);
  clearInterval(obs); await parar();
  return { repeticao: rep, data_hora: agora(), passos: rotulos.length, sequencia: rotulos.join(' > '), rolagens_manuais: 0,
    mudancas_de_rota_s: rotas, gravacao: `dados/privado/S02/fluxo-portal-${rep}`,
    observacao: 'transições: contar na gravação (troca do conteúdo principal); a mudança de rota é só apoio' };
}

async function tempo(page, metrica, rep, data) {
  await inicio(page); await irAoHistorico(page); await selecionar(page);
  const consultar = () => [...document.querySelectorAll('button')].find(b => b.innerText.trim() === 'Consultar' && b.getBoundingClientRect().width > 0) || null;
  let tClique, tFim;
  const pasta = path.join(PRIV, `tempo-portal-${metrica}-${rep}`);
  if (metrica === 'M2.1.1') {
    const parar = await gravar(page, pasta); await espera(800);
    tClique = await clicar(page, consultar);
    await aguardar(page, listaVisivel); tFim = Date.now() / 1000; await espera(1500);
    const q = await parar();
    return { metrica, repeticao: rep, data_hora: agora(), inicio_evento: 'clique em Consultar', fim_evento: 'primeira linha da lista visível', ...proposta(q, tClique, tFim), quadros: q.length, gravacao: path.relative(RAIZ, pasta) };
  }
  await clicar(page, consultar); await aguardar(page, listaVisivel); await espera(1500);
  const parar = await gravar(page, pasta); await espera(800);
  tClique = await clicar(page, seta, data);
  await aguardar(page, detalheVisivel); tFim = Date.now() / 1000; await espera(1500);
  const q = await parar();
  return { metrica, repeticao: rep, data_hora: agora(), inicio_evento: 'clique na seta da infração', fim_evento: '"Descrição da Infração" preenchida', ...proposta(q, tClique, tFim), quadros: q.length, gravacao: path.relative(RAIZ, pasta) };
}

async function volume(page, rep) {
  await inicio(page);
  const cdp = await page.createCDPSession(); await cdp.send('Network.enable');
  let bytes = 0, n = 0, medir = false; const reqs = {};
  cdp.on('Network.responseReceived', e => { if (medir) reqs[e.requestId] = { url: e.response.url, status: e.response.status }; });
  cdp.on('Network.loadingFinished', e => { if (medir) { bytes += e.encodedDataLength; n++; if (reqs[e.requestId]) reqs[e.requestId].bytes = e.encodedDataLength; } });
  medir = true;
  await irAoHistorico(page); await selecionar(page);
  await clicar(page, () => [...document.querySelectorAll('button')].find(b => b.innerText.trim() === 'Consultar' && b.getBoundingClientRect().width > 0) || null);
  await aguardar(page, listaVisivel); await espera(2500); medir = false;
  fs.writeFileSync(path.join(PRIV, `volume-portal-${rep}.json`), JSON.stringify(Object.values(reqs), null, 1));
  return { repeticao: rep, data_hora: agora(), instrumento: 'CDP Network (encodedDataLength), Chrome', bytes_transferidos: bytes, requisicoes: n,
    escopo: 'da abertura do menu Infração até a lista completa (mesmo intervalo do P3)', privado: `dados/privado/S02/volume-portal-${rep}.json` };
}

(async () => {
  const [modo, a, b2, c] = process.argv.slice(2);
  const { b, page } = await conectar();
  let r;
  try {
    if (modo === 'campos') r = await campos(page, a);
    else if (modo === 'fluxo') r = await fluxo(page, a);
    else if (modo === 'tempo') r = await tempo(page, a, b2, c);
    else if (modo === 'volume') r = await volume(page, a);
    else throw new Error('modo: campos | fluxo | tempo | volume');
    r.resultado = 'concluida';
  } catch (e) {
    const exp = e.message === 'sessao_expirada' || !(await logado(page).catch(() => false));
    r = { modo, resultado: exp ? 'sessao_expirada' : e.message === 'tempo_limite' ? 'tempo_limite' : 'falha', motivo: e.message, data_hora: agora() };
  }
  console.log(JSON.stringify(r));
  b.disconnect();
})().catch(e => { console.error(e.message); process.exit(1); });
