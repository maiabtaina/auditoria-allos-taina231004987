#!/usr/bin/env python3
"""
01_gerar_base.py  |  Trabalho individual de auditoria - ALLOS S.A. (ALOS3), exercício 2025
Preparador: matrícula 231004987  |  Data: 20/10/2026

DADOS SINTÉTICOS. Nenhuma linha gerada aqui é registro real da Allos.
Os TOTAIS-ALVO vêm das demonstrações financeiras reais de 31/12/2025 (nota explicativa nº 11,
consolidado, R$ mil) e servem apenas para calibrar a simulação:
  Custo ...................... 10.800.757
  Depreciação acumulada ......  (2.711.228)
  Mais-valia líquida ......... 12.292.137
  Total propriedades p/ invest. 20.381.666   (terrenos 70.566 + shopping centers 20.311.100)
  Adições de 2025 (custo) .... 361.710 + 5.124 + 116.653 + 10.130 = 493.617

Semente = matrícula (231004987) => base 100% reprodutível.
Uso:  python 01_gerar_base.py [--n 520000] [--out ../dados]
"""
import argparse, os
import numpy as np, pandas as pd

SEED = 231004987
ap = argparse.ArgumentParser()
ap.add_argument("--n", type=int, default=520_000)
ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dados"))
args = ap.parse_args()
N, OUT = args.n, args.out
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(SEED)

K = 1000 * 100  # R$ mil -> centavos
T_CUSTO_TOTAL = 10_800_757 * K
T_TERRENO     = 70_566 * K
T_DEP         = 2_711_228 * K
T_MV          = 12_292_137 * K
T_ADIC_2025   = 493_617 * K
T_VCL         = 20_381_666 * K
T_CUSTO_SHOP  = T_CUSTO_TOTAL - T_TERRENO

classes = ["Terreno", "Edificações", "Instalações", "Benfeitorias e acabamentos",
           "Equipamentos e sistemas", "Obras em andamento", "Direito de uso"]
p_cls   = np.array([0.004, 0.40, 0.23, 0.20, 0.12, 0.03, 0.016]); p_cls /= p_cls.sum()
mult    = {"Terreno": 1, "Edificações": 4.0, "Instalações": 1.6, "Benfeitorias e acabamentos": 1.0,
           "Equipamentos e sistemas": 0.5, "Obras em andamento": 2.0, "Direito de uso": 0.8}
vidas   = {"Edificações": [40, 50], "Instalações": [15, 20], "Benfeitorias e acabamentos": [10, 15, 25],
           "Equipamentos e sistemas": [5, 10], "Direito de uso": [10, 20, 30]}
n_shop  = 45
shop_w  = rng.lognormal(0, 0.6, n_shop); shop_w /= shop_w.sum()
shop_pct = rng.choice([100, 100, 100, 90, 75, 70, 65, 60.5, 50, 46.7, 40, 35, 30], n_shop)

cls = rng.choice(classes, N, p=p_cls)
shop_idx = rng.choice(n_shop, N, p=shop_w)
is_terr = cls == "Terreno"
nt = ~is_terr

w = rng.lognormal(0, 1.9, N) * np.vectorize(mult.get)(cls)
cost = np.zeros(N, dtype=np.int64)
cost[nt] = np.floor(w[nt] / w[nt].sum() * T_CUSTO_SHOP).astype(np.int64)
cost[is_terr] = np.floor(w[is_terr] / w[is_terr].sum() * T_TERRENO).astype(np.int64)
cost[np.argmax(np.where(nt, cost, 0))] += T_CUSTO_SHOP - cost[nt].sum()
cost[np.argmax(np.where(is_terr, cost, 0))] += T_TERRENO - cost[is_terr].sum()

anos = np.arange(1975, 2025)
pa = np.interp(anos, [1975, 1995, 2005, 2012, 2019, 2024], [0.2, 0.6, 1.4, 2.2, 1.5, 1.0]); pa /= pa.sum()
ano = rng.choice(anos, N, p=pa)
cand = np.where(nt & (cls != "Direito de uso"))[0]; rng.shuffle(cand)
sel = cand[np.cumsum(cost[cand]) <= T_ADIC_2025]
ano[sel] = 2025
is25 = ano == 2025
dia = rng.integers(0, 365, N)
data_ativ = pd.to_datetime(ano.astype(str) + "-01-01") + pd.to_timedelta(dia, unit="D")

vida = np.zeros(N, dtype=int)
for c, v in vidas.items():
    m = cls == c; vida[m] = rng.choice(v, m.sum())
idade = np.clip(2025.99 - (ano + dia / 365.0), 0, None)

dep_mask = (vida > 0)
rate = np.where(dep_mask, np.minimum(0.95, idade / np.where(vida > 0, vida, 1)) * rng.uniform(0.85, 1.0, N), 0.0)
base_dep = cost * rate
dep = np.floor(base_dep * (T_DEP / base_dep.sum())).astype(np.int64)
for _ in range(10):
    cap = (cost * 0.97).astype(np.int64)
    dep = np.minimum(dep, cap)
    room = np.where(dep_mask, cap - dep, 0)
    need = T_DEP - dep.sum()
    if abs(need) < 1000: break
    dep += np.floor(room / room.sum() * need).astype(np.int64)
dep[np.argmax(np.where(dep_mask, cost - dep, 0))] += T_DEP - dep.sum()

origem = np.where(is25, "Adição 2025", np.where(rng.random(N) < 0.55, "Combinação de negócios", "Aquisição/construção própria"))
origem = np.where(is_terr | (cls == "Direito de uso"), "Aquisição/construção própria", origem)
mvw = np.where(origem == "Combinação de negócios", cost * rng.uniform(0.5, 3.0, N), 0.0)
mv = np.floor(mvw / mvw.sum() * T_MV).astype(np.int64)
mv[np.argmax(mv)] += T_MV - mv.sum()

vcl = cost - dep + mv
assert vcl.sum() == T_VCL, (vcl.sum(), T_VCL)

frac = np.where(is25, (365 - dia) / 365.0, 1.0)
dep_ex = np.where(dep_mask & (idade < vida), cost / np.where(vida > 0, vida, 1) * frac, 0.0)
dep_ex = np.round(dep_ex / 100.0, 2)

atraso = np.where(rng.random(N) < 0.82, rng.integers(0, 6, N), rng.integers(0, 45, N))
data_lanc = pd.Series(data_ativ + pd.to_timedelta(atraso, unit="D"))
data_lanc = data_lanc.where(data_lanc <= pd.Timestamp("2025-12-31"), pd.Timestamp("2025-12-30"))
dow = data_lanc.dt.dayofweek.values
data_lanc = data_lanc + pd.to_timedelta(np.where(dow == 5, 2, np.where(dow == 6, 1, 0)), unit="D")
data_lanc = data_lanc.where(data_lanc <= pd.Timestamp("2025-12-31"), pd.Timestamp("2025-12-30"))
dow = data_lanc.dt.dayofweek.values
data_lanc = data_lanc - pd.to_timedelta(np.where(dow >= 5, dow - 4, 0), unit="D")
tipo = np.where(rng.random(N) < 0.18, "Manual", "Automático")
users = np.array([f"U{u:03d}" for u in range(1, 61)])
usuario = np.where(tipo == "Manual", rng.choice(users[:15], N), rng.choice(users, N))
pref = np.where(origem == "Combinação de negócios", "LAUDO", np.where(cls == "Direito de uso", "CTR", np.where(is_terr, "ESC", "NF")))
doc = np.array([f"{p}-{i:07d}" for p, i in zip(pref, rng.integers(1, 9_999_999, N))])
status = np.where(cls == "Obras em andamento", "Em desenvolvimento", "Em operação")

df = pd.DataFrame({
    "id_registro": [f"PPI-{i:07d}" for i in range(1, N + 1)],
    "id_shopping": [f"SHP-{s + 1:02d}" for s in shop_idx],
    "participacao_pct": shop_pct[shop_idx],
    "classe_ativo": cls, "origem": origem,
    "data_ativacao": pd.Series(data_ativ).dt.strftime("%Y-%m-%d").values,
    "vida_util_anos": vida,
    "valor_custo": cost / 100.0, "depreciacao_acumulada": dep / 100.0, "mais_valia_liquida": mv / 100.0,
    "valor_contabil_liquido": vcl / 100.0, "depreciacao_exercicio_2025": dep_ex,
    "status": status, "documento_suporte": doc, "tipo_lancamento": tipo, "usuario_lancamento": usuario,
    "data_lancamento": data_lanc.dt.strftime("%Y-%m-%d").values,
})
clean_total = round(df["valor_contabil_liquido"].sum(), 2)

# ===================== INSERÇÃO DE ERROS (com registro) =====================
reg = []
def log(tipo_e, rid, campo, vo, vi, ef_total, dist, desc):
    reg.append(dict(id_erro=f"E{len(reg)+1:04d}", tipo_erro=tipo_e, id_registro=rid, campo_alterado=campo,
                    valor_original=vo, valor_inserido=vi, efeito_no_total_da_base_RS=round(float(ef_total), 2),
                    distorcao_potencial_RS=round(float(dist), 2), descricao=desc))
used = set()
def pick_u(mask, k):
    idx = np.where(mask)[0]
    cand_ = [i for i in rng.permutation(idx) if i not in used][:k]
    used.update(cand_); return np.array(cand_)
C = {c: df.columns.get_loc(c) for c in df.columns}
mid = ((df.valor_contabil_liquido > 20_000) & (df.valor_contabil_liquido < 5_000_000)).values
rows = df.copy()

dup = pick_u(mid, 150); new = []
for j, i in enumerate(dup):
    r = df.iloc[i].copy(); r["id_registro"] = f"PPI-{N + j + 1:07d}"; new.append(r)
    log("DUPLICIDADE", r["id_registro"], "registro inteiro", df.iloc[i]["id_registro"], "cópia", r["valor_contabil_liquido"], r["valor_contabil_liquido"], "Registro duplicado de ativo existente (mesmos atributos, novo id)")
for i in pick_u((df.data_ativacao >= "2025-01-01").values & mid, 120):
    d = (pd.Timestamp("2026-01-05") + pd.Timedelta(days=int(rng.integers(0, 60)))).strftime("%Y-%m-%d")
    log("CORTE (ATIVACAO EM 2026)", df.iloc[i]["id_registro"], "data_ativacao", df.iloc[i]["data_ativacao"], d, 0.0, df.iloc[i]["valor_contabil_liquido"], "Ativo com data de ativação posterior a 31/12/2025 incluído no saldo")
    rows.iat[i, C["data_ativacao"]] = d
for i in pick_u((df.depreciacao_exercicio_2025 > 100).values, 200):
    fct = float(rng.choice([0.4, 0.5, 1.6, 1.8])); de = df.iloc[i]["depreciacao_exercicio_2025"]; delta = (fct - 1) * de
    rows.iat[i, C["depreciacao_exercicio_2025"]] = round(de * fct, 2)
    rows.iat[i, C["depreciacao_acumulada"]] = round(df.iloc[i]["depreciacao_acumulada"] + delta, 2)
    rows.iat[i, C["valor_contabil_liquido"]] = round(df.iloc[i]["valor_contabil_liquido"] - delta, 2)
    log("DEPRECIACAO INCORRETA", df.iloc[i]["id_registro"], "depreciacao_exercicio_2025 e acumulada", de, round(de * fct, 2), -delta, abs(delta), f"Depreciação do exercício alterada por fator {fct}")
for i in pick_u(mid, 80):
    rows.iat[i, C["status"]] = "Baixado"
    log("BAIXADO COM SALDO", df.iloc[i]["id_registro"], "status", "Em operação", "Baixado", 0.0, df.iloc[i]["valor_contabil_liquido"], "Ativo marcado como baixado mantido com valor contábil positivo")
for i in pick_u(((df.valor_custo > 50_000) & (df.classe_ativo != "Terreno")).values, 60):
    nd = round((df.iloc[i]["valor_custo"] + df.iloc[i]["mais_valia_liquida"]) * 1.1, 2); old = df.iloc[i]["valor_contabil_liquido"]
    nv = round(df.iloc[i]["valor_custo"] - nd + df.iloc[i]["mais_valia_liquida"], 2)
    rows.iat[i, C["depreciacao_acumulada"]] = nd; rows.iat[i, C["valor_contabil_liquido"]] = nv
    log("VCL NEGATIVO", df.iloc[i]["id_registro"], "depreciacao_acumulada", df.iloc[i]["depreciacao_acumulada"], nd, nv - old, abs(nv - old), "Depreciação acumulada excede custo + mais-valia")
for i in pick_u((df.classe_ativo == "Terreno").values, 40):
    d = round(df.iloc[i]["valor_custo"] * 0.03, 2); old = df.iloc[i]["valor_contabil_liquido"]
    rows.iat[i, C["depreciacao_acumulada"]] = d; rows.iat[i, C["valor_contabil_liquido"]] = round(old - d, 2)
    log("TERRENO DEPRECIADO", df.iloc[i]["id_registro"], "depreciacao_acumulada", 0.0, d, -d, d, "Terreno não depreciável com depreciação acumulada")
for i in pick_u(mid, 300):
    rows.iat[i, C["documento_suporte"]] = ""
    log("SEM DOCUMENTO SUPORTE", df.iloc[i]["id_registro"], "documento_suporte", df.iloc[i]["documento_suporte"], "", 0.0, df.iloc[i]["valor_contabil_liquido"], "Registro sem referência de documento (deficiência de controle; distorção apenas potencial)")
for i in pick_u(((df.valor_custo > 100_000) & (df.classe_ativo != "Terreno")).values, 90):
    old_c = df.iloc[i]["valor_custo"]; novo = float(round(old_c, -6) or 1_000_000)
    dl_s = "2025-12-28" if rng.random() < 0.5 else "2025-12-31"
    nv = round(novo - df.iloc[i]["depreciacao_acumulada"] + df.iloc[i]["mais_valia_liquida"], 2)
    for c_, v_ in (("tipo_lancamento", "Manual"), ("usuario_lancamento", "U099"), ("data_lancamento", dl_s), ("valor_custo", novo), ("valor_contabil_liquido", nv)):
        rows.iat[i, C[c_]] = v_
    ef = nv - df.iloc[i]["valor_contabil_liquido"]
    log("LANCAMENTO MANUAL ATIPICO", df.iloc[i]["id_registro"], "valor_custo/tipo/usuário/data", old_c, novo, ef, abs(ef), "Manual, usuário fora do cadastro (U099), domingo/31-12, valor redondo")
rows = pd.concat([rows, pd.DataFrame(new)], ignore_index=True)

rows.to_csv(os.path.join(OUT, "base_simulada_ppi_allos_2025.csv.gz"), index=False, compression="gzip")
regdf = pd.DataFrame(reg); regdf.to_csv(os.path.join(OUT, "registro_erros_inseridos.csv"), index=False)
rows.head(1000).to_csv(os.path.join(OUT, "amostra_primeiras_1000_linhas.csv"), index=False)
final_total = round(rows["valor_contabil_liquido"].sum(), 2)
print(f"Linhas: {len(rows):,} | VCL base limpa: R$ {clean_total:,.2f} | VCL base final: R$ {final_total:,.2f}")
print(f"Saldo DFP 31/12/2025: R$ {T_VCL/100:,.2f} | soma efeitos erros: R$ {regdf.efeito_no_total_da_base_RS.sum():,.2f} | residuo: R$ {final_total-clean_total-regdf.efeito_no_total_da_base_RS.sum():,.2f}")
print("Erros inseridos:", len(regdf), regdf.tipo_erro.value_counts().to_dict())
