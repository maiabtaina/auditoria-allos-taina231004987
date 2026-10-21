#!/usr/bin/env python3
"""
02_testes_auditoria.py | Testes de auditoria sobre a BASE SIMULADA (sintética) de Propriedades para Investimento
ALLOS S.A. - exercício 2025 | Preparador: matrícula 231004987 | 20/10/2026
Executa: conciliação (PT 500), testes de população/CAAT (PT 240/330/450), amostragem MUS (PT 530),
comparação erros inseridos x identificados, e analíticos (PT 520). Saída: ../dados/resultados/
"""
import os, json, math
import numpy as np, pandas as pd
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dados")
R = os.path.join(D, "resultados"); os.makedirs(R, exist_ok=True)
SEED = 231004987
rng = np.random.default_rng(SEED)

df = pd.read_csv(os.path.join(D, "base_simulada_ppi_allos_2025.csv.gz"), dtype={"documento_suporte": str}, keep_default_na=False)
reg = pd.read_csv(os.path.join(D, "registro_erros_inseridos.csv"))
for c in ["valor_custo", "depreciacao_acumulada", "mais_valia_liquida", "valor_contabil_liquido", "depreciacao_exercicio_2025"]:
    df[c] = pd.to_numeric(df[c])
df["dt_at"] = pd.to_datetime(df.data_ativacao); df["dt_lc"] = pd.to_datetime(df.data_lancamento)
out = {}

# ---- parâmetros reais (DFP 2025, consolidado, R$ mil) ----
SALDO_DFP = 20_381_666_000.00; LAIR = 1_017_601_000.00; DEP_DFP = 459_233_000.00
MAT_G = 0.05 * LAIR; MAT_PE = 0.75 * MAT_G; MAT_TRIV = 0.05 * MAT_G
out["materialidade"] = dict(global_=MAT_G, execucao=MAT_PE, trivial=MAT_TRIV)

# ---- T1 conciliação ----
tot = df.valor_contabil_liquido.sum(); ef = reg.efeito_no_total_da_base_RS.sum()
out["conciliacao"] = dict(linhas=len(df), vcl_base=round(tot, 2), saldo_dfp=SALDO_DFP, diferenca=round(tot - SALDO_DFP, 2),
                          efeito_erros_inseridos=round(ef, 2), residuo=round(tot - SALDO_DFP - ef, 2))
# identidade
ident = (df.valor_custo - df.depreciacao_acumulada + df.mais_valia_liquida - df.valor_contabil_liquido).abs() > 0.011
out["identidade_vcl_violacoes"] = int(ident.sum())

# ---- recomputo de depreciação do exercício ----
ano = df.dt_at.dt.year; dia = (df.dt_at - pd.to_datetime(ano.astype(str) + "-01-01")).dt.days
idade = (2025.99 - (ano + dia / 365.0)).clip(lower=0)
v = df.vida_util_anos.replace(0, np.nan)
frac = np.where(ano == 2025, (365 - dia) / 365.0, 1.0)
exp_dep = np.where((df.vida_util_anos > 0) & (idade < df.vida_util_anos), df.valor_custo / v * frac, 0.0)
exp_dep = np.nan_to_num(exp_dep); df["dep_esperada"] = np.round(exp_dep, 2)
df["dif_dep"] = (df.depreciacao_exercicio_2025 - df.dep_esperada)

# ---- testes de população (CAAT) ----
flags = {}
flags["DUPLICIDADE"] = df.duplicated(subset=["documento_suporte", "valor_custo", "data_ativacao"], keep="first") & (df.documento_suporte != "")
flags["CORTE (ATIVACAO EM 2026)"] = df.dt_at > pd.Timestamp("2025-12-31")
flags["BAIXADO COM SALDO"] = (df.status == "Baixado") & (df.valor_contabil_liquido > 0)
flags["VCL NEGATIVO"] = df.valor_contabil_liquido < 0
flags["TERRENO DEPRECIADO"] = (df.classe_ativo == "Terreno") & (df.depreciacao_acumulada > 0)
flags["SEM DOCUMENTO SUPORTE"] = df.documento_suporte == ""
flags["DEPRECIACAO INCORRETA"] = df.dif_dep.abs() > np.maximum(1.0, 0.01 * df.dep_esperada)
valid_users = {f"U{u:03d}" for u in range(1, 61)}
flags["LANCAMENTO MANUAL ATIPICO"] = (df.tipo_lancamento == "Manual") & (~df.usuario_lancamento.isin(valid_users)) & (df.dt_lc.dt.dayofweek.isin([5, 6]) | (df.dt_lc == pd.Timestamp("2025-12-31")))
rows = []
for t, m in flags.items():
    ids = set(df.loc[m, "id_registro"]); ins = set(reg.loc[reg.tipo_erro == t, "id_registro"])
    tp = len(ids & ins)
    rows.append(dict(tipo_erro=t, inseridos=len(ins), sinalizados_pelo_teste=len(ids), verdadeiros_positivos=tp,
                     falsos_positivos=len(ids - ins), nao_detectados=len(ins - ids),
                     taxa_deteccao=round(tp / len(ins), 4) if ins else None))
cmp_pop = pd.DataFrame(rows); cmp_pop.to_csv(os.path.join(R, "comparacao_erros_inseridos_x_identificados_populacao.csv"), index=False)
df["n_flags"] = sum(m.astype(int) for m in flags.values())
df.loc[df.n_flags > 0, ["id_registro", "id_shopping", "classe_ativo", "valor_contabil_liquido", "n_flags"]].to_csv(os.path.join(R, "excecoes_populacao.csv"), index=False)
out["testes_populacao"] = cmp_pop.to_dict("records")

# ---- amostragem MUS (PT 530) ----
RF = 3.0  # 95% de confiança, erro esperado zero (Poisson)
pos = df[df.valor_contabil_liquido > 0].copy()
key = pos[pos.valor_contabil_liquido >= MAT_PE]
rest = pos[pos.valor_contabil_liquido < MAT_PE].copy()
neg = df[df.valor_contabil_liquido < 0]
BV = rest.valor_contabil_liquido.sum(); SI = MAT_PE / RF; n_calc = math.ceil(BV / SI)
start = rng.uniform(0, SI)
cum = rest.valor_contabil_liquido.cumsum().values
pts = start + SI * np.arange(int(BV // SI) + 1); pts = pts[pts <= cum[-1]]
idx = np.unique(np.searchsorted(cum, pts, side="left"))
samp = rest.iloc[idx].copy()
out["amostragem"] = dict(metodo="MUS (unidade monetária), seleção sistemática com início aleatório", RF=RF, confianca=0.95,
    erro_tolerável=MAT_PE, populacao_testada_mus=round(BV, 2), intervalo_amostral=round(SI, 2), tamanho_calculado=n_calc,
    itens_selecionados_mus=len(samp), itens_chave_100pct=len(key), itens_negativos_100pct=len(neg), semente=SEED, inicio_aleatorio=round(start, 2))
# avaliação dos itens (procedimento item a item)
def dist_item(r):
    if flags["DUPLICIDADE"][r.name]: return r.valor_contabil_liquido
    if flags["CORTE (ATIVACAO EM 2026)"][r.name]: return r.valor_contabil_liquido
    if flags["BAIXADO COM SALDO"][r.name]: return r.valor_contabil_liquido
    if flags["TERRENO DEPRECIADO"][r.name]: return r.depreciacao_acumulada
    if flags["DEPRECIACAO INCORRETA"][r.name]: return abs(r.dif_dep)
    return 0.0
def excecao(r): return any(flags[t][r.name] for t in flags)
def avaliar(d):
    d = d.copy(); d["excecao"] = [excecao(r) for r in d.itertuples()]
    d["distorcao"] = [dist_item(r) if True else 0 for r in d.itertuples()]
    return d
class _R:  # adaptador p/ acessar por nome de índice
    pass
def avaliar2(d):
    ex, di = [], []
    for ix, r in d.iterrows():
        e = any(bool(flags[t].loc[ix]) for t in flags); ex.append(e)
        x = 0.0
        if flags["DUPLICIDADE"].loc[ix] or flags["CORTE (ATIVACAO EM 2026)"].loc[ix] or flags["BAIXADO COM SALDO"].loc[ix]: x = r.valor_contabil_liquido
        elif flags["TERRENO DEPRECIADO"].loc[ix]: x = r.depreciacao_acumulada
        elif flags["DEPRECIACAO INCORRETA"].loc[ix]: x = abs(r.dif_dep)
        di.append(x)
    d = d.copy(); d["excecao"] = ex; d["distorcao"] = di; return d
samp = avaliar2(samp); key_e = avaliar2(key); neg_e = avaliar2(neg)
samp["taint"] = (samp.distorcao / samp.valor_contabil_liquido).clip(upper=1.0)
errs = samp[samp.distorcao > 0].sort_values("taint", ascending=False)
INC = [1.75, 1.55, 1.46, 1.40, 1.36, 1.33, 1.31, 1.29, 1.28, 1.27]  # incrementos Poisson 95% (Stringer)
inc = [INC[min(i, len(INC) - 1)] for i in range(len(errs))]
precisao_basica = RF * SI
proj = float((errs.taint * SI).sum())
stringer = SI * (RF + float((errs.taint * np.array(inc)).sum())) if len(errs) else RF * SI
out["resultado_amostra"] = dict(itens_com_excecao=int(samp.excecao.sum()), itens_com_distorcao_quantificada=int(len(errs)),
    distorcao_na_amostra=round(float(samp.distorcao.sum()), 2), distorcao_projetada=round(proj, 2), precisao_basica=round(precisao_basica, 2),
    limite_superior_stringer=round(stringer, 2), erro_tolerável=MAT_PE, conclusao_estatistica="LIMITE SUPERIOR > ERRO TOLERÁVEL: população NÃO aceita sem ajuste/ampliação" if stringer > MAT_PE else "Limite superior ≤ erro tolerável")
out["itens_chave"] = dict(qtd=len(key), vcl=round(key.valor_contabil_liquido.sum(), 2), excecoes=int(key_e.excecao.sum()), distorcao=round(float(key_e.distorcao.sum()), 2))
out["itens_negativos"] = dict(qtd=len(neg), vcl=round(neg.valor_contabil_liquido.sum(), 2))
cols = ["id_registro", "id_shopping", "classe_ativo", "valor_contabil_liquido", "excecao", "distorcao"]
samp[cols + ["taint"]].to_csv(os.path.join(R, "amostra_mus_selecionada.csv"), index=False)
key_e[cols].to_csv(os.path.join(R, "itens_chave_100pct.csv"), index=False)
# erros inseridos x identificados via amostra
ins_ids = reg.set_index("id_registro")["tipo_erro"]
in_sample = samp[samp.excecao].id_registro.isin(ins_ids.index)
rs = []
for t in reg.tipo_erro.unique():
    ids = set(reg.loc[reg.tipo_erro == t, "id_registro"])
    rs.append(dict(tipo_erro=t, inseridos=len(ids), selecionados_na_amostra_mus=int(samp.id_registro.isin(ids).sum()),
                   itens_chave_100pct=int(key.id_registro.isin(ids).sum())))
pd.DataFrame(rs).to_csv(os.path.join(R, "comparacao_erros_inseridos_x_amostra.csv"), index=False)
out["amostra_x_erros"] = rs

# ---- PT 450: mapa de distorções (população) ----
dist_pop = df.copy()
mapa = []
for t in reg.tipo_erro.unique():
    s = reg[reg.tipo_erro == t]
    mapa.append(dict(tipo_erro=t, qtd=len(s), distorcao_potencial_total=round(s.distorcao_potencial_RS.sum(), 2),
                     efeito_sobre_saldo_da_base=round(s.efeito_no_total_da_base_RS.sum(), 2)))
mapa = pd.DataFrame(mapa); mapa.to_csv(os.path.join(R, "mapa_distorcoes_PT450.csv"), index=False)
out["mapa_distorcoes"] = mapa.to_dict("records")
out["distorcao_potencial_total"] = round(mapa.distorcao_potencial_total.sum(), 2)
out["distorcao_quantificada_monetaria"] = round(mapa[~mapa.tipo_erro.isin(["SEM DOCUMENTO SUPORTE", "LANCAMENTO MANUAL ATIPICO"])].distorcao_potencial_total.sum(), 2)

# ---- JE test / Benford ----
first = df.valor_custo[df.valor_custo >= 1].astype(int).astype(str).str[0].astype(int)
obs = first.value_counts(normalize=True).reindex(range(1, 10)).fillna(0)
ben = pd.Series({d: math.log10(1 + 1 / d) for d in range(1, 10)})
pd.DataFrame({"digito": range(1, 10), "observado": obs.values, "benford": ben.values}).to_csv(os.path.join(R, "benford_valor_custo.csv"), index=False)
out["benford_mad"] = round(float((obs - ben).abs().mean()), 5)

# ---- PT 520: analíticos ----
dep_base = df.depreciacao_exercicio_2025.sum(); dep_exp = df.dep_esperada.sum()
out["analiticos"] = dict(dep_exercicio_base=round(dep_base, 2), dep_esperada_recalculada=round(dep_exp, 2),
    dep_dfp_propriedades=DEP_DFP, razao_base_dfp=round(dep_base / DEP_DFP, 4),
    var_ppi_2025_2024=round(20_381_666 / 20_700_140 - 1, 5),
    roll_forward=dict(saldo_ini=20_700_140, adicoes_liquidas=-91_304 - 5_576 + 176_577 + 4_164, baixas=-(53_881 + 136_703 + 150_117 + 61_634), saldo_fim=20_700_140 - 91_304 - 5_576 + 176_577 + 4_164 - (53_881 + 136_703 + 150_117 + 61_634)))
out["perfil"] = dict(vcl_por_classe={k: round(v, 2) for k, v in df.groupby("classe_ativo").valor_contabil_liquido.sum().items()},
                     n_shoppings=int(df.id_shopping.nunique()), vcl_max=round(df.valor_contabil_liquido.max(), 2), mediana=round(df.valor_contabil_liquido.median(), 2))
json.dump(out, open(os.path.join(R, "resultados.json"), "w"), ensure_ascii=False, indent=2, default=float)
print(json.dumps({k: out[k] for k in ["materialidade", "conciliacao", "amostragem", "resultado_amostra", "itens_chave", "itens_negativos", "analiticos", "distorcao_potencial_total", "distorcao_quantificada_monetaria", "benford_mad"]}, ensure_ascii=False, indent=1, default=float))
print(cmp_pop.to_string()); print(pd.DataFrame(rs).to_string()); print(mapa.to_string())
