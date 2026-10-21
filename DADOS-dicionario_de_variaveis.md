# Dicionário de variáveis - base SINTÉTICA de Propriedades para Investimento (ALLOS 2025)

Matrícula 231004987. DADOS SINTÉTICOS, não são registros reais da Allos.

| Variável | Tipo | Descrição |
|---|---|---|
| id_registro | texto | Identificador único do registro (PPI-0000001...). Os 150 duplicados inseridos têm ids novos. |
| id_shopping | texto | Código sintético do shopping center (SHP-01 a SHP-45; 45 = shoppings com participação, F1 p.3). Não corresponde a nenhum shopping real. |
| participacao_pct | número | Fração ideal sintética do ativo detida (%). |
| classe_ativo | texto | Terreno, Edificações, Instalações, Benfeitorias e acabamentos, Equipamentos e sistemas, Obras em andamento, Direito de uso. |
| origem | texto | Aquisição/construção própria, Combinação de negócios (com mais-valia) ou Adição 2025. |
| data_ativacao | data AAAA-MM-DD | Data em que o ativo entrou em uso. |
| vida_util_anos | inteiro | Vida útil sintética (0 = não depreciável: terreno e obra em andamento). |
| valor_custo | R$ | Custo de aquisição/construção. |
| depreciacao_acumulada | R$ | Depreciação acumulada até 31/12/2025. |
| mais_valia_liquida | R$ | Mais-valia líquida de combinação de negócios. |
| valor_contabil_liquido | R$ | Custo - depreciação acumulada + mais-valia líquida (identidade testada). |
| depreciacao_exercicio_2025 | R$ | Depreciação do exercício; recalculada como custo/vida útil, proporcional aos dias em 2025 para adições do ano. |
| status | texto | Em operação, Em desenvolvimento ou Baixado. |
| documento_suporte | texto | Referência sintética de NF, laudo, escritura ou contrato (vazio = sem suporte). |
| tipo_lancamento | texto | Automático ou Manual. |
| usuario_lancamento | texto | Usuário sintético (U001-U060 válidos; U099 fora do cadastro). |
| data_lancamento | data | Data de lançamento contábil. |
