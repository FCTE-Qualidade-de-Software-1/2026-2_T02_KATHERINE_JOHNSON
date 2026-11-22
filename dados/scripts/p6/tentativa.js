// Uma tentativa da P6: tela inicial autenticada → Infração → Histórico de infrações por veículo →
// (fecha o aviso "É GOLPE!" se aparecer) → Selecionar → período 01/01/2024–31/12/2024 → Consultar → seta da infração escolhida → detalhe.
// Antes da captura, todo texto que não é rótulo vira tarja preta na própria página.
// Uso: node tentativa.js <chrome|firefox|android> <repeticao> <data-da-infracao-V1-I1> <bloco>
// Opcional (S05, V2): PERIODO_PADRAO=1 usa o período que o filtro abre (últimos 12 meses), sem calendário;
// VEICULO_HASH=<sha256 da placa> escolhe o veículo da lista sem gravar a placa; VEIC=<código> entra no nome da captura.
const { conectar } = require('./conectar');
const { escolherData } = require('./calendario');
const espera = ms => new Promise(r => setTimeout(r, ms));
const LIMITE = 60000;
// No celular, o toque sintético sai deslocado pela barra do Chrome; aciona pelo evento de clique da página.
const acionar = el => (process.env.TOQUE ? el.evaluate(e => e.click()) : el.click());
const ROTULOS = new Set(('Histórico de Infrações por Veículo|Detalhes da infração|Notificação de Penalidade|Registro de pagamento|' +
  'Dados do Veículo|Placa|Marca/Modelo|Infração|Código Renainf|Auto Infração|Regulamento|Responsável pela Infração|Órgão Autuador|' +
  'Natureza|Pontuação Infração/Status|Data Infração|Hora Infração|Data da Notif. de Autuação|Data da Notif. de Penalidade|' +
  'Data da Defesa Prévia|Identificação do Condutor Infrator|Data de Vencimento|Descrição da Infração|Local da Infração|Valor da Multa|' +
  'Valor Correção|Valor Desconto|Valor Devido|Velocidade Permitida|Velocidade Aferida|Situação Pagamento|Situação Multa|Voltar|' +
  'done|info|Categorias|Veículos|Habilitação|Agendamento').split('|'));

async function aguardar(page, fn, arg) {
  const fim = Date.now() + LIMITE;
  while (Date.now() < fim) {
    const h = await page.evaluateHandle(fn, arg).catch(() => null);
    if (h && h.asElement && h.asElement()) return h.asElement();
    await espera(300);
  }
  throw new Error('tempo_limite');
}
// Clica no elemento devolvido por fn; se o Angular trocar o nó no meio do clique, busca de novo.
async function clicar(page, fn, arg) {
  const fim = Date.now() + LIMITE;
  while (true) {
    const el = await aguardar(page, fn, arg);
    // Centraliza o alvo e confere que nada (ex.: ícone do assistente virtual) está por cima dele.
    const livre = await el.evaluate(e => {
      e.scrollIntoView({ block: 'center' });
      const r = e.getBoundingClientRect(), topo = document.elementFromPoint(r.x + r.width / 2, r.y + r.height / 2);
      return !!topo && (e === topo || e.contains(topo) || topo.contains(e));
    }).catch(() => false);
    if (!livre && !process.env.TOQUE) {  // no celular o acionamento é pelo evento da página, sem coordenadas
      if (Date.now() > fim) throw new Error('alvo coberto por outro elemento');
      await espera(500); continue;
    }
    // Só toca quando o alvo parou (menus e listas animam ao abrir).
    const r1 = await el.evaluate(e => JSON.stringify(e.getBoundingClientRect())).catch(() => '');
    await espera(400);
    const r2 = await el.evaluate(e => JSON.stringify(e.getBoundingClientRect())).catch(() => '-');
    if (r1 !== r2) continue;
    try { await acionar(el); return el; } catch (e) {
      if (!/detached|not clickable|not an Element/i.test(e.message) || Date.now() > fim) throw e;
      await espera(300);
    }
  }
}

(async () => {
  const [nav, repeticao, dataInfracao, bloco] = process.argv.slice(2);
  const { browser, page } = await conectar(nav);
  const inicio = new Date();
  const passos = [];
  let resultado = 'concluida', motivo = '';
  try {
    await page.goto('https://portal.detran.df.gov.br/#/home');
    await aguardar(page, () => document.querySelector('.header-toolbar-userMenu'));
    await espera(1500);
    passos.push('inicio_autenticado');
    // Se o chat do assistente virtual estiver aberto, ele cobre a página: fecha pela seta do topo.
    const chat = await page.evaluateHandle(() => { const c = document.querySelector('#bot_close_chevron_down'); return c && c.getBoundingClientRect().width > 0 && document.querySelector('#bot_widget_head')?.getBoundingClientRect().height > 0 ? c : null; });
    if (chat.asElement()) { await acionar(chat.asElement()); passos.push('fechar_chat_assistente'); await espera(1000); }
    // A tela inicial pode abrir o aviso "É GOLPE!", que cobre o menu até ser fechado.
    for (let i = 0; i < 10; i++) {
      const aviso = await page.evaluateHandle(() => [...document.querySelectorAll('button.alerta-fraude-botao')].find(b => b.getBoundingClientRect().width > 0) || null);
      if (aviso.asElement()) { await acionar(aviso.asElement()); passos.push('fechar_aviso_golpe'); await espera(800); break; }
      await espera(400);
    }
    if (nav === 'android') {  // layout móvel: o menu fica atrás do botão "menu"
      const aberto = await page.evaluate(() => [...document.querySelectorAll('button')].some(b => b.innerText.trim() === 'close' && b.getBoundingClientRect().width > 0));
      if (!aberto) {
        await clicar(page, () => [...document.querySelectorAll('button')].find(b => b.innerText.trim() === 'menu' && b.getBoundingClientRect().width > 0) || null);
        await espera(800);
      }
      await clicar(page, () => [...document.querySelectorAll('button')].find(b => b.innerText.trim().startsWith('Infração') && b.getBoundingClientRect().width > 0) || null);
    } else {
      await clicar(page, () => [...document.querySelectorAll('button.mat-menu-trigger')].find(b => b.innerText.trim().startsWith('Infração')) || null);
    }
    // O <a> do menu tem largura 0 no computador; o alvo visível é o título dentro dele.
    await espera(800);
    await clicar(page, () => [...document.querySelectorAll('.menu-item-title')].find(t => t.textContent.trim() === 'Histórico de infrações por veículo' && t.getBoundingClientRect().width > 0) || null);
    passos.push('menu_historico_veiculo');
    if (nav === 'android') {  // no celular o menu continua aberto por cima da página depois da navegação
      await espera(1500);
      const fechar = await page.evaluateHandle(() => [...document.querySelectorAll('button')].find(b => b.innerText.trim() === 'close' && b.getBoundingClientRect().width > 0) || null);
      if (fechar.asElement()) { await acionar(fechar.asElement()); passos.push('fechar_menu'); await espera(800); }
    }
    let indice = 0;
    if (process.env.VEICULO_HASH) {  // localiza o veículo pelo hash da placa; a placa não sai da página
      await aguardar(page, () => [...document.querySelectorAll('button')].find(b => b.innerText.trim() === 'Selecionar' && b.getBoundingClientRect().width > 0) || null);
      indice = await page.evaluate(async h => {
        const bs = [...document.querySelectorAll('button')].filter(b => b.innerText.trim() === 'Selecionar');
        const sha = async t => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))].map(x => x.toString(16).padStart(2, '0')).join('');
        for (let i = 0; i < bs.length; i++) for (const t of (bs[i].closest('tr, mat-card, div').innerText.match(/[A-Z]{3}[0-9][A-Z0-9][0-9]{2}/g) || [])) if (await sha(t) === h) return i;
        return -1;
      }, process.env.VEICULO_HASH);
      if (indice < 0) throw new Error('veículo não encontrado na lista');
    }
    await clicar(page, i => [...document.querySelectorAll('button')].filter(b => b.innerText.trim() === 'Selecionar' && b.getBoundingClientRect().width > 0)[i] || null, indice);
    passos.push('selecionar_veiculo');
    // As datas são somente leitura: o período é escolhido pelo calendário.
    await aguardar(page, () => [...document.querySelectorAll('mat-form-field')].find(f => f.innerText.includes('Data início')) || null);
    if (process.env.PERIODO_PADRAO) {
      passos.push('periodo_padrao');
    } else {
      const ini = await escolherData(page, 'Data início', 2024, 'JAN', 1);
      const fim = await escolherData(page, 'Data final', 2024, 'DEZ', 31);
      passos.push(`periodo ${ini}-${fim}`);
    }
    await clicar(page, () => [...document.querySelectorAll('button')].find(b => b.innerText.trim() === 'Consultar' && b.getBoundingClientRect().width > 0) || null);
    passos.push('consultar');
    const seta = await aguardar(page, d => {
      if ([...document.querySelectorAll('mat-card *')].some(e => e.children.length === 0 && /Nenhuma infração/.test(e.textContent))) return document.body;
      const tr = [...document.querySelectorAll('tr.mat-row')].find(t => [...t.cells].some(c => c.innerText.trim() === d));
      return tr ? tr.querySelector('mat-icon.icone-seta') : null;
    }, dataInfracao);
    if (await page.evaluate(e => e === document.body, seta)) throw new Error('lista sem a infração escolhida');
    await clicar(page, d => { const tr = [...document.querySelectorAll('tr.mat-row')].find(t => [...t.cells].some(c => c.innerText.trim() === d)); return tr ? tr.querySelector('mat-icon.icone-seta') : null; }, dataInfracao);
    passos.push('abrir_detalhe');
    await aguardar(page, () => [...document.querySelectorAll('mat-card *')].find(e => e.children.length === 0 && e.textContent.trim() === 'Descrição da Infração') || null);
    await espera(1500);
    passos.push('detalhe_exibido');
  } catch (e) {
    const deslogado = await page.evaluate(() => !document.querySelector('.header-toolbar-userMenu') && [...document.querySelectorAll('button')].some(b => /Fazer login/.test(b.innerText))).catch(() => false);
    resultado = deslogado ? 'sessao_expirada' : e.message === 'tempo_limite' ? 'tempo_limite' : 'falha';
    motivo = `${e.message} após ${passos[passos.length - 1] || 'início'}`;
  }
  // Tarja: cabeçalho do usuário, campos de formulário e todo texto do conteúdo que não é rótulo conhecido.
  const tarjados = await page.evaluate(rotulos => {
    const ok = new Set(rotulos); let n = 0;
    const tarjar = e => { e.style.setProperty('background', '#000', 'important'); e.style.setProperty('color', '#000', 'important'); e.style.setProperty('text-shadow', 'none', 'important'); n++; };
    document.querySelectorAll('.header-toolbar-userMenu, input').forEach(tarjar);
    document.querySelectorAll('mat-card *').forEach(e => {
      if ([...e.childNodes].some(c => c.nodeType === 3 && c.textContent.trim()) && !ok.has(e.textContent.trim())) tarjar(e);
    });
    return n;
  }, [...ROTULOS]);

  const pad = n => String(n).padStart(2, '0');
  const local = new Date(inicio.getTime() - 3 * 3600e3);
  const dataHora = `${local.getUTCFullYear()}-${pad(local.getUTCMonth() + 1)}-${pad(local.getUTCDate())}T${pad(local.getUTCHours())}:${pad(local.getUTCMinutes())}:${pad(local.getUTCSeconds())}-03:00`;
  const nome = `${process.env.SESSAO || 'S03'}-${bloco}-portal-P6-${process.env.VEIC || 'V1'}-${repeticao}-${dataHora.slice(0, 10)}.png`;
  await page.screenshot({ path: `${process.env.CAPTURAS || 'capturas'}/${nome}`, fullPage: true });
  console.log(JSON.stringify({ nav, repeticao: Number(repeticao), resultado, motivo, data_hora: dataHora, duracao_s: ((Date.now() - inicio) / 1000).toFixed(1), passos, tarjados, captura: nome }));
  await browser.disconnect();
})().catch(e => { console.error(e.message); process.exit(1); });
