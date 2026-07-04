# PARECER DE CONFORMIDADE — Análise empírica de A* versus Dijkstra para menor caminho em grids 2D com obstáculos vs. Especificação da Disciplina

## 1. Sumário executivo

O artigo submetido apresenta um estudo empírico robusto e bem fundamentado comparando Dijkstra e A*, destacando-se pela análise crítica do "sobrecusto da heurística". No entanto, a submissão viola um requisito administrativo crítico da disciplina quanto à composição do grupo.
**Pontos fortes:**

* Metodologia experimental estruturada com reprodutibilidade por sementes e tratamento adequado de instâncias inviáveis.


* Excelente fundamentação teórica conectada à implementação geométrica.


* Análise sofisticada dos cenários onde o baseline (Dijkstra) supera o A* em tempo, demonstrando maturidade analítica.
**Gaps principais:**


* Autoria individual, contrariando a especificação de grupo de 2 a 4 pessoas.


* Extrapolação/Interpretação incorreta dos resultados da referência complementar (Ardiansyah et al.).


* Ausência da declaração de complexidade computacional e de reflexões sobre dificuldades/melhorias, exigidas na especificação.



---

## 2. Matriz de conformidade

| ID | Requisito | Status | Evidência (localização exata) | Observação |
| --- | --- | --- | --- | --- |
| **A1** | Compreender o problema (otimização, entradas/saídas, restrições) | ATENDE | D1 - Resumo e Seções 1, 3.1

 | Explicitados grids, obstáculos, heurísticas e função objetivo (minimizar passos). |
| **A2** | Estudar o algoritmo (ideia, etapas, estruturas, complexidade) | ATENDE PARCIALMENTE | D1 - Seções 2 e 3.1

 | Explica $f = g + h$ e filas de prioridade, mas omite a complexidade assintótica exigida.

 |
| **A3** | Implementação própria | ATENDE | D1 - Seção 3.1

 | Autoria afirma uso de Python puro sem bibliotecas de grafos externas.

 |
| **A4** | Definir tarefa de otimização | ATENDE | D1 - Seção 3.2

 | Configurações de grids (50x50 a 200x200), densidades e justificativa para 122 descartes.

 |
| **A5** | Comparar com baseline | ATENDE | D1 - Seções 2 e 4

 | Dijkstra utilizado como baseline e fundamentado como caso particular $h \equiv 0$.

 |
| **A6** | Analisar resultados (sucessos, falhas, decisões, limitações) | ATENDE | D1 - Seções 5.1 e 5.2

 | Discute overhead do Python e falhas de desempenho do A* em ambientes esparsos.

 |
| **B1** | Short-paper de até 4 páginas | INCONCLUSIVO | [VERIFICAR] | A extensão visual do texto parece adequada, mas a paginação exata depende da formatação PDF final. |
| **B2** | Código-fonte em GitHub | INCONCLUSIVO | [VERIFICAR] | Link fornecido na Seção 6, mas repositório indisponível para verificação direta no contexto.

 |
| **B3** | Instruções de execução | INCONCLUSIVO | [VERIFICAR] | Depende de verificação do README no repositório. |
| **B4** | Dados/scripts para reprodução | INCONCLUSIVO | [VERIFICAR] | Depende de verificação do repositório indicado.

 |
| **B5** | Apresentação oral | FORA DE ESCOPO | N/A | Avaliação presencial. |
| **C1** | Introdução (relevância, motivação) | ATENDE | D1 - Seção 1

 | Contextualiza a navegação e a formulação de Hart et al..

 |
| **C2** | Artigo selecionado e referência completa | ATENDE PARCIALMENTE | D1 - Referências

 | A referência [2] está incompleta (falta journal e DOI) quando comparada à fonte original.

 |
| **C3** | Implementação e metodologia | ATENDE | D1 - Seção 3

 | Detalha ambiente e restrições. |
| **C4** | Resultados com tabelas/figuras | ATENDE | D1 - Seção 4 (Tabela 1, Figs 1-3)

 | Gráficos e tabela muito bem estruturados.

 |
| **C5** | Discussão e limitações (dificuldades e melhorias) | ATENDE PARCIALMENTE | D1 - Seção 5

 | Apresenta limitações, mas não cita "dificuldades de implementação" ou "possíveis melhorias" conforme exigido.

 |
| **C6** | Conclusão | ATENDE | D1 - Seção 6

 | Sintetiza com clareza o comportamento prático vs. teórico.

 |
| **D1-D7** | Critérios teóricos/analíticos do professor | ATENDE | D1 - Todo o documento

 | Exceto as ressalvas de complexidade e extrapolação apontadas nos Gaps. |
| **D8** | Organização do repositório | INCONCLUSIVO | [VERIFICAR] | Requer acesso ao link fornecido.

 |
| **D9** | Qualidade da apresentação oral | FORA DE ESCOPO | N/A |  |

---

## 3. Checagens de integridade (Bloco E)

| ID | Resultado | Evidência | Severidade |
| --- | --- | --- | --- |
| **E1** | **NÃO ATENDE** | D1 lista apenas "Fábio Krein" como autor. D2 exige grupos de no mínimo 2 pessoas.

 | P0 |
| **E2** | **ATENDE** | A matemática de execuções (540 totais - 122 excluídas = 418 viáveis) é consistente ao longo das seções 3.2 e 4.1 de D1.

 | N/A |
| **E3** | **ATENDE** | As afirmações de D1 sobre admissibilidade, consistência e Dijkstra como $h \equiv 0$ estão estritamente alinhadas aos Lemas 1 e 2 e à Seção IV-A de Hart et al..

 | N/A |
| **E4** | **NÃO ATENDE** | D1 afirma na Seção 5.1 que Ardiansyah et al. (Ref [2]) "reportam comportamento semelhante... vantagens em expansões nem sempre se traduzem... em tempo". Contudo, D4 afirma o oposto: "A* demonstra eficiência superior... consumindo menos tempo" em todos os seus cenários.

 | P1 |
| **E5** | **INCONCLUSIVO** | Definição de métrica de nós visitados requer inspeção de `src/astar.py`. | N/A |
| **E6** | **ATENDE** | O uso de "5.479" utiliza o padrão PT-BR para separador de milhar. (Observação: P2 para padronização global).

 | P2 |
| **E7** | **INCONCLUSIVO** | Reprodutibilidade declarada depende de acesso ao repositório. | N/A |

---

## 4. Gaps priorizados

| Prioridade | Gap | Requisito violado (ID) | Recomendação acionável | Esforço estimado |
| --- | --- | --- | --- | --- |
| **P0** | **Composição inválida do grupo** | E1 (D2 - Tarefa) | Confirmar com o professor a aceitação de trabalho individual antes da avaliação formal. | Baixo |
| **P1** | **Falsa atribuição de conclusão à literatura** | E4 | Remover a frase referente ao suposto comportamento de lentidão no artigo de Ardiansyah et al. na Seção 5.1, mantendo a observação apenas sobre o experimento próprio. | Baixo |
| **P1** | **Ausência de Complexidade Computacional** | A2 | Adicionar um parágrafo na Seção 2 declarando a complexidade de tempo e espaço de Dijkstra e A* com heap binário. | Baixo |
| **P2** | **Falta de discussão sobre melhorias e dificuldades** | C5 | Inserir um parágrafo na Seção 5.2 mencionando explicitamente as dificuldades enfrentadas e as direções futuras/melhorias. | Baixo |
| **P2** | **Referência Incompleta** | C2 | Atualizar a Referência [2] para incluir os dados completos de publicação (Volume, Edição e DOI do periódico Bit-Tech). | Muito Baixo |

---

## 5. Observações complementares (fora da especificação)

* A inferência do impacto geométrico (a "onda quase circular" do Dijkstra vs. o "corredor" do A*) foi uma sacada analítica excelente e valoriza consideravelmente o mérito científico do trabalho.


* A formatação dos valores na Tabela 1 de D1 utiliza ponto (ex: 2.254) para milhar nos nós visitados, mas vírgula (ex: 13,75 não é explícito, apenas 13.75 em notação US) para tempo. Uniformizar a notação numérica para o padrão PT-BR ou US ao longo de todo o texto evitaria potenciais confusões.



---

## 6. Veredicto final

* **Conformidade global:** 8 de 11 itens puramente textuais (avaliáveis no documento) em status ATENDE ou ATENDE PARCIALMENTE.
* **Itens FORA DE ESCOPO/INCONCLUSIVOS:** B1, B2, B3, B4, B5, D8, D9, E5, E7.
* **Recomendação:** **REQUER REVISÃO** (Devido à violação administrativa P0 do limite mínimo de alunos no grupo e ao erro material de citação P1).
