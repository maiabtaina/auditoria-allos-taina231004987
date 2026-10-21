#!/usr/bin/env python3
"""03_gerar_planilhas.py | Planilhas editáveis (fórmulas vivas) | ALLOS 2025 | matrícula 231004987 | 20/10/2026
Entradas em AZUL = dados reais da DFP 2025 (R$ mil) ou premissas; pretas = fórmulas; verdes = vínculo entre abas."""
import os, json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
BASE = os.path.dirname(os.path.abspath(__file__))
res = json.load(open(os.path.join(BASE, "..", "dados", "resultados", "resultados.json")))
OUT = os.path.join(BASE, "..", "planilhas", "papeis_de_trabalho_calculos_allos_2025.xlsx")
F = "Arial"
blue = Font(name=F, color="0000FF"); blk = Font(name=F); bold = Font(name=F, bold=True); grn = Font(name=F, color="008000")
hdr = PatternFill("solid", fgColor="1F3864"); hf = Font(name=F, bold=True, color="FFFFFF"); yel = PatternFill("solid", fgColor="FFFF99")
wb = Workbook()
def sheet(name, title, widths):
    ws = wb.create_sheet(name); ws["A1"] = title; ws["A1"].font = Font(name=F, bold=True, size=12)
    ws["A2"] = "Preparador: matrícula 231004987 | Data: 20/10/2026 | Revisão: ____________ (campo reservado; sem assinatura simulada) | Valores em R$ mil, salvo indicação"; ws["A2"].font = Font(name=F, italic=True, size=9)
    for i, w in enumerate(widths): ws.column_dimensions[chr(65 + i)].width = w
    return ws
def head(ws, r, vals):
    for i, v in enumerate(vals):
        c = ws.cell(r, i + 1, v); c.font = hf; c.fill = hdr; c.alignment = Alignment(wrap_text=True, vertical="center")
def put(ws, ref, v, font=None, fmt=None):
    ws[ref] = v; ws[ref].font = font or (blk if (isinstance(v, str) and v.startswith("=")) else blue if isinstance(v, (int, float)) else blk)
    if fmt: ws[ref].number_format = fmt
N0 = '#,##0;(#,##0);"-"'; P1 = '0.0%'; N2 = '#,##0.00;(#,##0.00);"-"'
wb.remove(wb.active)

# ---------- PT 320 Materialidade ----------
ws = sheet("PT320_Materialidade", "PT 320 - Materialidade (NBC TA 320) - ALLOS S.A. consolidado 31/12/2025", [46, 16, 12, 16, 60])
head(ws, 4, ["Base de referência (DFP 2025, consolidado)", "Valor (R$ mil)", "% usado", "Resultado (R$ mil)", "Fonte / justificativa"])
bases = [("Lucro antes dos impostos e contribuições (LAIR)", 1017601, 0.05, "DFP 2025, DRE (PDF p.17; pág. 8 das DFs). Base ESCOLHIDA: medida de resultado estável, 5% (faixa usual 5%)."),
         ("Receita líquida de aluguel e serviços", 2859106, 0.01, "DFP 2025, DRE. Alternativa (1% da receita), apenas comparação."),
         ("Total do ativo", 26006439, 0.005, "DFP 2025, balanço. Alternativa (0,5% do ativo), apenas comparação."),
         ("Patrimônio líquido", 13899006, 0.01, "DFP 2025, balanço. Alternativa (1% do PL), apenas comparação.")]
for i, (n, v, p, j) in enumerate(bases):
    r = 5 + i; put(ws, f"A{r}", n); put(ws, f"B{r}", v, fmt=N0); put(ws, f"C{r}", p, fmt=P1); put(ws, f"D{r}", f"=B{r}*C{r}", fmt=N0); put(ws, f"E{r}", j)
put(ws, "A10", "MATERIALIDADE GLOBAL (escolhida = LAIR x 5%)", bold); put(ws, "D10", "=D5", fmt=N0); ws["D10"].fill = yel
put(ws, "A11", "% da materialidade para execução (ME)"); put(ws, "C11", 0.75, fmt=P1); put(ws, "D11", "=D10*C11", fmt=N0); put(ws, "E11", "75%: risco inerente alto (estimativas de valor recuperável) e ambiente sem histórico de auditoria no trabalho (didático).")
put(ws, "A12", "Limite de distorções claramente triviais (5% da global)"); put(ws, "C12", 0.05, fmt=P1); put(ws, "D12", "=D10*C12", fmt=N0)
put(ws, "A14", "Materialidade específica 1 - Remuneração da administração/partes relacionadas (se aplicável)"); put(ws, "E14", "PLANEJADO: depende de dado interno; usar 10% do saldo/ transação da nota 23 (saldos de partes relacionadas R$ 55.865 ativo / 7.361 passivo).")
put(ws, "A15", "Materialidade específica 2 - Propriedades para investimento (saldo mais relevante)"); put(ws, "B15", 20381666, fmt=N0); put(ws, "C15", 0.0025, fmt='0.00%'); put(ws, "D15", "=B15*C15", fmt=N0); put(ws, "E15", "0,25% do saldo; exibida para confronto com a ME (resulta em valor maior que a global: NÃO adotada; prevalece a global).")
put(ws, "A17", "Revisão da materialidade no curso do trabalho"); put(ws, "E17", "Sem informação nova que a altere. Se distorções quantificadas > global (ver PT450), reavaliar ME e ampliar testes.")
put(ws, "A19", "Em R$ (unidade da base simulada)"); put(ws, "B19", "=D10*1000", fmt=N2); put(ws, "C19", "=D11*1000", fmt=N2); put(ws, "D19", "=D12*1000", fmt=N2); put(ws, "E19", "B = global | C = execução | D = trivial")

# ---------- PT 500 Conciliação ----------
ws = sheet("PT500_Conciliacao", "PT 500 - Conciliação da base simulada com o saldo contábil (nota 11) - DADOS SINTÉTICOS x DFP REAL", [62, 22, 60])
head(ws, 4, ["Item", "R$", "Observação"])
rows = [("Custo (nota 11, consolidado, R$ mil)", 10800757, "REAL - DFP 2025, PDF p.66"), ("(-) Depreciação acumulada (R$ mil)", -2711228, "REAL"), ("(+) Mais-valia líquida (R$ mil)", 12292137, "REAL")]
for i, (n, v, o) in enumerate(rows): put(ws, f"A{5+i}", n); put(ws, f"B{5+i}", v, fmt=N0); put(ws, f"C{5+i}", o)
put(ws, "A8", "Saldo contábil - Propriedades para investimento (R$ mil)", bold); put(ws, "B8", "=SUM(B5:B7)", fmt=N0)
put(ws, "A9", "Saldo no balanço consolidado 31/12/2025 (R$ mil)"); put(ws, "B9", 20381666, fmt=N0); put(ws, "C9", "REAL - balanço, PDF p.15 (pág.6 das DFs)")
put(ws, "A10", "Diferença nota 11 x balanço (deve ser zero)"); put(ws, "B10", "=B8-B9", fmt=N0)
put(ws, "A12", "Base SIMULADA - soma do valor contábil líquido (R$)", bold); put(ws, "B12", res["conciliacao"]["vcl_base"], fmt=N2); put(ws, "C12", "SINTÉTICO - script 02 (520.150 linhas)")
put(ws, "A13", "Saldo DFP em R$"); put(ws, "B13", "=B9*1000", font=blk, fmt=N2)
put(ws, "A14", "Diferença base x saldo DFP (R$)"); put(ws, "B14", "=B12-B13", fmt=N2)
head(ws, 16, ["Explicação da diferença: erros inseridos (efeito no total da base)", "R$", "Registro: dados/registro_erros_inseridos.csv"])
r = 17
for rec in res["mapa_distorcoes"]:
    put(ws, f"A{r}", rec["tipo_erro"]); put(ws, f"B{r}", rec["efeito_sobre_saldo_da_base"], fmt=N2); put(ws, f"C{r}", f'{rec["qtd"]} registros'); r += 1
put(ws, f"A{r}", "Soma dos efeitos dos erros inseridos", bold); put(ws, f"B{r}", f"=SUM(B17:B{r-1})", fmt=N2)
put(ws, f"A{r+1}", "RESÍDUO NÃO EXPLICADO (arredondamento de centavos)", bold); put(ws, f"B{r+1}", f"=B14-B{r}", fmt=N2); ws[f"B{r+1}"].fill = yel
put(ws, f"C{r+1}", "Base limpa (antes dos erros) = saldo DFP exato; resíduo decorre de arredondamento em ponto flutuante ao gravar centavos.")
r += 4; head(ws, r, ["Roll-forward REAL do saldo (nota 11, R$ mil)", "R$ mil", "Fonte"])
rf = [("Saldo em 31/12/2024", 20700140, "DFP 2025 nota 11 (PDF p.65)"), ("Adições: instalações e edificações (líq. depreciação)", -91304, "nota 11"), ("Adições: direito de uso", -5576, "nota 11"),
      ("Aquisição do Shopping Brasília", 176577, "nota 11"), ("Outros", 4164, "nota 11"), ("Baixa: 9,9% Plaza Sul", -53881, "nota 11"), ("Baixa: 45% Rio Anil", -136703, "nota 11"),
      ("Baixa: 10% Tijuca", -150117, "nota 11"), ("Baixa: 20% Carioca", -61634, "nota 11")]
a = r + 1
for i, (n, v, o) in enumerate(rf): put(ws, f"A{a+i}", n); put(ws, f"B{a+i}", v, fmt=N0); put(ws, f"C{a+i}", o)
b = a + len(rf); put(ws, f"A{b}", "Saldo recalculado em 31/12/2025", bold); put(ws, f"B{b}", f"=SUM(B{a}:B{b-1})", fmt=N0)
put(ws, f"A{b+1}", "Diferença para o balanço (deve ser zero)"); put(ws, f"B{b+1}", f"=B{b}-B9", fmt=N0)

# ---------- PT 530 Amostragem ----------
ws = sheet("PT530_Amostragem", "PT 530 - Amostragem MUS sobre a BASE SIMULADA (propriedades para investimento)", [56, 22, 62])
head(ws, 4, ["Parâmetro", "Valor", "Nota"])
am = res["amostragem"]; ra = res["resultado_amostra"]
put(ws, "A5", "Erro tolerável (= materialidade de execução, R$)"); put(ws, "B5", "='PT320_Materialidade'!C19", font=grn, fmt=N2)
put(ws, "A6", "Fator de confiança RF (95%, erro esperado zero - Poisson)"); put(ws, "B6", am["RF"], fmt="0.00")
put(ws, "A7", "População sujeita a MUS (R$, sem itens-chave nem negativos)"); put(ws, "B7", am["populacao_testada_mus"], fmt=N2); put(ws, "C7", "SINTÉTICO")
put(ws, "A8", "Intervalo amostral (R$) = erro tolerável / RF"); put(ws, "B8", "=B5/B6", fmt=N2)
put(ws, "A9", "Tamanho da amostra calculado = população / intervalo"); put(ws, "B9", "=ROUNDUP(B7/B8,0)", fmt="#,##0")
put(ws, "A10", "Itens efetivamente selecionados (seleção sistemática, início aleatório, semente = matrícula)"); put(ws, "B10", am["itens_selecionados_mus"], fmt="#,##0"); put(ws, "C10", "Menor que o calculado: itens maiores que o intervalo são atingidos mais de uma vez e contados uma só.")
put(ws, "A11", "Itens-chave testados a 100% (valor >= erro tolerável)"); put(ws, "B11", am["itens_chave_100pct"], fmt="#,##0")
put(ws, "A12", "Itens com saldo negativo testados a 100%"); put(ws, "B12", res["itens_negativos"]["qtd"], fmt="#,##0")
put(ws, "A14", "Itens da amostra com exceção"); put(ws, "B14", ra["itens_com_excecao"], fmt="#,##0")
put(ws, "A15", "Itens da amostra com distorção monetária quantificada"); put(ws, "B15", ra["itens_com_distorcao_quantificada"], fmt="#,##0")
put(ws, "A16", "Distorção encontrada na amostra (R$)"); put(ws, "B16", ra["distorcao_na_amostra"], fmt=N2)
put(ws, "A17", "Precisão básica (R$) = RF x intervalo"); put(ws, "B17", "=B6*B8", fmt=N2)
put(ws, "A18", "Distorção projetada (R$) = soma(taint) x intervalo"); put(ws, "B18", ra["distorcao_projetada"], fmt=N2)
put(ws, "A19", "Limite superior de distorção - Stringer/Poisson (R$)", bold); put(ws, "B19", ra["limite_superior_stringer"], fmt=N2); ws["B19"].fill = yel
put(ws, "A20", "Conclusão estatística"); put(ws, "B20", '=IF(B19>B5,"NÃO ACEITA: limite superior > erro tolerável","ACEITA")'); put(ws, "C20", "Resultado SIMULADO. Em trabalho real: ampliar amostra, solicitar correção e reavaliar risco.")
put(ws, "A22", "Incrementos Poisson 95% (1º ao 10º erro ordenado por taint)"); 
for i, v in enumerate([1.75, 1.55, 1.46, 1.40, 1.36, 1.33, 1.31, 1.29, 1.28, 1.27]): put(ws, f"{chr(66+i) if i<2 else 'B'}{23+i}", v, fmt="0.00") if False else put(ws, f"B{23+i}", v, fmt="0.00")
put(ws, "C23", "Detalhe da amostra e das exceções: dados/resultados/amostra_mus_selecionada.csv")

# ---------- PT 540 PCE ----------
ws = sheet("PT540_PCE", "PT 540 - Estimativa: provisão para perdas de crédito esperadas (nota 8) - recálculo e sensibilidade", [40, 16, 16, 16, 16, 16, 16])
head(ws, 4, ["Faixa (aluguéis + CDU + cotas condominiais)", "A vencer", "<=90 dias", "91-180", "181-360", ">360", "Total"])
al = [314349, 16492, 15065, 19554, 287585]; cdu = [3121, 813, 450, 987, 20273]; ct = [15118, 1413, 3349, 10346, 129457]
for r_, (n, v) in zip((5, 6, 7), (("Aluguéis", al), ("Taxa de cessão de direito de uso", cdu), ("Cotas condominiais", ct))):
    put(ws, f"A{r_}", n)
    for i, x in enumerate(v): put(ws, f"{chr(66+i)}{r_}", x, fmt=N0)
    put(ws, f"G{r_}", f"=SUM(B{r_}:F{r_})", fmt=N0)
put(ws, "A8", "Total por faixa", bold)
for c in "BCDEFG": put(ws, f"{c}8", f"=SUM({c}5:{c}7)", fmt=N0)
put(ws, "A9", "% de provisão (matriz da nota 8, 31/12/2025)")
for i, x in enumerate([0.0378, 0.3952, 0.6579, 0.9101, 1.0]): put(ws, f"{chr(66+i)}9", x, fmt='0.00%')
put(ws, "A10", "PCE esperada por faixa (recálculo)")
for c in "BCDEF": put(ws, f"{c}10", f"={c}8*{c}9", fmt=N0)
put(ws, "G10", "=SUM(B10:F10)", fmt=N0)
put(ws, "A12", "PCE total registrada (balanço/nota 8)"); put(ws, "B12", 546430, fmt=N0)
put(ws, "A13", "PCE de prestação de serviços e outros (análise individual) - saldo bruto serviços+outros"); put(ws, "B13", "=73905+22999", fmt=N0)
put(ws, "A14", "Diferença: registrada - recalculada pela matriz"); put(ws, "B14", "=B12-G10", fmt=N0)
put(ws, "A15", "Diferença / saldo bruto de serviços e outros"); put(ws, "B15", "=B14/B13", fmt=P1); put(ws, "C15", "A diferença deve ser explicada pela análise individual (PLANEJADO: exige acesso à análise interna).")
put(ws, "A16", "Diferença vs materialidade de execução"); put(ws, "B16", "=B14/'PT320_Materialidade'!D11", fmt=P1)
head(ws, 18, ["Sensibilidade (pontos percentuais nas faixas vencidas)", "-10 p.p.", "-5 p.p.", "Base", "+5 p.p.", "+10 p.p.", ""])
put(ws, "A19", "PCE recalculada (R$ mil)")
for c, d in zip("BCDEF", (-0.10, -0.05, 0, 0.05, 0.10)):
    put(ws, f"{c}19", f"=B8*B9+SUMPRODUCT(C8:E8,MIN(1,MAX(0,1))*(C9:E9+({d})))+F8*F9" if False else f"=B8*B9+C8*MIN(1,C9+({d}))+D8*MIN(1,D9+({d}))+E8*MIN(1,E9+({d}))+F8*F9", fmt=N0)
put(ws, "A20", "Variação vs base (R$ mil)")
for c in "BCDEF": put(ws, f"{c}20", f"={c}19-$D$19", fmt=N0)
put(ws, "A21", "Variação vs materialidade de execução (x)")
for c in "BCDEF": put(ws, f"{c}21", f"=ABS({c}20)/'PT320_Materialidade'!$D$11", fmt='0.00"x"')

# ---------- PT 520 Analíticos ----------
ws = sheet("PT520_Analiticos", "PT 520 - Procedimentos analíticos (DFP 2025 x 2024, consolidado) - REALIZADO COM EVIDÊNCIA PÚBLICA", [44, 14, 14, 12, 12, 14, 14, 14, 40])
head(ws, 4, ["Conta (R$ mil)", "2025", "2024", "Var. R$", "Var. %", "Expectativa 2025", "Dif. real x esperada", "Investigar?", "Fonte / premissa"])
ws["A3"] = "Premissa didática de reajuste (inflação contratual proxy):"; ws["A3"].font = bold; put(ws, "D3", 0.04, fmt=P1); put(ws, "E3", "SUBSTITUIR pelo IPCA/IGP-M oficial do período; 4% é premissa do aluno, não dado público.")
an = [("Receitas de aluguéis", 2055493, 1973209, "nota 18", True), ("Estacionamento", 634500, 598008, "nota 18", True), ("Receita de serviços", 341541, 329946, "nota 18", True),
      ("Receita líquida total", 2859106, 2739848, "DRE", True), ("Custo de aluguéis e serviços", 746938, 718981, "DRE/nota 19", True), ("Depreciação e amortização de propriedades (custo)", 459233, 451396, "nota 19", False),
      ("Despesas com vendas, gerais e administrativas", 692505, 704220, "nota 20", True), ("Resultado financeiro líquido", -521759, -584923, "DRE/nota 21", False),
      ("Lucro antes dos impostos (LAIR)", 1017601, 868181, "DRE", False), ("Contas a receber líquido (circ.+não circ.)", 554236, 585193, "nota 8", False), ("Provisão p/ perdas de crédito esperadas", 546430, 519209, "nota 8", False),
      ("Propriedades para investimento", 20381666, 20700140, "balanço/nota 11", False), ("Aplicações financeiras (circ.+não circ.)", 2536587, 3511385, "nota 7", False),
      ("Empréstimos, financiamentos e debêntures", 5879310, 6645024, "nota 13/5", False), ("Obrigações por compra e venda de ativos", 17887, 427236, "nota 15.1", False),
      ("Provisão para contingências", 254628, 241548, "nota 14", False), ("Depósitos judiciais", 192477, 169019, "balanço", False), ("Dividendos a pagar", 440839, 211798, "balanço", False)]
for i, (n, a25, a24, src, esp) in enumerate(an):
    r = 5 + i; put(ws, f"A{r}", n); put(ws, f"B{r}", a25, fmt=N0); put(ws, f"C{r}", a24, fmt=N0); put(ws, f"D{r}", f"=B{r}-C{r}", fmt=N0); put(ws, f"E{r}", f"=IF(C{r}=0,0,D{r}/ABS(C{r}))", fmt=P1)
    if esp: put(ws, f"F{r}", f"=C{r}*(1+$D$3)", fmt=N0); put(ws, f"G{r}", f"=B{r}-F{r}", fmt=N0); put(ws, f"H{r}", f"=IF(ABS(G{r})>'PT320_Materialidade'!$D$11,\"SIM\",\"não\")")
    else: put(ws, f"H{r}", f"=IF(ABS(D{r})>'PT320_Materialidade'!$D$11,\"SIM\",\"não\")")
    put(ws, f"I{r}", src)
last = 5 + len(an)
put(ws, f"A{last+1}", "Limite de investigação = materialidade de execução (R$ mil)"); put(ws, f"B{last+1}", "='PT320_Materialidade'!D11", font=grn, fmt=N0)
put(ws, f"A{last+2}", "Obs.: onde não há expectativa independente (linhas sem coluna F), o teste é de variação absoluta contra o limite; 'SIM' exige explicação documentada (PT 520).")

# ---------- PT 570 ----------
ws = sheet("PT570_Continuidade", "PT 570 - Continuidade operacional: liquidez e endividamento (DFP 2025, consolidado) - REAL", [52, 16, 16, 50])
head(ws, 4, ["Indicador (R$ mil)", "31/12/2025", "31/12/2024", "Fonte"])
li = [("Ativo circulante", 3316531, 4271851, "balanço"), ("Passivo circulante", 1284420, 2265460, "balanço"), ("Caixa e equivalentes", 60570, 47771, "balanço"), ("Aplicações financeiras (total)", 2536587, 3511385, "nota 7"),
      ("Empréstimos, financiamentos e debêntures (total)", 5879310, 6645024, "nota 5/13"), ("Obrigações compra e venda de ativos", 17887, 427236, "nota 5"), ("Derivativos (passivo)", 132740, 158383, "nota 5"), ("Patrimônio líquido", 13899006, 14134520, "balanço")]
for i, (n, a, b, s) in enumerate(li): r = 5 + i; put(ws, f"A{r}", n); put(ws, f"B{r}", a, fmt=N0); put(ws, f"C{r}", b, fmt=N0); put(ws, f"D{r}", s)
put(ws, "A14", "Liquidez corrente", bold); put(ws, "B14", "=B5/B6", fmt='0.00"x"'); put(ws, "C14", "=C5/C6", fmt='0.00"x"')
put(ws, "A15", "Dívida líquida (empréstimos + obrigações - caixa - aplicações + derivativos)"); put(ws, "B15", "=B9+B10-B7-B8+B11", fmt=N0); put(ws, "C15", "=C9+C10-C7-C8+C11", fmt=N0); put(ws, "D15", "Nota 5 divulga 3.432.780 (2025) e 3.671.487 (2024)")
put(ws, "A16", "Dívida líquida / PL"); put(ws, "B16", "=B15/B12", fmt=P1); put(ws, "C16", "=C15/C12", fmt=P1)
put(ws, "A17", "Diferença para a dívida líquida da nota 5 (2025)"); put(ws, "B17", "=B15-3432780", fmt=N0)
put(ws, "A18", "EBITDA gerencial 2025 (R$ mil) - fonte secundária; usar o oficial"); put(ws, "B18", 2076500, fmt=N0); put(ws, "D18", "Fato Relevante 10/03/2026 (via acionista.com.br)")
put(ws, "A19", "Dívida líquida / EBITDA (covenant da nota 13: <= 3,5x, base gerencial ajustada)"); put(ws, "B19", "=B15/B18", fmt='0.00"x"'); put(ws, "D19", "Aproximação: o covenant usa EBITDA Ajustado Consolidado Gerencial; cálculo contratual = PLANEJADO (exige dados internos).")
put(ws, "A20", "Folga vs limite 3,5x"); put(ws, "B20", "=3.5-B19", fmt='0.00"x"')

# ---------- PT 450 ----------
ws = sheet("PT450_Distorcoes", "PT 450 - Mapa de distorções (SIMULADAS na base sintética; nenhuma é achado sobre a Allos real)", [34, 10, 22, 22, 22, 30])
head(ws, 4, ["Tipo (registro de erros inseridos)", "Qtd", "Distorção potencial (R$)", "Efeito no saldo da base (R$)", "Corrigida?", "Natureza"])
nat = {"DUPLICIDADE": "Quantitativa - existência", "CORTE (ATIVACAO EM 2026)": "Quantitativa - corte", "DEPRECIACAO INCORRETA": "Quantitativa - mensuração", "BAIXADO COM SALDO": "Quantitativa - existência/direitos",
       "VCL NEGATIVO": "Quantitativa - mensuração", "TERRENO DEPRECIADO": "Quantitativa - classificação", "SEM DOCUMENTO SUPORTE": "Controle (potencial)", "LANCAMENTO MANUAL ATIPICO": "Qualitativa - burla de controles/fraude (NBC TA 240)"}
for i, rec in enumerate(res["mapa_distorcoes"]):
    r = 5 + i; put(ws, f"A{r}", rec["tipo_erro"]); put(ws, f"B{r}", rec["qtd"], fmt="#,##0"); put(ws, f"C{r}", rec["distorcao_potencial_total"], fmt=N2); put(ws, f"D{r}", rec["efeito_sobre_saldo_da_base"], fmt=N2); put(ws, f"E{r}", "Não (simulação: pendente de ajuste)"); put(ws, f"F{r}", nat.get(rec["tipo_erro"], ""))
e = 5 + len(res["mapa_distorcoes"])
put(ws, f"A{e}", "TOTAL", bold); put(ws, f"B{e}", f"=SUM(B5:B{e-1})", fmt="#,##0"); put(ws, f"C{e}", f"=SUM(C5:C{e-1})", fmt=N2)
put(ws, f"A{e+1}", "Distorções monetárias quantificadas (exclui 'sem documento' e 'manual atípico')"); put(ws, f"C{e+1}", res["distorcao_quantificada_monetaria"], fmt=N2)
put(ws, f"A{e+2}", "Materialidade global (R$)"); put(ws, f"C{e+2}", "='PT320_Materialidade'!B19", font=grn, fmt=N2)
put(ws, f"A{e+3}", "Quantificada / materialidade global"); put(ws, f"C{e+3}", f"=C{e+1}/C{e+2}", fmt=P1)
put(ws, f"A{e+4}", "Conclusão SIMULADA"); put(ws, f"C{e+4}", f'=IF(C{e+3}>1,"Distorções não corrigidas EXCEDEM a materialidade: opinião modificada, se persistissem","Abaixo da materialidade")')

# ---------- Cobertura ----------
ws = sheet("Cobertura_Normas", "Matriz de cobertura: norma x papel de trabalho (versões em versoes_normas.py e no PDF)", [26, 14, 70])
head(ws, 4, ["Norma (versão consultada, CFC, 20/10/2026)", "Papel de trabalho", "Natureza da execução predominante"])
cov = [("NBC TA Estrutura Conceitual", "PT EC", "Realizado (documental)"), ("NBC TA 200", "PT 200", "Realizado + planejado"), ("NBC TA 210", "PT 210", "Realizado (carta didática)"), ("NBC TA 220", "PT 220", "Planejado"),
       ("NBC TA 230", "PT 230", "Realizado (estrutura do dossiê)"), ("NBC TA 240", "PT 240", "Realizado + simulado (testes de lançamentos)"), ("NBC TA 250", "PT 250", "Realizado (mapeamento) + planejado"), ("NBC TA 260", "PT 260", "Planejado (minuta)"),
       ("NBC TA 265", "PT 265", "Hipóteses x constatações simuladas"), ("NBC TA 300", "PT 300", "Realizado (plano) + cronograma"), ("NBC TA 315", "PT 315", "Realizado com evidência pública"), ("NBC TA 320", "PT 320", "Realizado (cálculo)"),
       ("NBC TA 330", "PT 330", "Planejado + simulado"), ("NBC TA 402", "PT 402", "Planejado"), ("NBC TA 450", "PT 450", "Simulado"), ("NBC TA 500", "PT 500", "Realizado + simulado"),
       ("NBC TA 501", "PT 501", "Realizado (litígios/segmentos) + análise (estoques)"), ("NBC TA 505", "PT 505", "Planejado (modelos; nenhuma solicitação enviada)"), ("NBC TA 510", "PT 510", "Realizado parcial + planejado"),
       ("NBC TA 520", "PT 520", "Realizado (DFP) + simulado"), ("NBC TA 530", "PT 530", "Simulado (base sintética)"), ("NBC TA 540", "PT 540", "Realizado (recálculo) + simulado (sensibilidade)"), ("NBC TA 550", "PT 550", "Realizado (nota 23) + planejado"),
       ("NBC TA 560", "PT 560", "Realizado com evidência pública"), ("NBC TA 570", "PT 570", "Realizado (indicadores públicos)"), ("NBC TA 580", "PT 580", "Minuta didática"), ("NBC TA 600", "PT 600", "Realizado (mapa) + planejado")]
from versoes_normas import VERS
for i, (a, b, c) in enumerate(cov): ws.cell(5 + i, 1, f"{VERS[b][0]} ({VERS[b][1]})").font = blk; ws.cell(5 + i, 2, b).font = blk; ws.cell(5 + i, 3, c).font = blk
wb.save(OUT); print("ok", OUT)
