# Dossiê de auditoria - ALLOS S.A. (B3: ALOS3) - exercício 2025

**Aluno (identificação por matrícula): 231004987** | Data de preparação: 20/10/2026 | Trabalho individual

> **Exercício didático.** Não é opinião de auditor independente. Nenhuma confirmação, entrevista, inspeção ou acesso a sistemas foi realizado, e nenhuma empresa, auditor, cliente ou fornecedor foi contatado.
> **A base de dados é SINTÉTICA**: calibrada só nos totais reais da nota 11 da Allos. Nenhuma linha é registro real.

## Companhia
ALLOS S.A. (ALOS3). Antes: Aliansce Sonae Shopping Centers S.A. (ALSO3, nome de pregão Alianscsonae), da combinação Aliansce + Sonae Sierra (2019). Após a fusão com a BRMalls (2023), a nova denominação foi aprovada em 17/10/2023 e o código ALOS3 vale desde 25/10/2023 (fontes secundárias W7 a W9 em `fontes/relacao_fontes.md`; conferir no Formulário Cadastral/RI). Auditor de 2025 (real): Deloitte, relatório de 10/03/2026.

## Conta escolhida para a base simulada
**Propriedades para Investimento**: R$ 20.381.666 mil = 78,4% do ativo consolidado de 31/12/2025. A justificativa está no Anexo C do PDF.

## Organização do repositório

| Pasta/arquivo | Conteúdo |
|---|---|
| `dossie/Dossie_Auditoria_ALLOS_2025_matricula_231004987.pdf` | Dossiê com os 27 papéis de trabalho (PT EC e NBC TA 200 a 600), programas de auditoria por ciclo (Anexo A), erros inseridos x exceções (Anexo B), base simulada e dicionário (Anexo C) e conclusão integrada |
| **Base simulada [(link de download)](https://docs.google.com/spreadsheets/d/12iMWTPEbafmdAmDSBqA2m5j6MGhMTB54SD_PMXB4CcA/edit?usp=sharing)** | **520.150 linhas, 17 colunas: [[COLE AQUI O SEU LINK]](https://docs.google.com/spreadsheets/d/12iMWTPEbafmdAmDSBqA2m5j6MGhMTB54SD_PMXB4CcA/edit?usp=sharing)** (fora do repositório por causa do limite de tamanho do GitHub) |
| `dados/dicionario_de_variaveis.md` | Dicionário das 17 variáveis da base |
| `dados/registro_erros_inseridos.csv` | Registro dos 1.040 erros inseridos de propósito |
| `dados/amostra_primeiras_1000_linhas.csv` | Prévia das 1.000 primeiras linhas da base |
| `dados/resultados/` | Saídas dos testes: exceções, amostra MUS, comparações, mapa de distorções e JSON de resultados |
| `codigo/` | `01_gerar_base.py`, `02_testes_auditoria.py`, `03_gerar_planilhas.py`, `04_gerar_dossie_pdf.py` e arquivos de conteúdo dos papéis de trabalho |
| `planilhas/papeis_de_trabalho_calculos_allos_2025.xlsx` | Materialidade, conciliação, amostragem, PCE, analíticos, continuidade, distorções e cobertura (com fórmulas) |
| `matriz_cobertura_normas.md` | Norma x papel de trabalho, com a versão de cada norma |
| `fontes/relacao_fontes.md` | Fontes com endereço, data de acesso, documento, página e exercício |
| `requirements.txt` e `run_all.sh` | Bibliotecas e comando para rodar tudo |

## Base simulada: link de download

A base sintética (520.150 linhas) é grande para o limite de upload do GitHub (25 MB pelo navegador). Por isso, conforme o enunciado, ela está disponível por link de download:

**[COLE AQUI O SEU LINK]**

- Conferência: a soma da coluna `valor_contabil_liquido` é **R$ 20.448.164.979,64**.
- Os dados são **sintéticos**. Não são registros reais da Allos.
- O código em `codigo/01_gerar_base.py` (semente = matrícula 231004987) recria exatamente a mesma base.

## Como reproduzir
```bash
pip install -r requirements.txt
cd codigo
python 01_gerar_base.py        # gera a base (semente = 231004987) e o registro de erros, na pasta dados/
python 02_testes_auditoria.py  # conciliação, testes na população, amostragem MUS e comparações
python 03_gerar_planilhas.py   # planilha de cálculos (abrir no Excel ou LibreOffice)
python 04_gerar_dossie_pdf.py  # PDF do dossiê
```
Resultados esperados: 520.150 linhas e soma do valor contábil líquido de R$ 20.448.164.979,64. Esse valor é o saldo da DFP (R$ 20.381.666.000,00) mais os efeitos dos erros inseridos (R$ 66.498.979,59) e R$ 0,05 de arredondamento.

## Versão das normas consultadas
Fonte: portal do CFC, lista *NBC TA de auditoria independente* (https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/), acesso em 20/10/2026. Regra: versão em vigor para o exercício de 2025.

| PT | Norma e versão | Publicação | Observação |
|---|---|---|---|
| PT EC | NBC TA Estrutura Conceitual | DOU 25/11/15 | vigente |
| PT 200 | NBC TA 200 (R1) | DOU 05/09/16 | vigente |
| PT 210 | NBC TA 210 (R1) | DOU 05/09/16 | vigente |
| PT 220 | NBC TA 220 (R3) | DOU 09/12/21 | vigente |
| PT 230 | NBC TA 230 (R1) | DOU 05/09/16 | vigente |
| PT 240 | NBC TA 240 (R1) | DOU 05/09/16 | R1 aplicada ao exercício de 2025. A lista do CFC já mostra a R2 (DOU 25/09/26), posterior ao exercício e ao relatório de 10/03/2026; sua vigência não foi lida e ela não foi aplicada |
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
| PT 570 | NBC TA 570 (versão anterior à R1) | R1: DOU 25/09/26 | A lista do CFC mostra a R1, posterior ao exercício e ao relatório; foi aplicada a versão que antecedia a R1 (texto não consta da lista consultada). Inferência registrada |
| PT 580 | NBC TA 580 (R1) | DOU 05/09/16 | vigente |
| PT 600 | NBC TA 600 (R2) | DOU 06/12/23 | vigente |

Os itens das normas estão indicados por tema. A numeração de parágrafos não foi incluída, porque os textos integrais das normas não foram lidos.

## Limitações
Somente informação pública; base sintética; sem revisão independente; a expectativa de reajuste de 4% no PT 520 é premissa do aluno; fontes secundárias (imprensa e analistas) têm baixa confiabilidade.
