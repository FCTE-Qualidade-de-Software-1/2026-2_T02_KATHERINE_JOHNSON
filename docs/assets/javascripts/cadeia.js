/*
 * Diagramas clicáveis da cadeia Fase 1 → Fase 4 (página inicial).
 *
 * O Material renderiza blocos ```mermaid com securityLevel "strict", que desliga os links dos
 * nós. Os blocos ```mermaid-cadeia (classe kj-cadeia) são renderizados aqui, com links ativos.
 * Sem JavaScript, ou se o Mermaid não carregar, o código do diagrama continua visível como texto
 * e a tabela da página de rastreabilidade é a alternativa.
 */
(function () {
  "use strict";

  var MERMAID = "https://unpkg.com/mermaid@11.4.1/dist/mermaid.min.js";
  var blocos = Array.prototype.slice.call(document.querySelectorAll("pre.kj-cadeia"));
  if (!blocos.length) return;

  var fontes = blocos.map(function (pre) { return pre.textContent; });
  var alvos = blocos.map(function (pre, i) {
    var div = document.createElement("div");
    div.className = "kj-cadeia-diagrama";
    div.setAttribute("role", "region");
    div.setAttribute("tabindex", "0");
    div.setAttribute("aria-label", "Diagrama " + (i + 1) + " da cadeia de rastreabilidade; use Tab para percorrer os nós");
    return div;
  });

  function escuro() {
    var esquema = document.body.getAttribute("data-md-color-scheme");
    return esquema === "slate";
  }

  function acessivel(div) {
    // Cada nó com link recebe nome acessível igual ao seu texto visível.
    div.querySelectorAll("a").forEach(function (a) {
      var texto = (a.textContent || "").replace(/\s+/g, " ").trim();
      if (texto) a.setAttribute("aria-label", texto);
      if (!a.hasAttribute("tabindex")) a.setAttribute("tabindex", "0");
    });
  }

  var rodada = 0;
  function renderizar() {
    var atual = ++rodada;
    window.mermaid.initialize({
      startOnLoad: false,
      securityLevel: "loose",
      theme: escuro() ? "dark" : "neutral",
      flowchart: { curve: "basis" }
    });
    blocos.forEach(function (pre, i) {
      window.mermaid.render("kj-cadeia-" + i + "-" + atual, fontes[i]).then(function (r) {
        if (atual !== rodada) return;
        alvos[i].innerHTML = r.svg;
        if (r.bindFunctions) r.bindFunctions(alvos[i]);
        acessivel(alvos[i]);
        if (pre.parentNode) {
          pre.parentNode.replaceChild(alvos[i], pre);
        }
      }).catch(function (erro) {
        // Mantém o código visível; registra o erro só no console.
        if (window.console) console.error("Diagrama da cadeia não renderizado:", erro);
      });
    });
  }

  var script = document.createElement("script");
  script.src = MERMAID;
  script.onload = function () {
    renderizar();
    // Troca de tema claro/escuro do Material sem recarregar a página.
    new MutationObserver(renderizar).observe(document.body, {
      attributes: true,
      attributeFilter: ["data-md-color-scheme"]
    });
  };
  document.head.appendChild(script);
})();
