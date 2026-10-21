# -*- coding: utf-8 -*-
# Conteúdo dos papéis de trabalho (parte A). Tags: [RP]=Realizado com evidência pública; [PL]=Planejado por falta de acesso; [SM]=Simulado (dados sintéticos)
# Fontes: F1=PDF 98 p. (comentário de desempenho + DFs + notas + relatório do auditor Deloitte, 10/03/2026); F2=Relatório de Resultados 4T25 + ITR 1T25/2T25 (central de resultados do RI);
# F3=Publicação legal Valor 18/03/2026; W1..W6 = fontes web (ver fontes/relacao_fontes.md). Páginas de F1 = página do PDF.
PTS = []
def pt(**k): PTS.append(k)

pt(cod="PT EC", titulo="Estrutura Conceitual para trabalhos de asseguração", norma="NBC TA Estrutura Conceitual (itens sobre elementos do trabalho, nível de asseguração, evidência e relatório)",
 objetivo="Caracterizar o trabalho, usuários, objeto, critérios, responsabilidades, evidência e nível de asseguração; diferenciar auditoria de outros trabalhos de asseguração. Objeto: demonstrações contábeis individuais e consolidadas da ALLOS S.A. em 31/12/2025.",
 afirmacoes="Não se aplicam afirmações por conta; o papel enquadra o trabalho. Risco: confundir este dossiê didático com um trabalho de asseguração real ou com opinião independente.",
 pop="Fontes: F1 p.10-14 (relatório do auditor Deloitte) e p.15-23 (DFs). Critério de enquadramento: elementos do trabalho de asseguração (três partes, objeto, critérios, evidência, relatório).",
 proc=[("RP","Identificar as três partes na auditoria REAL: auditor (Deloitte Touche Tohmatsu), parte responsável (Diretoria da ALLOS, F1 p.13), usuários previstos (acionistas e administradores, F1 p.10)."),
       ("RP","Identificar objeto e critérios: demonstrações financeiras individuais/consolidadas; práticas contábeis adotadas no Brasil e IFRS Accounting Standards (F1 p.10)."),
       ("RP","Identificar nível: asseguração razoável (F1 p.13: 'segurança razoável é um alto nível de segurança, mas não uma garantia')."),
       ("RP","Comparar com outros trabalhos: revisão limitada de ITR (asseguração limitada; existe nas ITRs de 1T25/2T25, F2), procedimentos previamente acordados e compilação (sem asseguração)."),
       ("SM","Definir o status deste dossiê: exercício didático, sem acesso à entidade, sem contratação e sem emissão de opinião; usa dados públicos e uma base SINTÉTICA.")],
 evid="F1 p.10-14; F2 (relatórios de revisão das ITRs); PT 200, PT 210, PT 500.",
 res="Quadro comparativo: AUDITORIA = razoável, opinião positiva, evidência extensa (testes de controles/substantivos); REVISÃO LIMITADA = limitada, conclusão negativa, principalmente indagação e analíticos; AGREED-UPON = sem asseguração, relata achados factuais; COMPILAÇÃO = sem asseguração. Conclusão: o trabalho do aluno é um EXERCÍCIO de aplicação das normas; não constitui trabalho de asseguração. Limitação: sem contratação, sem evidência obtida da entidade, sem relatório assinado.")

pt(cod="PT 200", titulo="Objetivos gerais do auditor e condução da auditoria", norma="NBC TA 200 (itens sobre objetivos gerais, ética, ceticismo, julgamento profissional, risco de auditoria, segurança razoável)",
 objetivo="Documentar ética, independência, ceticismo, julgamento profissional, risco de auditoria e condições para obter segurança razoável.",
 afirmacoes="Risco de auditoria = risco de distorção relevante (inerente x controle) x risco de detecção. Riscos ao trabalho: pressão de prazo, uso de ferramenta de IA, ausência de acesso à entidade.",
 pop="Fontes: F1 p.10 (declaração de independência do auditor real), F1 'Relacionamento com auditores externos' (Relatório da Administração, F1 p.6), código de ética profissional.",
 proc=[("RP","Registrar que a Deloitte declara independência segundo o Código de Ética Profissional do Contador e normas do CFC para entidades de interesse público (F1 p.10)."),
       ("RP","Registrar serviços não-auditoria divulgados no Relatório da Administração: revisão de qualidade (quality assurance) da adoção do IFRS S1/S2, honorários de cerca de R$ 119 mil (F1 p.6, seção Relacionamento com Auditores Externos; a companhia concluiu não haver conflito de interesse ou perda de independência). Avaliar ameaça de autorrevisão/interesse como baixa pela natureza e valor, conforme avaliação da própria administração (conferir texto)."),
       ("PL","Declaração de independência do aluno: confirmar ausência de investimento em ALOS3, vínculo com a companhia ou conflito. NÃO CONFIRMADO neste dossiê; o aluno deve declarar por conta própria."),
       ("SM","Ceticismo: tratar as asserções da administração e as fontes secundárias (W1-W5) como não confiáveis até corroboração com F1; registrar divergências em PT 500."),
       ("SM","Julgamento: decisões documentadas (base de materialidade em PT 320; conta de maior materialidade em PT 500; amostragem em PT 530).")],
 evid="F1 p.10-14; PT 220, PT 300, PT 320, PT 500.",
 res="Modelo de risco aplicado: RA = RDR x RD. RDR (inerente x controle) avaliado como ALTO em receita de aluguel (linearização) e PPI (valor recuperável) com base nos PAAs do auditor real (F1 p.11-12) e na complexidade das notas; logo, RD deve ser baixo (mais testes). Segurança razoável exige evidência suficiente e apropriada, que NÃO é atingível aqui por falta de acesso: limitação central do trabalho.")

pt(cod="PT 210", titulo="Termos do trabalho de auditoria (carta de contratação didática)", norma="NBC TA 210 (itens sobre precondições, concordância sobre os termos, carta de contratação)",
 objetivo="Preparar carta de contratação DIDÁTICA e avaliar as precondições para a auditoria das demonstrações de 31/12/2025.",
 afirmacoes="Risco: aceitar trabalho sem estrutura de relatório aceitável, sem acesso à informação ou sem reconhecimento de responsabilidades pela administração.",
 pop="Fontes: F1 p.10 (estrutura de relatório e base contábil), F1 p.13 (responsabilidades). Critério: precondições (base contábil aceitável; concordância da administração).",
 proc=[("RP","Base contábil: CPC/IFRS Accounting Standards (F1 p.10) = estrutura aplicável aceitável para entidade de interesse público."),
       ("PL","Obter reconhecimento formal da Diretoria sobre elaboração das DFs, controle interno e acesso irrestrito. Não obtido (nenhum contato com a companhia, conforme regra do trabalho)."),
       ("SM","Minuta da carta (ver abaixo), sem assinatura e sem envio.")],
 evid="F1 p.10, p.13; PT EC, PT 220, PT 580.",
 res="MINUTA (didática, NÃO enviada e NÃO assinada): 'À Diretoria da ALLOS S.A. Objetivo: auditar as DFs individuais e consolidadas do exercício findo em 31/12/2025 e emitir relatório com opinião, PAAs e outros assuntos. Alcance: balanço, DRE, DRA, DMPL, DFC, DVA e notas, segundo as NBC TA. Responsabilidades da Diretoria: elaboração conforme CPC/IFRS, controles internos, acesso integral a registros, representações formais por escrito. Responsabilidades do auditor: segurança razoável; julgamento e ceticismo; comunicação com a governança. Relatório: estrutura da NBC TA 700/701 (opinião, base, PAAs, outros assuntos, responsabilidades). Limitação: honorários, prazos e equipe fixados somente em contrato real.' Conclusão: precondições documentais atendidas em F1; as relativas à administração ficam PLANEJADAS.")

pt(cod="PT 220", titulo="Gestão da qualidade da auditoria", norma="NBC TA 220 (itens sobre direção, supervisão, revisão, consultas, recursos, conflitos)",
 objetivo="Planejar direção, supervisão, revisão, consultas e recursos; documentar conflitos e riscos à qualidade.",
 afirmacoes="Risco à qualidade: preparador único, cronograma de 5 dias, evidência somente pública, uso de IA, ausência de revisor independente.",
 pop="Equipe didática: 1 preparador (matrícula 231004987). Não são atribuídas tarefas a pessoas reais.",
 proc=[("PL","Direção: papéis hipotéticos em trabalho real (sócio responsável, gerente, sênior, assistentes, especialista em avaliação de ativos, especialista em TI)."),
       ("PL","Supervisão e revisão: revisão de cada PT pelo nível superior antes da conclusão; campo de revisão existe em todos os PTs e está EM BRANCO."),
       ("PL","Consultas: matérias de julgamento (impairment, linearização de receita, covenants) levadas a consulta técnica."),
       ("RP","Conflitos: nenhum identificado em fontes públicas; independência do aluno é declaração a prestar pelo aluno (PT 200)."),
       ("SM","Registro de risco à qualidade com resposta: (i) conferir toda cifra real contra F1; (ii) separar real x sintético em arquivos distintos; (iii) reproduzir os testes por script com semente fixa.")],
 evid="PT 200, PT 230, PT 300; README.",
 res="Riscos à qualidade identificados e respondidos conforme acima. Revisão por terceiros NÃO ocorreu e NÃO é simulada. Conclusão: a qualidade fica limitada pela ausência de revisão independente; recomenda-se que o aluno revise integralmente os números antes de entregar.")

pt(cod="PT 230", titulo="Documentação de auditoria", norma="NBC TA 230 (itens sobre forma, conteúdo, extensão, montagem e guarda do arquivo)",
 objetivo="Criar índice, convenção de códigos, referências cruzadas, controle de versões e procedimentos de montagem e guarda.",
 afirmacoes="Risco: documentação insuficiente para que um auditor experiente, sem vínculo, entenda natureza, época, extensão e conclusões.",
 pop="Todos os 27 papéis deste dossiê e arquivos do repositório GitHub.",
 proc=[("RP","Convenção: PT = papel de trabalho; PT [norma] = papel da NBC TA correspondente; F = fonte documental; W = fonte web; [RP]/[PL]/[SM] = classificação do procedimento; 'ref.' = referência cruzada."),
       ("RP","Índice e matriz de cobertura: ver Seção 1 do PDF e planilha Cobertura_Normas."),
       ("RP","Controle de versões: v1.0 de 20/10/2026 (preparação). Alterações subsequentes devem ser registradas no histórico do Git (commit) com data."),
       ("PL","Montagem e guarda: arquivo final fechado e protegido; prazo de montagem e de guarda conforme a NBC TA 230 (R1) (conferir o prazo no texto da norma); acesso restrito."),
       ("SM","Reprodutibilidade: todos os cálculos sintéticos vêm de scripts com semente 231004987.")],
 evid="README; planilha papeis_de_trabalho_calculos_allos_2025.xlsx; fontes/relacao_fontes.md.",
 res="Estrutura completa; cada PT cita fontes, páginas e referências cruzadas. Limitação: a guarda e confidencialidade reais não se aplicam a exercício didático.")

pt(cod="PT 240", titulo="Responsabilidades do auditor em relação a fraude", norma="NBC TA 240 (itens sobre discussão da equipe, fatores de risco, presunção de fraude na receita, burla de controles pela administração, testes de lançamentos)",
 objetivo="Avaliar fatores de risco de fraude, incluindo reconhecimento de receitas e burla de controles; planejar testes de lançamentos e respostas.",
 afirmacoes="Receita de aluguel (ocorrência, corte, precisão); lançamentos manuais no razão/ativo (existência, valoração). Riscos significativos presumidos: fraude na receita e burla de controles.",
 pop="Real: DRE e notas 18-20 (F1 p.17, p.83). Simulado: 520.150 registros da base de PPI (dados/base_simulada_ppi_allos_2025.csv.gz), inclusive 18% lançamentos manuais.",
 proc=[("RP","Triângulo da fraude com evidência pública: INCENTIVO - guidance de EBITDA R$ 2.070-2.150 mi e resultado de R$ 2.076,5 mi, perto do piso (W1); dividendos pagos de R$ 708.000 mil em 2025 (DFC, F1 p.22); remuneração baseada em ações (nota 25, F1 p.87). OPORTUNIDADE - receita de aluguel por linearização com cálculo sistêmico e julgamento (PAA, F1 p.11); estimativas de valor recuperável internas (F1 p.11-12). ATITUDE - nada em fonte pública indica; PL: entrevistas com administração e governança."),
       ("RP","Presunção de fraude na receita NÃO afastada: a receita de aluguel linear foi tratada como PAA pelo auditor real (F1 p.11); mantém-se risco significativo."),
       ("SM","Testes de lançamentos (CAAT) na base sintética: manuais, usuário fora do cadastro (U099), fim de semana/31-12, valor redondo. Resultado: 90 de 90 lançamentos atípicos inseridos foram identificados (taxa 100%; 0 falsos positivos nesse teste)."),
       ("SM","Teste de Benford no valor de custo: MAD = 0,00037 (aderência alta; nenhum desvio relevante entre dígitos)."),
       ("PL","Entrevistas, discussão da equipe, imprevisibilidade (testes surpresa), revisão de estimativas por viés, acesso ao razão real: dependem de acesso interno.")],
 evid="dados/resultados/comparacao_erros_inseridos_x_identificados_populacao.csv; benford_valor_custo.csv; F1 p.11, p.83, p.87; W1; PT 315, PT 330, PT 450.",
 res="Real: risco significativo mantido para receita e burla de controles (resposta planejada). Simulado: o teste de lançamentos detectou 90/90 manuais atípicos, o que demonstra a eficácia do critério, não fraude na Allos. Limitações: critérios do teste conhecem o padrão inserido (viés de simulação); em dados reais a taxa de detecção seria menor.")

pt(cod="PT 250", titulo="Consideração de leis e regulamentos", norma="NBC TA 250 (itens sobre entendimento do arcabouço legal, procedimentos diante de indícios de descumprimento, comunicação)",
 objetivo="Mapear obrigações relevantes e riscos de descumprimento; definir procedimentos e comunicações diante de indícios.",
 afirmacoes="Divulgação, classificação e completude de provisões e contingências; riscos de multas e passivos.",
 pop="Arcabouço aplicável a companhia aberta do Novo Mercado e do setor de shopping centers.",
 proc=[("RP","Mapa: (i) com efeito direto nas DFs: Lei 6.404/76, normas CVM (informações periódicas, fato relevante - Res. CVM 44, citada em W2; independência do auditor - Res. CVM 162/22, citada em F1), regulamento do Novo Mercado, tributos federais/municipais (DVA, F1 p.23); (ii) sem efeito direto, mas que podem gerar multas ou ação civil: segurança e prevenção de incêndio/pânico, trabalhista (obrigações trabalhistas R$ 145.464 mil, nota 15.2), ambiental, consumidor, locação (ações renovatórias/revisionais, nota 14 F1 p.77), anticorrupção (Lei 12.846/2013), proteção de dados."),
       ("RP","Indício público a acompanhar: incêndio no Shopping Tijuca em 02/01/2026 com óbito de dois brigadistas (W2); a companhia não informou impactos financeiros no comunicado; nota 28 cita cobertura por seguros (F1 p.92). Risco de responsabilização civil/administrativa e de perdas não cobertas."),
       ("PL","Indagar a administração e assessores jurídicos sobre descumprimentos; ler atas e correspondência com reguladores; avaliar ações de comunicação."),
       ("PL","Resposta a indícios: discutir com nível adequado da administração; comunicar à governança (PT 260); avaliar impacto na opinião e no dever de reportar; consultar assessoria jurídica própria.")],
 evid="F1 p.17, p.23, p.77, p.92; W2; PT 260, PT 501, PT 560.",
 res="Mapa elaborado; nenhum indício de descumprimento sustentado por evidência pública, exceto o evento Tijuca, que é acidente (não implica descumprimento comprovado). Limitação: sem acesso a atas, correspondência regulatória ou assessores jurídicos.")

pt(cod="PT 260", titulo="Comunicação com os responsáveis pela governança", norma="NBC TA 260 (itens sobre alcance, época, riscos significativos, independência, dificuldades significativas)",
 objetivo="Preparar comunicação didática sobre alcance, época, riscos significativos, independência e principais dificuldades.",
 afirmacoes="Risco: comunicação tardia ou incompleta aos responsáveis pela governança.",
 pop="Governança hipotética: Conselho de Administração e eventual Comitê de Auditoria (existência a confirmar no Formulário de Referência).",
 proc=[("RP","Insumos reais: PAAs do auditor real (receita de aluguel; valor recuperável de PPI e ágios, F1 p.11-12) e independência (F1 p.10)."),
       ("SM","Minuta (NÃO enviada): ALCANCE - auditoria do grupo ALLOS (controladora e controladas), 45 shoppings com participação e 6 de terceiros (F1 p.3). ÉPOCA - planejamento, interino, final antes de 10/03 do ano seguinte. RISCOS SIGNIFICATIVOS - receita linear; impairment de PPI (R$ 20,38 bi) e ágios (R$ 324,8 mi); burla de controles. INDEPENDÊNCIA - confirmação formal e honorários não-auditoria. DIFICULDADES - acesso a premissas internas, modelos de valor justo e dados dos shoppings."),
       ("PL","Reunião efetiva, atas e resposta da governança: não realizadas.")],
 evid="F1 p.3, p.10-12; PT 200, PT 240, PT 315.",
 res="Minuta pronta como modelo; comunicação real = PLANEJADA. Limitação: não há governança real consultada.")

pt(cod="PT 265", titulo="Comunicação de deficiências de controle interno", norma="NBC TA 265 (itens sobre identificação, avaliação de significância e comunicação)",
 objetivo="Matriz com condição, critério, causa, efeito e recomendação; separar HIPÓTESES de constatações sustentadas por evidências.",
 afirmacoes="Riscos de controle sobre ativação/depreciação do PPI, lançamentos manuais, suporte documental e estimativas.",
 pop="Real: nenhuma deficiência é divulgada em fonte pública (o relatório do auditor não precisa mencioná-las). Simulado: exceções da base sintética.",
 proc=[("RP","Revisão de F1 e F2: nenhuma menção pública a deficiência significativa; conclusão: NÃO há constatação real sustentada."),
       ("SM","Constatações SIMULADAS (sustentadas pelos testes na base sintética): C1 300 registros sem documento suporte; C2 90 lançamentos manuais atípicos; C3 80 ativos 'Baixado' com saldo; C4 150 duplicidades; C5 120 ativações pós-corte; C6 60 saldos negativos; C7 40 terrenos depreciados; C8 200 depreciações divergentes."),
       ("PL","Hipóteses para teste de controles reais (HIP): H1 revisão independente de ativação de obras; H2 bloqueio de lançamento manual em fim de semana; H3 conciliação periódica razão x subledger de ativos; H4 matriz de PCE revisada trimestralmente.")],
 evid="dados/registro_erros_inseridos.csv; dados/resultados/excecoes_populacao.csv; PT 240, PT 330, PT 450.",
 res="MATRIZ (resumo) - CONDIÇÃO: manuais atípicos; CRITÉRIO: política de alçada e segregação; CAUSA (hipótese): ausência de bloqueio sistêmico; EFEITO: risco de burla; RECOMENDAÇÃO: controle preventivo + revisão independente. Idem para C1-C8. Distinção: C1-C8 são SIMULADAS; H1-H4 são hipóteses. Nenhuma é afirmação sobre a Allos real.")

pt(cod="PT 300", titulo="Planejamento da auditoria", norma="NBC TA 300 (itens sobre atividades preliminares, estratégia global, plano de auditoria, direção, supervisão)",
 objetivo="Elaborar estratégia global, plano, cronograma e programas por ciclo; justificar prioridades e alterações.",
 afirmacoes="Alocação de esforço proporcional ao risco: PPI (78,4% do ativo), receita, dívida, estimativas.",
 pop="Ciclos: receitas; disponibilidades/aplicações; PPI/imobilizado; passivos; estimativas; grupo/consolidação.",
 proc=[("RP","Estratégia global: abordagem predominantemente substantiva para PPI (volume e valor) com testes de controles em receita linear (sistema); envolvimento de especialista em avaliação para impairment (compatível com F1 p.12)."),
       ("RP","Cronograma didático: 20/10 fontes e materialidade; 21/10 base sintética e conciliação; 22/10 testes e amostragem; 23/10 PTs restantes; 24/10 PDF e GitHub; 25/10 prazo."),
       ("SM","Programas por ciclo: Anexo A (receitas, disponibilidades, estoques, imobilizado/PPI, passivos, estimativas)."),
       ("RP","Alterações ao plano registradas: (A1) 20/10/2026 - a conta de maior materialidade do ativo é Propriedades para Investimento (R$ 20.381.666 mil; 78,4% do ativo consolidado), confirmada em F1 p.15; (A2) a fonte 'notas explicativas' indicada pelo aluno (F3) é publicação legal resumida; as notas completas estão em F1 p.24-92 e passam a ser a fonte principal.")],
 evid="F1 p.15, p.24-92; Anexo A; PT 315, PT 320, PT 330.",
 res="Plano consistente com os riscos de PT 315. Limitação: cronograma real exigiria visitas, interino e final.")

pt(cod="PT 315", titulo="Identificação e avaliação dos riscos de distorção relevante", norma="NBC TA 315 (itens sobre entendimento da entidade, ambiente, estrutura contábil, TI, controles; riscos significativos)",
 objetivo="Compreender a entidade, ambiente, estrutura contábil, TI e controles; matriz de riscos por conta e afirmação; identificar riscos significativos.",
 afirmacoes="Ocorrência, existência, integridade, direitos/obrigações, mensuração/alocação, apresentação.",
 pop="F1 (DFs e notas) e F3; W1-W5 para contexto. Critério: probabilidade x magnitude por conta/afirmação.",
 proc=[("RP","Entidade e ambiente: plataforma de shopping centers; ao final de 2025, 45 shoppings (ABL total 1.938 mil m2; ABL própria 1.265 mil m2) e 6 de terceiros (F1 p.3). Receitas 2025 (R$ mil): aluguéis 2.055.493; estacionamento 634.500; serviços 341.541; cessão de direito de uso 26.388 (F1 p.83). Segmentos: aluguel, estacionamento, outros (nota 6)."),
       ("RP","Estrutura contábil: CPC/IFRS; PPI ao custo menos depreciação e impairment, com divulgação de valor justo de R$ 32.208.683 mil (incl. minoritários) vs R$ 31.210.322 mil em 2024 (F1 p.66). Rec. linear (CPC 06 R2)."),
       ("RP","Estrutura societária complexa: reestruturações e vendas parciais em 2025 (Brasília adquirido; vendas de 9,9% Plaza Sul, 45% Rio Anil, 10% Tijuca, 20% Carioca - F1 p.66). Nota 4 descreve operações."),
       ("RP","TI e controles (inferência de F1 p.11): contratos de locação e cálculo de linearização são sistêmicos; controles-chave existem na atividade de reconhecimento de receita. Detalhes de ITGC = PL."),
       ("RP","Riscos significativos: R1 receita de aluguel (linearização, corte) - presunção de fraude; R2 impairment/valor recuperável de PPI e ágios; R3 burla de controles. Riscos adicionais: R4 PCE (R$ 546.430 mil sobre bruto de R$ 1.006.629 mil); R5 covenants/endividamento (R$ 5,88 bi); R6 contingências (R$ 254.628 mil) e depósitos judiciais (R$ 192.477 mil); R7 imposto diferido passivo (R$ 4.642.094 mil); R8 partes relacionadas; R9 evento Tijuca."),
       ("PL","Entendimento de controles por walkthrough, ITGC, mapeamento de sistemas e conversas com a administração.")],
 evid="F1 p.3, p.11-12, p.15-17, p.49, p.66, p.83; W2; PT 240, PT 320, PT 330.",
 res="MATRIZ (R=risco; I=inerente; C=controle presumido; S=significativo): PPI - existência/mensuração: I Alto, S sim (R2); Receita aluguel - ocorrência/corte/precisão: I Alto, S sim (R1); PCE - mensuração: I Alto (julgamento), S não; Dívida - integridade/classificação/divulgação covenants: I Médio; Contingências - integridade: I Médio-Alto; Imposto diferido - mensuração: I Médio; Aplicações financeiras - existência/valoração: I Baixo-Médio; Partes relacionadas - integridade/divulgação: I Médio. Cruzamento com os PAAs reais (receita e impairment) confirma R1 e R2. Limitação: avaliação de controle é presumida (sem walkthroughs).")

pt(cod="PT 320", titulo="Materialidade no planejamento e execução", norma="NBC TA 320 (itens sobre determinação da materialidade global, para execução e específicas; revisão)",
 objetivo="Calcular e justificar materialidade global, para execução e materialidades específicas; fundamentar bases e percentuais.",
 afirmacoes="Define o limite para distorções relevantes nas DFs consolidadas de 31/12/2025.",
 pop="Referências reais (R$ mil, F1 p.15-17): LAIR 1.017.601; receita líquida 2.859.106; ativo total 26.006.439; PL 13.899.006.",
 proc=[("RP","Base escolhida: LAIR consolidado (medida de rentabilidade estável; investidores a utilizam), 5% = R$ 50.880 mil = materialidade GLOBAL."),
       ("RP","Materialidade para execução: 75% = R$ 38.160 mil (risco inerente alto em estimativas e ausência de histórico). Trivial: 5% da global = R$ 2.544 mil."),
       ("RP","Referências comparativas (planilha PT320): 1% receita = R$ 28.591 mil; 0,5% ativo = R$ 130.032 mil; 1% PL = R$ 138.990 mil. Escolha da menor medida estável cuja cobertura é razoável para os usuários."),
       ("RP","Materialidades específicas: PPI (0,25% do saldo = R$ 50.954 mil) comparada, não adotada; partes relacionadas (nota 23) - 10% do saldo, PL por exigir dado interno."),
       ("RP","Revisão: reavaliar se resultado final divergir de modo relevante; no cenário simulado, distorções quantificadas somam 129% da materialidade global (PT 450), o que levaria à reavaliação.")],
 evid="planilhas/papeis_de_trabalho_calculos_allos_2025.xlsx (aba PT320_Materialidade); F1 p.15-17.",
 res="Global R$ 50.880.050; execução R$ 38.160.037,50; trivial R$ 2.544.002,50 (em reais, base de uso na amostragem). Limitação: percentuais são julgamento do aluno, não parâmetro oficial.")

pt(cod="PT 330", titulo="Respostas do auditor aos riscos avaliados", norma="NBC TA 330 (itens sobre respostas globais, procedimentos adicionais, testes de controles, procedimentos substantivos)",
 objetivo="Relacionar cada risco aos testes de controles e substantivos, definindo natureza, época e extensão; distinguir executado x planejado.",
 afirmacoes="Vide matriz de PT 315.",
 pop="Riscos R1-R9 (PT 315). Base sintética de PPI para testes substantivos de detalhe.",
 proc=[("SM","R2/PPI-existência: confirmar existência e ativação (amostra MUS + 100% itens-chave): EXECUTADO sobre a base sintética (PT 530)."),
       ("SM","R2/PPI-corte: ativações em 2026: EXECUTADO (120 detectados de 120)."),
       ("SM","R2/PPI-mensuração: recálculo de depreciação em 100% da base: EXECUTADO (200/200 detectados; 183 'colaterais' explicados)."),
       ("RP","R4/PCE: recálculo pela matriz da nota 8: EXECUTADO (PT 540)."),
       ("RP","R1/Receita: analítico por natureza (PT 520): EXECUTADO com DFP."),
       ("PL","R1: teste de controle sobre linearização; recálculo em amostra de contratos; testes de corte de receita no razão real."),
       ("PL","R2/impairment: especialista em avaliação; testar taxa de desconto (7,25%-11,75%) e exit yield (7,00%-11,50%), comparar com mercado e projeções passadas (compatível com F1 p.12)."),
       ("PL","R5/dívida: confirmação com bancos e debenturistas; recálculo de covenants; R6: confirmação com assessores jurídicos (PT 505).")],
 evid="PT 315, PT 450, PT 505, PT 520, PT 530, PT 540; dados/resultados/*.csv.",
 res="Natureza: substantiva para PPI (volume) e analítica/recálculo para PCE e receita; controles para linearização (PL). Época: final de exercício (PL real), com interino para controles. Extensão: 100% de CAAT na base; MUS ~1.570 itens + 4 itens-chave + 60 negativos. Cobertura real das respostas é PARCIAL pela falta de acesso.")
