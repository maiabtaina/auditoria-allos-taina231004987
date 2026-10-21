# Dossiê de auditoria - ALLOS S.A. (B3: ALOS3) - exercício 2025

**Aluno (identificação por matrícula): 231004987** | Data de preparação: 20/10/2026 | Trabalho individual

> **Exercício didático.** Não é opinião de auditor independente. Nenhuma confirmação, entrevista, inspeção ou acesso a sistemas foi realizado, e nenhuma empresa, auditor, cliente ou fornecedor foi contatado.
> **A base de dados é SINTÉTICA**: calibrada só nos totais reais da nota 11 da Allos; nenhuma linha é registro real.

## Companhia
ALLOS S.A. (ALOS3). Antes: Aliansce Sonae Shopping Centers S.A. (ALSO3, nome de pregão Alianscsonae), da combinação Aliansce + Sonae Sierra (2019). Após a fusão com a BRMalls (2023), nova denominação aprovada em 17/10/2023 e código ALOS3 desde 25/10/2023 (fontes secundárias W7-W9; conferir no Formulário Cadastral/RI). Auditor 2025 (real): Deloitte, relatório de 10/03/2026.

## Conta escolhida para a base simulada
**Propriedades para Investimento**: R$ 20.381.666 mil = 78,4% do ativo consolidado de 31/12/2025 (justificativa no Anexo C do PDF).

## Organização do repositório
| Pasta/arquivo | Conteúdo |
|---|---|
| `dossie/Dossie_Auditoria_ALLOS_2025_matricula_231004987.pdf` | Dossiê: 27 papéis de trabalho (PT EC, 200 a 600), programas por ciclo (Anexo A), erros x exceções (B), base simulada e dicionário (C), conclusão integrada |
| `dados/base_simulada_ppi_allos_2025.csv.gz` | Base sintética, **520.150 linhas** (compactada; ~21 MB) |
| `dados/dicionario_de_variaveis.md` | Dicionário das 17 variáveis |
| `dados/registro_erros_inseridos.csv` | Registro dos 1.040 erros inseridos |
| `dados/resultados/` | Saídas dos testes (exceções, amostra MUS, comparações, mapa de distorções, JSON) |
| `dados/amostra_primeiras_1000_linhas.csv` | Prévia legível da base |
| `codigo/` | `01_gerar_base.py`, `02_testes_auditoria.py`, `03_gerar_planilhas.py`, `04_gerar_dossie_pdf.py`, conteúdo dos PTs |
| `planilhas/papeis_de_trabalho_calculos_allos_2025.xlsx` | Materialidade, conciliação, amostragem, PCE, analíticos, continuidade, distorções, cobertura (fórmulas vivas) |
| `matriz_cobertura_normas.md` | Norma x papel de trabalho |
| `fontes/relacao_fontes.md` | Fontes com URL, data de acesso, documento, página e exercício |

## Como reproduzir
```bash
pip install -r requirements.txt
cd codigo
python 01_gerar_base.py        # gera a base (semente = 231004987) e o registro de erros
python 02_testes_auditoria.py  # conciliação, CAAT, amostragem MUS, comparações
python 03_gerar_planilhas.py   # planilhas (abrir no Excel/LibreOffice para recalcular)
python 04_gerar_dossie_pdf.py  # PDF do dossiê
```
Resultados esperados: 520.150 linhas; soma do valor contábil líquido R$ 20.448.164.979,64 (= saldo DFP R$ 20.381.666.000,00 + efeitos dos erros inseridos R$ 66.498.979,59 + R$ 0,05 de arredondamento).

## Limite de arquivo do GitHub
O `.csv.gz` (~21 MB) cabe no limite de 100 MB por arquivo (e no upload pelo navegador, que aceita até 25 MB). Se não couber, o código reproduz a base: rode `01_gerar_base.py`. Não é necessário link externo: a base compactada cabe no limite do GitHub.

## Versão das normas consultadas
Fonte: portal do CFC, lista *NBC TA de auditoria independente* (https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/), acesso em 20/10/2026. Regra: versão em vigor para o exercício de 2025.

| PT | Norma e versão | Publicação | Observação |
|---|---|---|---|
| PT EC | NBC TA Estrutura Conceitual - Estrutura Conceitual para Trabalhos de Asseguração | DOU 25/11/15 | vigente |
| PT 200 | NBC TA 200 (R1) | DOU 05/09/16 | vigente |
| PT 210 | NBC TA 210 (R1) | DOU 05/09/16 | vigente |
| PT 220 | NBC TA 220 (R3) | DOU 09/12/21 | vigente |
| PT 230 | NBC TA 230 (R1) | DOU 05/09/16 | vigente |
| PT 240 | NBC TA 240 (R1) | DOU 05/09/16 | R1 aplicada ao exercício de 2025. A lista do CFC já mostra a NBC TA 240 (R2), DOU 25/09/26, publicada depois do exercício e do relatório (10/03/2026); sua vigência não foi lida e ela não foi aplicada |
| PT 250 | NBC TA 250 | DOU 14/02/19 | vigente |
| PT 260 | NBC TA 260 (R2) | DOU 04/07/16 | vigente |
| PT 265 | NBC TA 265 | Res. CFC 1.210/09 | vigente |
| PT 300 | NBC TA 300 (R1) | DOU 05/09/16 | vigente |
| PT 315 | NBC TA 315 (R2) | DOU 02/09/21 | vigente |
| PT 320 | NBC TA 320 (R1) | DOU 05/09/16 | vigente |
| PT 330 | NBC TA 330 (R1) | DOU 05/09/16 | vigente |
| PT 402 | NBC TA 402 | Res. CFC 1.215/09 | vigente |
| PT 450 | NBC TA 450 (R1) | DOU 05/09/16 | vigente |
| PT 500 | NBC TA 500 (R1) | DOU 05/09/16 | vigente |
| PT 501 | NBC TA 501 | Res. CFC 1.218/09 | vigente |
| PT 505 | NBC TA 505 | Res. CFC 1.219/09 | vigente |
| PT 510 | NBC TA 510 (R1) | DOU 05/09/16 | vigente |
| PT 520 | NBC TA 520 | Res. CFC 1.221/09 | vigente |
| PT 530 | NBC TA 530 | Res. CFC 1.222/09 | vigente |
| PT 540 | NBC TA 540 (R2) | DOU 23/10/19 | vigente |
| PT 550 | NBC TA 550 | Res. CFC 1.224/09 | vigente |
| PT 560 | NBC TA 560 (R1) | DOU 05/09/16 | vigente |
| PT 570 | NBC TA 570 (versão anterior à R1) | R1: DOU 25/09/26 | A lista do CFC mostra a NBC TA 570 (R1), DOU 25/09/26, posterior ao exercício e ao relatório de 10/03/2026; foi aplicada a versão que antecedia a R1 (o texto dela não consta da lista consultada) - inferência a registrar |
| PT 580 | NBC TA 580 (R1) | DOU 05/09/16 | vigente |
| PT 600 | NBC TA 600 (R2) | DOU 06/12/23 | vigente |

Itens das normas indicados por tema; a numeração de parágrafos não foi incluída (textos integrais não lidos).

## Limitações
Somente informação pública; base sintética; sem revisão independente; expectativa de reajuste de 4% no PT 520 é premissa do aluno.
