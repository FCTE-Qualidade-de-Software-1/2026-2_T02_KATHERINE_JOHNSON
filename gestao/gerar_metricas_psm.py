import json
import re
import subprocess
import os
import matplotlib.pyplot as plt
import numpy as np

os.makedirs('gestao', exist_ok=True)

REPO = "FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON"
cmd = [
    "gh", "issue", "list",
    "--repo", REPO,
    "--milestone", "Entrega 1 (E1) - Fases 1 e 2 GQM",
    "--state", "all",
    "--json", "number,title,assignees,body,state,stateReason"
]

print("Coletando issues da API do GitHub via gh CLI...")
try:
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    issues_data = json.loads(result.stdout)
except Exception as e:
    print(f"Erro ao executar gh CLI: {e}")
    issues_data = []

# Mapeamento dos usuários do GitHub para os nomes da equipe
LOGIN_TO_NOME = {
    "Daniellira540": "Daniel",
    "HeitorM50": "Heitor",
    "HugoFreitass": "Hugo",
    "pedruck": "Pedro Druck",
    "PedroGTG": "Pedro Henrique",
    "Phill-Chill": "Philipe"
}

# Regex robusta para capturar com ou sem asteriscos, colchetes e espaços
re_est = re.compile(r"Estimativa\s+inicial\s+de\s+horas:\*{0,2}\s*\[?\s*(\d+)\s*(?:h|horas)?\s*\]?", re.IGNORECASE)
re_real = re.compile(r"Horas\s+reais\s+executadas:\*{0,2}\s*\[?\s*(\d+)\s*(?:h|horas)?\s*\]?", re.IGNORECASE)

membros_esforco = {nome: {"est": 0, "real": 0, "issues": 0} for nome in LOGIN_TO_NOME.values()}

for issue in issues_data:
    num = issue.get("number")
    body = issue.get("body", "") or ""
    assignees = [a["login"] for a in issue.get("assignees", [])]
    
    # Issues fechadas como duplicadas não entram na medição (ex.: #27, incorporada à #2)
    if issue.get("stateReason") == "DUPLICATE":
        continue

    # Issues com mais de um responsável têm as horas divididas igualmente entre eles
    nomes = [LOGIN_TO_NOME[a] for a in assignees if a in LOGIN_TO_NOME] or (["Daniel"] if num == 2 else ["Outros"])
    for nome in nomes:
        membros_esforco.setdefault(nome, {"est": 0, "real": 0, "issues": 0})

    m_est = re_est.search(body)
    m_real = re_real.search(body)

    # Captura os valores ou assume 5h se for a issue agregadora #2 ainda em preenchimento
    h_est = int(m_est.group(1)) if m_est else (5 if num == 2 else 0)
    h_real = int(m_real.group(1)) if m_real else (5 if num == 2 else 0)

    for nome in nomes:
        membros_esforco[nome]["est"] += h_est / len(nomes)
        membros_esforco[nome]["real"] += h_real / len(nomes)
        membros_esforco[nome]["issues"] += 1

print("\n--- DADOS EXTRAÍDOS COM SUCESSO ---")
for membro, dados in membros_esforco.items():
    print(f"{membro:15}: Estimado = {dados['est']:.2f}h | Real = {dados['real']:.2f}h | Issues = {dados['issues']}")

# 1. Gráfico PSM/CID: Recursos e Custos (Horas Estimadas vs. Reais)
membros = list(membros_esforco.keys())
h_est = [membros_esforco[m]["est"] for m in membros]
h_real = [membros_esforco[m]["real"] for m in membros]

x = np.arange(len(membros))
width = 0.35

plt.figure(figsize=(10, 5))
plt.bar(x - width/2, h_est, width, label='Horas Estimadas', color='#3498db')
plt.bar(x + width/2, h_real, width, label='Horas Reais Executadas', color='#2ecc71')

plt.xlabel('Integrantes da Equipe', fontweight='bold')
plt.ylabel('Horas', fontweight='bold')
plt.title('PSM/CID - Recursos e Custos: Esforço Planejado vs. Realizado (Release E1)', pad=15)
plt.xticks(x, membros, rotation=15)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('gestao/recursos_custos_e1.png', dpi=300)
plt.close()
print("-> Gráfico gerado: gestao/recursos_custos_e1.png")

# 2. Gráfico PSM/CID: Calendário e Progresso (Issues por Membro)
qtd_issues = [membros_esforco[m]["issues"] for m in membros]

plt.figure(figsize=(10, 5))
bars = plt.bar(membros, qtd_issues, color='#9b59b6', width=0.5)
plt.xlabel('Integrantes da Equipe', fontweight='bold')
plt.ylabel('Quantidade de Issues', fontweight='bold')
plt.title('PSM/CID - Calendário e Progresso: Distribuição de Issues (Release E1)', pad=15)
plt.xticks(rotation=15)
plt.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, int(yval), ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('gestao/progresso_issues_e1.png', dpi=300)
plt.close()
print("-> Gráfico gerado: gestao/progresso_issues_e1.png")