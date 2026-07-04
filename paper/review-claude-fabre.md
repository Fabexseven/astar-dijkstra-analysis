Vou executar a avaliação conforme o prompt. Primeiro preciso inspecionar o repositório R1 (e R2 se necessário) para as verificações dos Blocos B e E.Todas as verificações foram concluídas, incluindo a re-execução completa dos 540 experimentos com determinismo confirmado. Segue o parecer no formato exigido.

---

# PARECER DE CONFORMIDADE — "Análise empírica de A\* versus Dijkstra para menor caminho em grids 2D com obstáculos" vs. Especificação da Disciplina

## 1. Sumário executivo

O short-paper apresenta conformidade substancial com a especificação (D2), com evidência forte de integridade experimental: a re-execução completa dos 540 experimentos a partir de R1 reproduziu `found`, `path_cost` e `visited_nodes` de forma bit-idêntica ao CSV versionado, e todas as médias da Tabela 1 de D1 conferem com o CSV. **Pontos fortes:** (1) reprodutibilidade real verificada de ponta a ponta; (2) fidelidade teórica rigorosa a Hart et al. (Teorema 1, Lema 2, h ≡ 0); (3) análise crítica que explica inclusive quando o A\* perde (§5.1). **Gaps principais:** (1) **P0** — o trabalho lista um único autor, mas D2 exige grupo de 2 a 4 pessoas; (2) **P1** — a complexidade assintótica dos algoritmos está ausente, embora exigida por D2 "quando disponível"; (3) **P1** — a citação a Ardiansyah et al. [2] é sobre-interpretada e o README de R1 referencia uma pasta `paper/` inexistente. Recomendação: **APTO COM AJUSTES MENORES**, condicionado à resolução do item administrativo P0 com o professor.

## 2. Matriz de conformidade

| ID | Requisito | Status | Evidência (localização exata) | Observação |
|----|-----------|--------|-------------------------------|------------|
| A1 | Compreender o problema (entradas/saídas, função objetivo, restrições) | ATENDE | D1 §1, §2 e §3.1: entradas (grid n×n, origem (0,0), destino (n−1,n−1)), saída (caminho), objetivo (minimizar custo em passos, §3.2 métrica i), restrições (pesos não negativos/unitários, obstáculos, 4-conectividade) | Os quatro elementos estão presentes, embora "função objetivo" não seja nomeada formalmente com esse termo |
| A2 | Estudar o algoritmo (ideia, etapas, estruturas de dados, complexidade) | ATENDE PARCIALMENTE | D1 §2 (f = g + h, admissibilidade, consistência) e §3.1 (heap binário `heapq`, dicionário g, conjunto de expandidos) | ⚠ A complexidade assintótica (ex.: O((V+E) log V) com heap binário) **não é apresentada em nenhuma seção de D1**, apesar de amplamente disponível para Dijkstra/A\* |
| A3 | Implementação própria; bibliotecas só auxiliares | ATENDE | R1: `src/dijkstra.py`, `src/astar.py`, `src/grid.py` implementados do zero (apenas `heapq` da stdlib); `requirements.txt` contém somente `pandas>=2.0` e `matplotlib>=3.7` (usados só em `src/plots.py`); D1 §3.1 declara "sem bibliotecas externas de grafos ou pathfinding" | Declaração de D1 confere com o código |
| A4 | Tarefa de otimização com instâncias e critério mensurável | ATENDE | D1 §3.2: 3 tamanhos × 3 densidades × 30 seeds; métricas custo/nós/tempo. Exclusão das 122 execuções inviáveis justificada em D1 §3.2 e implementada em R1 `src/plots.py` linha 30 (`df = df[df["found"] == True]`) | Tratamento idêntico no artigo e no repositório |
| A5 | Comparação com baseline | ATENDE | D1 §2 (Dijkstra como caso h ≡ 0), §4 (Tabela 1 compara nós e tempo; §4.1 compara qualidade); README de R1 rotula explicitamente "Dijkstra (baseline)" | Cobre qualidade da solução E eficiência; escolha justificada teoricamente |
| A6 | Analisar resultados (bom desempenho / falha / decisões / limitações) | ATENDE | Bom desempenho: D1 §4.2–4.3 e §5 (mapas densos/grandes); falha: §5.1 (esparsos, tempo 4–9% pior); decisões de implementação: §3.1 e §5.1 (sobrecusto por nó, Python puro); limitações: §5.2 | As quatro dimensões de D2 estão cobertas |
| B1 | Short-paper ≤ 4 páginas | ATENDE | D1 possui exatamente 4 páginas (verificado via extração do PDF); referências na página 4 | Com referências dentro: 4 páginas; sem referências: < 4 páginas. Atende em ambas as contagens, independentemente da permissão do professor |
| B2 | Repositório GitHub organizado | ATENDE | R1 árvore raiz: `src/`, `results/`, `graphs/`, `README.md`, `requirements.txt`, `.gitignore` | Estrutura limpa e modular |
| B3 | Instruções de execução | ATENDE | README de R1, seções "Instalação", "Como rodar os experimentos" (`python -m src.experiments`) e "Como gerar os gráficos" (`python -m src.plots`); comandos executados com sucesso nesta avaliação | Verificado por execução real |
| B4 | Dados/scripts para reprodução | ATENDE PARCIALMENTE | `results/results.csv` versionado (540 linhas + cabeçalho, conferido); seeds 0–29 documentadas no README e codificadas em `src/experiments.py` | ⚠ O README referencia `paper/` na "Estrutura do repositório", mas a pasta **não existe** na árvore real de R1 (raiz contém apenas graphs/, results/, src/ e 3 arquivos) — inconsistência P1 |
| B5 | Apresentação oral | FORA DE ESCOPO | — | Não avaliável por documento |
| C1 | Introdução com motivação da escolha do artigo | ATENDE | D1 §1, parágrafo 2: objetivo de "reproduzir empiricamente [...] o ganho previsto pela formulação de [1]" | Motivação presente, embora sucinta |
| C2 | Referências completas do artigo e algoritmo | ATENDE PARCIALMENTE | Referência [1] completa (D1, Referências). ⚠ Referência [2] incompleta: "ARDIANSYAH et al. [...] 2025" **omite venue (bit-Tech), volume (8), número (2), páginas e DOI (10.32877/bt.v8i2.3474)**, todos presentes em D4 | Corrigir a entrada [2] |
| C3 | Implementação e metodologia | ATENDE | D1 §3.1 (decisões: mesma estrutura, mesma função de vizinhança, chave de prioridade como única diferença) e §3.2 (instâncias e métricas) | — |
| C4 | Resultados com tabelas/figuras e baseline | ATENDE | D1 Tabela 1 (legendada, unidades ms) e Figuras 1–3 (legendas com média ± desvio padrão) | Ver E6 sobre separador de milhar |
| C5 | Discussão: divergências, dificuldades, melhorias | ATENDE PARCIALMENTE | Divergências/limitações: D1 §5.1–5.2. Melhorias: implícitas em §5.2 (heurísticas octile/euclidiana, memória não avaliada). ⚠ "Dificuldades de implementação" não são relatadas explicitamente em nenhuma seção | Adicionar 1–2 frases sobre dificuldades encontradas |
| C6 | Conclusão | ATENDE | D1 §6: resume aprendizados e conclui adequação ("Em aplicações com mapas densos e de larga escala, o A\* mostra-se claramente preferível") | — |
| D1 | Adequação/relevância do artigo | ATENDE | Hart et al. (1968) é o artigo seminal do A\*; tema "caminhos mínimos" listado como adequado em D2 | — |
| D2 | Compreensão do problema e algoritmo | ATENDE PARCIALMENTE | Compreensão teórica sólida (D1 §2), mas ausência da complexidade assintótica (ver A2) | Risco em arguição: pergunta sobre complexidade é provável |
| D3 | Qualidade da implementação | ATENDE | Código de R1 limpo, documentado, modular, determinístico (verificado por re-execução) | — |
| D4 | Definição da tarefa de otimização | ATENDE | Ver A4 | — |
| D5 | Comparação experimental com baseline | ATENDE | Ver A5 | — |
| D6 | Clareza e objetividade do short-paper | ATENDE | Texto conciso, 4 páginas, estrutura na ordem sugerida por D2 | Ver E6 (ambiguidade tipográfica) |
| D7 | Análise crítica dos resultados | ATENDE | D1 §5.1 é o ponto alto: explica o caso em que o A\* perde em tempo apesar de podar nós | Ver E4: a ancoragem em [2] é frágil |
| D8 | Organização do repositório | ATENDE PARCIALMENTE | Estrutura boa, mas README descreve pasta `paper/` inexistente (ver B4) | — |
| D9 | Qualidade da apresentação oral | FORA DE ESCOPO | — | — |

## 3. Checagens de integridade (Bloco E)

| ID | Resultado | Evidência | Severidade |
|----|-----------|-----------|------------|
| E1 | **NÃO ATENDE** — D1 lista **1 autor** (Fábio Krein); D2 exige grupo de no mínimo 2 e no máximo 4 pessoas | D1, cabeçalho | **P0** — confirmar com o professor se trabalho individual foi autorizado |
| E2 | **ATENDE** — 540 execuções, 122 com `found=False`, 418 viáveis; médias da Tabela 1 de D1 conferem exatamente com o CSV (ex.: 200×200/30%: A\* 5.478,5 ≈ 5.479 nós, 10,41 ms; Dijkstra 27.417,4 nós, 42,17 ms) | R1 `results/results.csv` (análise pandas nesta avaliação); D1 §3.2, §4.1, Tabela 1 | — |
| E3 | **ATENDE** — (a) "se h admissível, A\* é ótimo" fiel ao Teorema 1 de D3 ("If ĥ(n) ≤ h(n) for all n, then A\* is admissible"); (b) "se consistente, cada nó expandido no máximo uma vez" fiel ao Lema 2 e à discussão de que a reabertura do Passo 4 torna-se vácua; (c) "Dijkstra = A\* com h ≡ 0" compatível com D3 §IV-A. Ressalva: D3 §IV-A atribui o caso f̂ = ĝ ao algoritmo de Minty (via Pollack e Wiebenson) e **não cita Dijkstra nominalmente**; a identificação com Dijkstra é padrão na literatura, mas é inferência do autor, não afirmação literal de D3 | D3 pp. 103, 104 (Lemma 2), 106 (§IV-A) | P2 (nota de precisão) |
| E4 | **ATENDE PARCIALMENTE — citação sobre-interpretada.** D1 §5.1 afirma que "Ardiansyah et al. [2] reportam comportamento semelhante [...] vantagens em expansões nem sempre se traduzem proporcionalmente em tempo". Em D4, porém, o A\* melhora **ambas** as métricas (Tabela 4: 8 vs. 11 nós; 1,9 vs. 2,8 ms — redução de tempo de ~32%, maior que a redução de nós de ~27%); D4 não reporta o fenômeno de ganho em nós sem ganho proporcional em tempo. Nota adicional: D4 tem inconsistência interna (Fig. 2 reporta 7 vs. 6 nós explorados; Tabela 4 reporta 11 vs. 8), o que fragiliza qualquer leitura quantitativa de [2] | D1 §5.1; D4 Tabela 4, Fig. 2 e §IV-C/D | **P1** |
| E5 | **ATENDE** — D1 define nós visitados como "cardinalidade do conjunto de nós removidos da fila de prioridade"; em R1, `visited_nodes = len(visited)`, onde `visited` acumula exatamente os nós retirados do heap (pops duplicados colapsam no conjunto). Definições coincidem em ambos os algoritmos | R1 `src/dijkstra.py` e `src/astar.py` (laço `heappop` → `visited.add`) | — |
| E6 | **RISCO CONFIRMADO** — Tabela 1 de D1 mistura ponto como separador de milhar ("2.254", "5.479", "27.417" nós) e ponto como separador decimal ("3.08", "10,41"/"42,17" ms — o texto de §4.3 usa vírgula decimal). O CSV confirma que "2.254" = 2.254 nós (dois mil e duzentos), mas um leitor pode interpretar como 2,254. Padronizar | D1 Tabela 1 vs. R1 CSV (médias 2254,0 e 5478,5) | **P2** |
| E7 | **ATENDE (verificação forte)** — Reprodução executada nesta avaliação: `pip install -r requirements.txt` + `python -m src.experiments` regenerou o CSV; comparação linha a linha com o CSV versionado mostrou `found`, `path_cost` e `visited_nodes` **bit-idênticos** nas 540 execuções (tempos variam por máquina, como o README adverte). `python -m src.plots` regenera os 9 PNGs a partir do CSV, com o mesmo filtro de inviáveis do artigo. Não foi necessário recorrer a R2 | Execução real em ambiente limpo; R1 README, `src/experiments.py`, `src/plots.py` | — |

## 4. Gaps priorizados

| Prioridade | Gap | Requisito violado (ID) | Recomendação acionável | Esforço estimado |
|------------|-----|------------------------|------------------------|------------------|
| P0 | Trabalho com 1 autor; especificação exige grupo de 2–4 pessoas | E1 (D2, "Tarefa") | Confirmar por escrito com o professor a autorização para entrega individual ou incluir coautor antes da entrega | Trivial (administrativo) |
| P1 | Complexidade assintótica ausente | A2 / D2 | Adicionar parágrafo na Seção 2 com a complexidade O((V+E) log V) do Dijkstra/A\* com heap binário e observar que, no grid, V = n² e E ≈ 4n² | 15 min |
| P1 | Citação [2] sobre-interpretada em §5.1 | E4 / D7 | Reescrever a frase para afirmar apenas que [2] compara as mesmas métricas em malha viária, removendo a atribuição do fenômeno "expansões ≠ tempo" a [2], ou citar fonte que efetivamente o reporte | 10 min |
| P1 | README referencia pasta `paper/` inexistente | B4 / D8 | Criar a pasta `paper/` com o PDF do short-paper ou remover a linha correspondente da "Estrutura do repositório" no README | 5 min |
| P1 | Referência [2] bibliograficamente incompleta | C2 | Completar a entrada [2] com venue, volume, número, páginas e DOI: "bit-Tech, v. 8, n. 2, p. 2974–2983, 2025. doi: 10.32877/bt.v8i2.3474" | 5 min |
| P2 | Separador de milhar ambíguo na Tabela 1 | E6 / D6 | Padronizar a Tabela 1 usando espaço fino ou vírgula PT-BR consistente para milhares e decimais (ex.: "2 254" e "10,41") | 10 min |
| P2 | "Dificuldades de implementação" não explicitadas | C5 | Adicionar 1–2 frases em §5 relatando dificuldades concretas (ex.: tratamento de grids inviáveis, medição de tempo estável) | 10 min |
| P2 | Atribuição de "Dijkstra = A\* com h ≡ 0" diretamente a [1] | E3(c) | Ajustar a redação para "o caso h ≡ 0 discutido em [1, §IV-A] corresponde à busca de custo uniforme, equivalente ao Dijkstra" | 5 min |
| P2 | Alegação de que as exclusões ocorrem "predominantemente no cenário 200×200 com 30%" | E2 (precisão) | Reformular: das 122 exclusões, 96 ocorrem a 30% de densidade (26/34/36 por tamanho) e 26 a 20%; o cenário 200×200/30% é a moda (36), não a maioria | 5 min |

## 5. Observações complementares (fora da especificação)

1. O README de R1 afirma que a 20% de obstáculos o A\* visita "cerca de 62%" dos nós do Dijkstra, enquanto D1 §4.2 afirma "aproximadamente 60%" — pequena divergência de arredondamento entre README e artigo; alinhar os dois textos.
2. A análise geométrica de §5 (onda circular vs. corredor) é uma contribuição didática acima do exigido; uma figura ilustrando os nós expandidos em um grid de exemplo a fortaleceria na arguição.
3. O desvio padrão elevado do A\* é mencionado (§4.2) mas não quantificado na Tabela 1; incluir a coluna ±σ tornaria a afirmação verificável no próprio artigo.
4. O CSV registra execuções inviáveis também a 20% de densidade (26 casos), o que poderia ser explorado brevemente como evidência do limiar de percolação do grid.
5. Considerar fixar versões exatas em `requirements.txt` (ex.: `pandas==2.x.y`) para reprodutibilidade estrita de ambiente, embora as versões mínimas atuais tenham funcionado nesta verificação.

## 6. Veredicto final

- **Conformidade global:** 17 de 24 itens avaliáveis em ATENDE; 6 em ATENDE PARCIALMENTE (A2, B4, C2, C5, D2, D8 — todos sanáveis com esforço menor que 1 hora no total); 1 em NÃO ATENDE (E1, administrativo).
- **Itens FORA DE ESCOPO:** B5, D9 (apresentação oral).
- **Recomendação: APTO COM AJUSTES MENORES** — condicionado à resolução do gap P0 (composição do grupo) junto ao professor. A base experimental é sólida e integralmente reprodutível (verificada por re-execução completa nesta avaliação); os demais ajustes são pontuais e de baixo esforço.
