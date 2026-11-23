// Executa blocos de tempo da lista no portal (P4 M2.1.1 ou P7 M3.2.3), um registro por tentativa.
// Registros, gravações e mensagens de erro ficam só em dados/privado/S02/<caso>/ (fora do Git).
// Uso: CASO=V4 node coletar_portal.js --bloco B10 --modo p7 --sessao S08 --rede wifi
const path = require('path');
const fs = require('fs');
const s = require('./portal_s02');

const espera = ms => new Promise(r => setTimeout(r, ms));
const agora = () => { const d = new Date(Date.now() - 3 * 3600e3); return d.toISOString().slice(0, 19) + '-03:00'; };
const LIMITE = 60000;
const CONTAM_P7 = new Set(['concluida', 'falha', 'sessao_expirada', 'tempo_limite']);
const consultar = () => [...document.querySelectorAll('button')].find(b => b.innerText.trim() === 'Consultar' && b.getBoundingClientRect().width > 0) || null;
// Mensagens de erro do serviço, login exigido ou lista: o primeiro estado visível decide a tentativa.
const estado = () => {
  const vis = e => e && e.getBoundingClientRect().width > 0 && e.innerText.trim();
  if (document.querySelector('tr.mat-row')) return { estado: 'lista' };
  const vazio = [...document.querySelectorAll('mat-card *')].find(e => e.children.length === 0 && /Nenhuma infração/.test(e.textContent));
  if (vazio) return { estado: 'erro', texto: vazio.textContent.trim() };
  const erro = [...document.querySelectorAll('mat-dialog-container, snack-bar-container, .mat-snack-bar-container, .mat-mdc-snack-bar-container, .swal2-popup, .toast-container > *, [role=alert], [role=alertdialog]')].find(vis);
  if (erro) return { estado: 'erro', texto: erro.innerText.trim().slice(0, 300) };
  if (!document.querySelector('.header-toolbar-userMenu') && [...document.querySelectorAll('button')].some(b => /Fazer login/.test(b.innerText))) return { estado: 'login' };
  return null;
};

function args() {
  const a = process.argv.slice(2), o = { sessao: 'S06', rede: 'wifi' };
  for (let i = 0; i < a.length; i += 2) o[a[i].replace(/^--/, '')] = a[i + 1];
  if (!/^B[0-9]{2}$/.test(o.bloco || '') || !['lista', 'p7'].includes(o.modo) || !/^S[0-9]{2}$/.test(o.sessao) || !['wifi', '4g', 'degradada'].includes(o.rede))
    throw new Error('uso: --bloco Bnn --modo lista|p7 [--sessao Snn] [--rede wifi|4g|degradada]');
  return o;
}

async function tentativa(page, metrica, rep, bloco) {
  const pasta = path.join(s.PRIV, `tempo-portal-${bloco}-${metrica}-${rep}`);
  if (fs.existsSync(pasta)) throw new Error('Gravação já existe; use repetição diferente');
  let etapa = 'preparacao';
  try {
    await s.inicio(page); await s.irAoHistorico(page); await s.selecionar(page);
    etapa = 'tentativa';
    const parar = await s.gravar(page, pasta); await espera(800);
    const tClique = await s.clicar(page, consultar);
    let fim = null, tFim = null;
    while (Date.now() / 1000 < tClique + LIMITE / 1000 + 5) {  // margem; o limite é conferido no vídeo
      fim = await page.evaluate(estado).catch(() => null);
      if (fim) { tFim = Date.now() / 1000; break; }
      await espera(150);
    }
    await espera(1500);
    const q = await parar();
    const resultado = !fim ? 'tempo_limite' : fim.estado === 'lista' ? 'concluida' : fim.estado === 'login' ? 'sessao_expirada' : 'falha';
    return { metrica, repeticao: rep, data_hora: agora(), resultado, etapa, inicio_evento: 'clique em Consultar',
      fim_evento: 'primeira linha da lista visível', ...(resultado === 'concluida' ? s.proposta(q, tClique, tFim) : {}),
      quadros: q.length, diagnostico_privado: fim && fim.texto || '', gravacao: path.relative(path.resolve(__dirname, '..', '..', '..'), pasta) };
  } catch (e) {
    // Página que não carrega na preparação conta como falha do serviço; o resto é erro de instrumento.
    const servico = e.message === 'tempo_limite' || e.message === 'sessao_expirada';
    return { metrica, repeticao: rep, data_hora: agora(), etapa,
      resultado: e.message === 'sessao_expirada' ? 'sessao_expirada' : servico ? (etapa === 'preparacao' ? 'falha' : 'tempo_limite') : 'erro_instrumento',
      tipo: e.name, diagnostico_privado: e.message };
  }
}

async function main() {
  const o = args();
  if (!process.env.CASO) throw new Error('CASO obrigatório');
  const metrica = o.modo === 'p7' ? 'M3.2.3' : 'M2.1.1';
  const contam = o.modo === 'p7' ? CONTAM_P7 : new Set(['concluida']);
  const selecao = JSON.parse(fs.readFileSync(path.join(s.PRIV, 'selecao.json')));
  process.env.VEICULO_HASH = selecao.hash_placa;
  const { b, page } = await s.conectar();
  let n = 0;
  try {
    for (let rep = 1; rep <= 20 && n < 11; rep++) {
      const id = String(rep).padStart(2, '0');
      const destino = path.join(s.PRIV, `${o.bloco}-${id}.json`);
      if (fs.existsSync(destino)) { if (contam.has(JSON.parse(fs.readFileSync(destino)).resultado)) n++; continue; }
      const inicio = agora();
      const r = await tentativa(page, metrica, id, o.bloco);
      Object.assign(r, { sessao: o.sessao, rede: o.rede, bloco: o.bloco, canal: 'portal', aquecimento: n === 0, inicio_execucao: inicio });
      fs.writeFileSync(destino, JSON.stringify(r, null, 2), { mode: 0o600 });
      console.log(JSON.stringify({ bloco: o.bloco, repeticao: id, resultado: r.resultado, etapa: r.etapa, aquecimento: r.aquecimento, tempo_s: r.tempo_s }));
      if (contam.has(r.resultado)) n++;
      if (r.resultado === 'sessao_expirada' || r.resultado === 'erro_instrumento') { process.exitCode = 1; break; }
      await espera(1000);
    }
  } finally { b.disconnect(); }
  if (n < 11 && !process.exitCode) process.exitCode = 1;
}
main().catch(e => { console.error(e.name); process.exit(1); });
