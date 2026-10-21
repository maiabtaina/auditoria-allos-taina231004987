#!/usr/bin/env python3
"""04_gerar_dossie_pdf.py | Monta o dossiê PDF | ALLOS S.A. 2025 | matrícula 231004987 | 20/10/2026"""
import os, json, csv
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from conteudo_pts_b import PTS, ANEXOS, EXC
from versoes_normas import VERS
import re
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "..", "dossie", "Dossie_Auditoria_ALLOS_2025_matricula_231004987.pdf")
res = json.load(open(os.path.join(BASE, "..", "dados", "resultados", "resultados.json")))
MAT, DATA = "231004987", "20/10/2026"
def S(t):
    for a, b in {"≤": "<=", "≥": ">=", "→": "->", "×": "x", "≈": "~", "−": "-", "Δ": "delta ", "\u00a0": " "}.items(): t = t.replace(a, b)
    return t.replace("&", "&amp;").replace("<=", "&lt;=").replace(">=", "&gt;=").replace(" < ", " &lt; ").replace(" > ", " &gt; ").replace("(<", "(&lt;").replace(" >", " &gt;")
ST = dict(
 h1=ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=colors.HexColor("#1F3864"), spaceAfter=6),
 h2=ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=colors.HexColor("#1F3864"), spaceBefore=8, spaceAfter=3),
 b=ParagraphStyle("b", fontName="Helvetica", fontSize=8.6, leading=11.2, spaceAfter=3),
 lab=ParagraphStyle("lab", fontName="Helvetica-Bold", fontSize=8.2, leading=10, textColor=colors.white, backColor=colors.HexColor("#1F3864"), borderPadding=(2, 3, 2, 3), spaceBefore=6, spaceAfter=4),
 sm=ParagraphStyle("sm", fontName="Helvetica", fontSize=7.4, leading=9.2, textColor=colors.HexColor("#444444")),
 warn=ParagraphStyle("warn", fontName="Helvetica-Bold", fontSize=8.6, leading=11, textColor=colors.HexColor("#8B0000"), backColor=colors.HexColor("#FFF2CC"), borderPadding=4, spaceAfter=6))
TAG = {"RP": ("#1E7B34", "REALIZADO COM EVIDÊNCIA PÚBLICA"), "PL": ("#B45F06", "PLANEJADO POR FALTA DE ACESSO"), "SM": ("#6A1B9A", "SIMULADO PARA FINS DIDÁTICOS")}
def P(t, st="b"): return Paragraph(S(t), ST[st])
def proc_par(tag, txt):
    c, n = TAG[tag]; return Paragraph(f'<font color="{c}"><b>[{tag}]</b></font> {S(txt)}', ST["b"])
def footer(c, d):
    c.saveState(); c.setFont("Helvetica", 7); c.setFillColor(colors.HexColor("#555555"))
    c.drawString(1.8 * cm, 1.0 * cm, f"Dossiê didático - ALLOS S.A. 2025 | matrícula {MAT} | {DATA} | dados sintéticos identificados | sem opinião de auditor")
    c.drawRightString(A4[0] - 1.8 * cm, 1.0 * cm, f"pág. {d.page}"); c.restoreState()
doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=1.8 * cm, rightMargin=1.8 * cm, topMargin=1.6 * cm, bottomMargin=1.7 * cm,
                      title="Dossiê de auditoria - ALLOS S.A. - 2025", author=f"Matrícula {MAT}")
doc.addPageTemplates([PageTemplate(id="p", frames=[Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")], onPage=footer)])
E = []
# ---------------- capa ----------------
E += [Spacer(1, 2.5 * cm), P("DOSSIÊ DE AUDITORIA - ALLOS S.A. (B3: ALOS3)", "h1"), P("Demonstrações contábeis anuais de 31/12/2025 e comparativos de 2024. NBC TA Estrutura Conceitual e NBC TA 200 a 600.", "h2"),
      Spacer(1, 0.4 * cm), P(f"Trabalho individual | Preparador: matrícula {MAT} | Data de preparação: {DATA} | Campo de revisão: em branco, sem revisão ou assinatura simulada de terceiros."),
      Spacer(1, 0.3 * cm),
      P("AVISO 1 - Este é um exercício didático. NÃO é opinião de auditor independente e NÃO houve contato com a companhia, auditores, clientes ou fornecedores. Nenhuma confirmação, entrevista, inspeção física ou acesso a sistemas foi realizado.", "warn"),
      P("AVISO 2 - A base de 520.150 registros de Propriedades para Investimento é SINTÉTICA. Foi calibrada apenas nos totais reais divulgados pela Allos na nota 11. Nenhuma linha é registro real. Os erros nela existentes foram inseridos propositalmente e estão registrados.", "warn"),
      P("Classificação dos procedimentos: [RP] Realizado com evidência pública | [PL] Planejado por falta de acesso | [SM] Simulado para fins didáticos (dados sintéticos).")]
E += [Spacer(1, 0.3 * cm), P("1. Identificação da companhia", "h2"),
      P("ALLOS S.A. (B3: ALOS3), plataforma de shopping centers; Novo Mercado. Histórico de nome e código: a companhia era a Aliansce Sonae Shopping Centers S.A. (código ALSO3, nome de pregão Alianscsonae), resultante da combinação Aliansce + Sonae Sierra de 2019 (W9); após a fusão com a BRMalls (2023), a assembleia de 17/10/2023 aprovou a nova denominação ALLOS S.A. e, a partir de 25/10/2023, as ações passaram a ser negociadas como ALOS3, com nome de pregão ALLOS (W7, W8). A companhia atribuída é a mesma. Datas e códigos de fontes secundárias devem ser conferidos no Formulário Cadastral e nos comunicados no site de RI/CVM. Auditor das DFs de 2025 (real): Deloitte Touche Tohmatsu Auditores Independentes Ltda., relatório de 10/03/2026 com opinião sem ressalva e PAAs sobre receita de aluguel e valor recuperável de PPI e ágios (F1 p.10-14)."),
      P("Dados-chave reais, consolidado 31/12/2025 (R$ mil; F1 p.15-17): ativo total 26.006.439; propriedades para investimento 20.381.666 (78,4% do ativo); receita líquida 2.859.106; LAIR 1.017.601; lucro líquido 945.293; patrimônio líquido 13.899.006."),
      PageBreak()]
# ---------------- índice / convenções ----------------
E += [P("2. Índice, convenções e matriz de cobertura", "h1"),
      P("Convenção de códigos: PT EC = Estrutura Conceitual; PT nnn = papel da NBC TA nnn. F = fonte documental; W = fonte web; ref. = referência cruzada. Cada PT contém: código, título, norma/itens; objetivo e conta; afirmações e riscos; população, fontes e critérios; procedimentos; evidências e referências cruzadas; resultados, exceções, conclusão e limitações; preparador e campo de revisão.")]
rows = [["PT", "Título", "Norma"]] + [[p["cod"], Paragraph(S(p["titulo"]), ST["sm"]), Paragraph(S(p["norma"].split("(")[0].strip()), ST["sm"])] for p in PTS]
t = Table(rows, colWidths=[1.6 * cm, 10.3 * cm, 5.4 * cm], repeatRows=1)
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F3864")), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white), ("FONTSIZE", (0, 0), (-1, -1), 7.4), ("GRID", (0, 0), (-1, -1), 0.3, colors.grey), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")]))
E += [t, Spacer(1, 0.3 * cm), P("Versões das normas consultadas (portal do CFC, lista 'NBC TA de auditoria independente', acesso em 20/10/2026, https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/). Regra: aplicar a versão em vigor para o exercício de 2025. Itens das normas são indicados por tema; a numeração de parágrafos não foi incluída porque os textos integrais das normas não foram lidos nesta preparação.", "b")]
rows = [["PT", "Norma e versão", "Publicação", "Observação"]] + [[c, Paragraph(S(v[0]), ST["sm"]), v[1], Paragraph(S(v[2]), ST["sm"])] for c, v in VERS.items()]
t = Table(rows, colWidths=[1.5 * cm, 5.0 * cm, 2.6 * cm, 8.2 * cm], repeatRows=1)
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F3864")), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white), ("FONTSIZE", (0, 0), (-1, -1), 7.2), ("GRID", (0, 0), (-1, -1), 0.3, colors.grey), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")]))
E += [t, PageBreak()]
# ---------------- fontes ----------------
src = [("F1", "relatório_do_auditor_independente_allos.pdf (98 p.). Conteúdo: comentário de desempenho 2025, DFs, notas e relatório da Deloitte de 10/03/2026. Origem informada: https://cdn.financialreports.eu/financialreports/media/filings/52822/2026/RNS/52822_rns_2026-03-10_cb3634d8-4c11-4a92-bf6d-355af0fd85e0.pdf", "20/10/2026", "Exercício 2025 (comparativo 2024)"),
       ("F2", "allos_drp_4t25_merged.pdf (173 p.): Relatório de Resultados 4T25 e ITRs de 1T25 e 2T25 (balanços de 31/03 e 30/06/2025, p.126-127 e p.76-77). Origem: https://ri.allos.com.br/informacoes-financeiras/central-de-resultados/", "20/10/2026", "4T25; ITR 1T25/2T25"),
       ("F3", "possivel_nota_explicativa_da_allos.pdf (5 p.): publicação legal no Valor Econômico, 18/03/2026 (relatório da administração e DFs resumidas). Origem: https://publicidadelegal.valor.com.br/valor/2026/03/18/ALLOS1588221418032026.pdf", "20/10/2026", "Exercício 2025"),
       ("W1", "Projeções gerenciais da Allos (EBITDA 2025 e sinergias): https://acionista.com.br/projecoes-gerenciais-da-allos-s-a-ganham-novas-diretrizes/", "20/10/2026", "2025"),
       ("W2", "Comunicado ao Mercado - Incidente Shopping Tijuca, 04/01/2026: https://acionista.com.br/wp-content/uploads/2026/01/ALLOS_S.A-Comunicado_ao_Mercado-Incidente_no_Shopping_Tijuca_-04-01-2026.pdf", "20/10/2026", "2026 (evento subsequente)"),
       ("W3", "Genial Análises, Prévia 2T26 (22/07/2026): https://analisa.genialinvestimentos.com.br/acoes/aliansce-sonae/allos-alos3-previa-2t26-fundamentos-firmes", "20/10/2026", "2026"),
       ("W4", "Safra/Especialista, resultados do 2T26: https://oespecialista.safra.com.br/analise/allos-resultados-segundo-trimestre-2026/", "20/10/2026", "2026"),
       ("W5", "Nord Investimentos, resultados do 1T26: https://www.nordinvestimentos.com.br/blog/allos-alos3-resultados-1t26/", "20/10/2026", "2026"),
       ("W6", "Visão do histórico ALOS3 (origem Aliansce Sonae): https://visnoinvest.com.br/stocks/ALOS3", "20/10/2026", "histórico"),
       ("F4", "Lista de NBC TA de auditoria independente (versões e datas de publicação): https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/", "20/10/2026", "versões vigentes na consulta"),
       ("W7", "Comunicado ao Mercado: novo código ALOS3 em substituição a ALSO3 e nome de pregão ALLOS: https://acionista.com.br/allos-alos-novo-codigo-de-negociacao-ticker/", "20/10/2026", "2023"),
       ("W8", "Nova razão social ALLOS S.A. (antes Aliansce Sonae Shopping Centers S.A.) e ticker ALOS3 em 25/10: https://euqueroinvestir.com/acoes/allos-also3-nova-razao-social-ticker-alos3", "20/10/2026", "2023"),
       ("W9", "Bloomberg Línea: fusão Aliansce+Sonae Sierra (2019), fusão com brMalls e mudança de nome: https://www.bloomberglinea.com.br/negocios/aliansce-agora-allos-mira-o-centro-oeste-e-a-atracao-de-marcas-globais-diz-ceo/", "20/10/2026", "2019-2023")]
E += [P("3. Relação de fontes", "h1"), P("Para cada fonte: endereço, data de acesso, documento, página (indicada em cada PT) e exercício. Páginas citadas de F1 e F2 = número de página do arquivo PDF. Fontes W são secundárias (baixa confiabilidade) e usadas como indício.")]
rows = [["ID", "Documento / endereço", "Acesso", "Exercício"]] + [[a, Paragraph(S(b), ST["sm"]), c, Paragraph(S(d), ST["sm"])] for a, b, c, d in src]
t = Table(rows, colWidths=[1.0 * cm, 11.3 * cm, 1.9 * cm, 3.1 * cm], repeatRows=1)
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F3864")), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white), ("FONTSIZE", (0, 0), (-1, -1), 7.4), ("GRID", (0, 0), (-1, -1), 0.3, colors.grey), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")]))
E += [t, Spacer(1, 0.2 * cm), P("Observação de rastreabilidade: os nomes dos arquivos enviados não correspondem ao conteúdo (por exemplo, o arquivo 'relatório do auditor' contém as DFs e as notas completas). O conteúdo foi verificado página a página e prevalece sobre o nome do arquivo.", "sm"), PageBreak()]
# ---------------- PTs ----------------
def sec(label, content_pars):
    return [P(label, "lab")] + content_pars
for p in PTS:
    vn, vd, vs = VERS[p["cod"]]; itens = re.search(r"\((.*)\)\s*$", p["norma"]).group(1)
    head = [P(f'{p["cod"]} - {p["titulo"]}', "h1"), P(f'<b>Norma e versão consultada:</b> {vn} ({vd}); fonte CFC, acesso em 20/10/2026.'), P(f'<b>Itens utilizados (por tema):</b> {itens}.')]
    E += head
    E += sec("OBJETIVO E CONTA / PROCESSO / DIVULGAÇÃO EXAMINADA", [P(p["objetivo"])])
    E += sec("AFIRMAÇÕES RELEVANTES E RISCOS IDENTIFICADOS", [P(p["afirmacoes"])])
    E += sec("POPULAÇÃO, FONTES E CRITÉRIOS DE SELEÇÃO", [P(p["pop"])])
    E += sec("PROCEDIMENTOS (cada um classificado: RP / PL / SM)", [proc_par(t, x) for t, x in p["proc"]])
    E += sec("EVIDÊNCIAS E REFERÊNCIAS CRUZADAS", [P(p["evid"])])
    E += sec("RESULTADOS, EXCEÇÕES, CONCLUSÃO E LIMITAÇÕES", [P(p["res"]), P("<b>Exceções:</b> " + EXC[p["cod"]])])
    E += [Spacer(1, 4), P(f'<b>Preparado por:</b> matrícula {MAT} em {DATA}. <b>Revisão:</b> ____________________ data: ___/___/_____ (campo reservado; nenhuma revisão ou assinatura foi simulada).', "sm"), PageBreak()]
# ---------------- Anexo A programas ----------------
E += [P("Anexo A - Programas de auditoria por ciclo", "h1"), P("Programas para receitas, disponibilidades, estoques, imobilizado/PPI, passivos e estimativas, conforme aplicáveis à ALLOS. Cada procedimento está classificado como RP, PL ou SM.")]
for cod, tit, ctx, procs in ANEXOS:
    E += [P(f"{cod} - {tit}", "h2"), P(f"<b>Riscos/afirmações:</b> {ctx}")] + [proc_par(t, x) for t, x in procs]
E += [PageBreak()]
# ---------------- Anexo B erros ----------------
E += [P("Anexo B - Erros inseridos x exceções identificadas (base sintética)", "h1"),
      P("Registro de erros: dados/registro_erros_inseridos.csv (1.040 linhas). A coluna 'efeito_no_total_da_base_RS' concilia a base final ao saldo da DFP. Resultado dos testes na população (CAAT):")]
cp = list(csv.DictReader(open(os.path.join(BASE, "..", "dados", "resultados", "comparacao_erros_inseridos_x_identificados_populacao.csv"), encoding="utf-8")))
rows = [["Tipo de erro", "Inseridos", "Sinalizados", "Verdadeiros +", "Falsos +", "Não detectados", "Detecção"]] + [[r["tipo_erro"], r["inseridos"], r["sinalizados_pelo_teste"], r["verdadeiros_positivos"], r["falsos_positivos"], r["nao_detectados"], f'{float(r["taxa_deteccao"]):.0%}'] for r in cp]
t = Table(rows, colWidths=[5.2 * cm, 1.7 * cm, 2.1 * cm, 2.2 * cm, 1.6 * cm, 2.5 * cm, 1.8 * cm], repeatRows=1)
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F3864")), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white), ("FONTSIZE", (0, 0), (-1, -1), 7.4), ("GRID", (0, 0), (-1, -1), 0.3, colors.grey), ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")]))
E += [t, Spacer(1, 4), P("Os 183 falsos positivos do teste de depreciação são efeitos colaterais: 112 em ativos cuja data de ativação foi alterada para 2026 (erro de corte) e 71 em ativos cujo custo foi alterado por lançamento manual atípico; o recálculo usa esses atributos. Não há falso positivo 'puro'."),
      P("Por amostra MUS (n=1.570 + 4 itens-chave + 60 negativos): limite superior de distorção R$ 100.530.747 > erro tolerável R$ 38.160.038.")]
E += [PageBreak()]

# ---------------- Anexo C base simulada ----------------
DIC = [("id_registro","texto","Identificador único do registro (PPI-0000001...). Os 150 duplicados inseridos têm ids novos."),
("id_shopping","texto","Código sintético do shopping center (SHP-01 a SHP-45; 45 = shoppings com participação, F1 p.3). Não corresponde a nenhum shopping real."),
("participacao_pct","número","Fração ideal sintética do ativo detida (%)."),("classe_ativo","texto","Terreno, Edificações, Instalações, Benfeitorias e acabamentos, Equipamentos e sistemas, Obras em andamento, Direito de uso."),
("origem","texto","Aquisição/construção própria, Combinação de negócios (com mais-valia) ou Adição 2025."),("data_ativacao","data AAAA-MM-DD","Data em que o ativo entrou em uso."),
("vida_util_anos","inteiro","Vida útil sintética (0 = não depreciável: terreno e obra em andamento)."),("valor_custo","R$","Custo de aquisição/construção."),
("depreciacao_acumulada","R$","Depreciação acumulada até 31/12/2025."),("mais_valia_liquida","R$","Mais-valia líquida de combinação de negócios."),
("valor_contabil_liquido","R$","Custo - depreciação acumulada + mais-valia líquida (identidade testada)."),("depreciacao_exercicio_2025","R$","Depreciação do exercício; recalculada como custo/vida útil, proporcional aos dias em 2025 para adições do ano."),
("status","texto","Em operação, Em desenvolvimento ou Baixado."),("documento_suporte","texto","Referência sintética de NF, laudo, escritura ou contrato (vazio = sem suporte)."),
("tipo_lancamento","texto","Automático ou Manual."),("usuario_lancamento","texto","Usuário sintético (U001-U060 válidos; U099 fora do cadastro)."),("data_lancamento","data","Data de lançamento contábil.")]
E += [P("Anexo C - Base simulada: justificativa, premissas, método, dicionário e conciliação", "h1"),
 P("<b>Escolha da conta e materialidade.</b> Pelo balanço consolidado de 31/12/2025 (F1 p.15), a maior conta do ativo é Propriedades para Investimento: R$ 20.381.666 mil, 78,4% do ativo total (R$ 26.006.439 mil) e muito acima da segunda (aplicações financeiras, R$ 2.536.587 mil, 9,8%). A nota 11 (F1 p.64-66) decompõe o saldo em custo R$ 10.800.757 mil, depreciação acumulada (R$ 2.711.228 mil) e mais-valia líquida R$ 12.292.137 mil; o auditor real a trata como PAA (F1 p.11-12)."),
 P("<b>Premissas.</b> Cada linha é um componente contábil de ativo (terreno, edificação, instalação, benfeitoria, equipamento, obra, direito de uso) de um dos 45 shoppings sintéticos, com custo lognormal e classe, vida útil e idade variáveis. Calibração real: (i) soma de custo, depreciação acumulada e mais-valia = valores da nota 11; (ii) terrenos somam R$ 70.566 mil; (iii) adições de 2025 somam o custo de R$ 493.617 mil divulgado na nota 11 (instalações e edificações 361.710 + direito de uso 5.124 + Shopping Brasília 116.653 + outros 10.130). A despesa de depreciação NÃO foi calibrada (ver PT 520)."),
 P("<b>Método de geração.</b> Script codigo/01_gerar_base.py, semente = matrícula (231004987), numpy/pandas; 520.000 linhas-base + 150 duplicadas inseridas = 520.150. Valores em centavos inteiros com ajuste do resíduo para fechar exatamente os totais-alvo. Em seguida, inserção de 1.040 erros/anomalias de 8 tipos, com registro (id, campo, valor original, valor inserido, efeito no total, distorção potencial)."),
 P("<b>Conciliação.</b> Base limpa = R$ 20.381.666.000,00 = saldo DFP (diferença zero). Base final = R$ 20.448.164.979,64; diferença de R$ 66.498.979,64 = soma dos efeitos dos erros inseridos (R$ 66.498.979,59) + R$ 0,05 de arredondamento."), P("<b>Dicionário de variáveis</b>", "h2")]
rows = [["Variável", "Tipo", "Descrição"]] + [[a, b, Paragraph(S(c), ST["sm"])] for a, b, c in DIC]
t = Table(rows, colWidths=[4.0 * cm, 2.3 * cm, 11.0 * cm], repeatRows=1)
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F3864")), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white), ("FONTSIZE", (0, 0), (-1, -1), 7.4), ("GRID", (0, 0), (-1, -1), 0.3, colors.grey), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")]))
E += [t, PageBreak()]
with open(os.path.join(BASE, "..", "dados", "dicionario_de_variaveis.md"), "w", encoding="utf-8") as f:
    f.write("# Dicionário de variáveis - base SINTÉTICA de Propriedades para Investimento (ALLOS 2025)\n\nMatrícula 231004987. DADOS SINTÉTICOS, não são registros reais da Allos.\n\n| Variável | Tipo | Descrição |\n|---|---|---|\n")
    for a, b, c in DIC: f.write(f"| {a} | {b} | {c} |\n")

# ---------------- Conclusão ----------------
E += [P("4. Conclusão integrada", "h1"),
      P("<b>Riscos.</b> Com base em evidência pública (F1), os riscos significativos da ALLOS são: (R1) reconhecimento da receita de aluguel por linearização (risco presumido de fraude); (R2) valor recuperável das propriedades para investimento (R$ 20,38 bi) e dos ágios (R$ 324,8 mi); (R3) burla de controles. Complementares: PCE (R$ 546,4 mi), covenants e endividamento (R$ 5,88 bi), contingências, imposto diferido, estrutura societária complexa e o incêndio no Shopping Tijuca em janeiro de 2026."),
      P("<b>Procedimentos realizados com evidência pública.</b> Reconciliação das DFs (balanço x notas x DRE x DVA, sem diferença); roll-forward do PPI; testes de saldos de abertura contra uma segunda fonte; analíticos com investigação das variações acima do limite; recálculo da PCE; indicadores de liquidez e covenants; eventos subsequentes; mapa de partes relacionadas, grupo e segmentos."),
      P(f"<b>Procedimentos simulados.</b> Base sintética de 520.150 registros, conciliada ao saldo real (diferença explicada pelos erros inseridos: R$ 66.498.979,59; resíduo de R$ 0,05); CAAT com 100% de detecção dos erros inseridos; amostra MUS com limite superior superior ao erro tolerável; distorções quantificadas de R$ 65.752.721 (129% da materialidade global de R$ 50.880.050), cenário que, se real, exigiria correção, ampliação de testes e possível modificação da opinião."),
      P("<b>Procedimentos planejados.</b> Testes de controles, confirmações externas (nenhuma enviada), inspeção física, relatórios SOC 1, avaliação com especialista do valor recuperável, litígios com assessores, entrevistas, completude de partes relacionadas, auditores de componentes e carta de representações."),
      P("<b>Limitações.</b> Informações públicas apenas; sem acesso a razão, sistemas, premissas internas, atas e contratos; base sintética que NÃO é evidência sobre a ALLOS; edição das normas a confirmar; expectativa de reajuste de 4% é premissa; fontes secundárias com baixa confiabilidade; ausência de revisão independente."),
      P("<b>Conclusão.</b> Os documentos públicos, internamente consistentes, não revelam indício de distorção relevante nem de dúvida significativa sobre a continuidade. Contudo, esta conclusão é provisória e se limita às evidências disponíveis; ela NÃO constitui opinião profissional independente sobre as demonstrações contábeis da ALLOS S.A.", "b"),
      Spacer(1, 6), P(f"Preparado por: matrícula {MAT} em {DATA}. Controle de versões: v1.0 de {DATA}. Revisão: ____________ (reservado).", "sm")]
doc.build(E); print("PDF ok:", OUT)
