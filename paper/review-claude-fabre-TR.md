Vou executar a mesma avaliação sobre a Versão II. Primeiro preciso inspecionar o repositório agora referenciado pelo artigo (R2), verificar se a nova metodologia de cronometragem (mediana de 10 execuções, Wilcoxon) está implementada, e revalidar os números.Todas as verificações da Versão II foram concluídas. Segue o parecer atualizado.

---

# PARECER DE CONFORMIDADE — "Análise empírica de A\* versus Dijkstra..." (Versão II, Krein & Souza) vs. Especificação da Disciplina

## 1. Sumário executivo

A Versão II resolve os quatro gaps mais graves da Versão I: o trabalho agora tem **dois autores** (P0 sanado), a **complexidade assintótica** O((V+E) log V) está na Seção 2, a pasta **`paper/`** existe no repositório com artigo, diff e script de build, e a **Tabela 1 adota convenção PT-BR consistente** (ponto milhar, vírgula decimal). A integridade experimental segue exemplar: as médias, razões e frações de percolação (90/90, 77/90, 42/90) da Tabela 1 conferem exatamente com o CSV versionado, e o teste de Wilcoxon foi **regenerado nesta avaliação com valores idênticos** ao `significance.csv` (p máximo = 4,9×10⁻⁴, validando a alegação "p < 0,001" nas nove configurações). **Pontos fortes:** (1) metodologia de cronometragem robustecida (mediana de 10 medições) implementada e documentada em `src/experiments.py`; (2) validação estatística pareada nova e reprodutível; (3) justificativa de exclusão das 122 execuções agora fundamentada (percolação) e com argumento de não-enviesamento. **Gaps remanescentes:** (1) **P1** — a citação a Ardiansyah et al. [2] permanece sobre-interpretada; (2) **P1** — o README de R2 mantém números da cronometragem antiga, divergindo do artigo e do CSV atuais; (3) **P1** — referência [2] segue bibliograficamente incompleta. Recomendação: **APTO COM AJUSTES MENORES**.

## 2. Matriz de conformidade

| ID | Requisito | Status | Evidência (localização exata) | Observação |
|----|-----------|--------|-------------------------------|------------|
| A1 | Compreender o problema | ATENDE | D1-v2 §1 (duas questões de pesquisa explícitas), §3.1 (entradas, saída, restrições), §3.2 (função objetivo: custo em passos) | Melhorado: RQs (i) e (ii) explicitam o que se otimiza e o que se mede |
| A2 | Estudar o algoritmo (incl. complexidade) | **ATENDE** ✚ | D1-v2 §2, último parágrafo: "Implementados com heap binário, ambos têm complexidade de pior caso O((V + E) log V) — com V = n² e E = O(n²)", com a observação correta de que a vantagem do A\* é de fator constante/caso médio | **Gap da Versão I sanado** |
| A3 | Implementação própria; bibliotecas auxiliares | ATENDE | R2 `src/*.py` do zero; `requirements.txt` adiciona `scipy>=1.10` e `markdown>=3.4`; docstring de `significance.py` justifica explicitamente: "o uso de SciPy aqui é tarefa auxiliar de análise, não substitui os algoritmos" | Uso auxiliar em conformidade com D2 |
| A4 | Tarefa de otimização com instâncias e critério | ATENDE ✚ | D1-v2 §3.2: exclusão das 122 execuções agora justificada por percolação, com frações verificadas contra o CSV (90/90, 77/90, 42/90 grids viáveis por densidade) e argumento de que a exclusão não favorece o A\* | Justificativa substancialmente mais forte que na Versão I |
| A5 | Comparação com baseline | ATENDE | D1-v2 §2 (h ≡ 0), Tabela 1, §4.1–4.3; agora com significância estatística pareada por semente | — |
| A6 | Analisar resultados (4 dimensões) | ATENDE | Bom desempenho: §4.2–4.3, §5; falha: §5.1 (agora com evidência estatística: "mais lento nas três com 10%"); decisões: §3.1–3.2 (mediana de 10 medições); limitações: §5.2 | — |
| B1 | Short-paper ≤ 4 páginas | ATENDE | PDF revisado possui exatamente 4 páginas; referências na página 4 (dentro do limite em ambas as contagens) | — |
| B2 | Repositório GitHub organizado | ATENDE | R2 (repositório referenciado pelo artigo): `src/`, `results/`, `graphs/`, `paper/`, `docs/`, README, requirements | ⚠ Ver gap de consolidação R1↔R2 na Seção 4 |
| B3 | Instruções de execução | ATENDE | README de R2: instalação com venv, `python -m src.experiments`, `python -m src.plots`, `python -m src.significance` (docstring) e `python paper/build_pdf.py`; experimentos, gráficos e significância executados com sucesso nesta avaliação | `build_pdf.py` requer Chrome/Chromium, dependência externa devidamente documentada |
| B4 | Dados/scripts para reprodução | **ATENDE** ✚ | `results/results.csv` (540 linhas) e `results/significance.csv` versionados; seeds 0–29; pasta `paper/` **agora existe** com `paper_revisado.md`, `.pdf`, `.diff` e `build_pdf.py` (todos verificados, HTTP 200) | **Inconsistência README↔árvore da Versão I sanada** |
| B5 | Apresentação oral | FORA DE ESCOPO | — | — |
| C1 | Introdução com motivação | ATENDE | D1-v2 §1, com questões de pesquisa (i) e (ii) formalizadas | — |
| C2 | Referências completas | ATENDE PARCIALMENTE | [1] completa; [3] (Dijkstra, 1959) **adicionada** — corrige a citação órfã da Versão I. ⚠ [2] **permanece incompleta**: "ARDIANSYAH et al. [...] 2025" ainda omite venue (bit-Tech), v. 8, n. 2, páginas e DOI (10.32877/bt.v8i2.3474) presentes em D4 | Gap parcialmente sanado |
| C3 | Implementação e metodologia | ATENDE ✚ | §3.1–3.2; nova metodologia de tempo (mediana de 10 medições, host único) descrita no artigo e **implementada de forma idêntica** em `src/experiments.py` (`TIMING_REPETITIONS = 10`, `median(timings)`) | Verificação cruzada artigo↔código positiva |
| C4 | Resultados com tabelas/figuras | ATENDE | Tabela 1 (nova coluna de tempos, razões recalculadas — todas as 9 razões conferem com o CSV: 1,11/0,83/0,50/1,10/0,82/0,36/1,15/0,85/0,27) e Figuras 1–3 | ⚠ Legenda da Figura 1 ainda diz "sobre 30 sementes" — ver Seção 4 |
| C5 | Discussão: divergências, dificuldades, melhorias | **ATENDE** ✚ | Dificuldade concreta (ruído de cronometragem em escala de ms) identificada em §3.2 e mitigada; §5.2 renomeada "Limitações **e trabalhos futuros**" com melhorias explícitas (heurísticas octile/euclidiana, estudo de memória/fronteira) | Gap da Versão I sanado |
| C6 | Conclusão | ATENDE | §6, agora com quantificações precisas (10–15%; ≈3,8×) e direção futura | — |
| D1 | Adequação do artigo | ATENDE | Inalterado | — |
| D2 | Compreensão do problema/algoritmo | **ATENDE** ✚ | Complexidade presente (ver A2); distinção pior caso vs. caso médio demonstra compreensão madura | Risco de arguição reduzido |
| D3 | Qualidade da implementação | ATENDE ✚ | `significance.py` bem documentado, com teste t como verificação complementar e tratamento de exceções; `measure()` com justificativa da mediana em docstring | — |
| D4 | Definição da tarefa | ATENDE | Ver A4 | — |
| D5 | Comparação com baseline | ATENDE ✚ | Agora com Wilcoxon pareado por semente — reproduzido nesta avaliação com resultados **idênticos** ao CSV versionado | — |
| D6 | Clareza do short-paper | ATENDE ✚ | Convenção numérica PT-BR agora consistente na Tabela 1 (E6 da Versão I sanado); texto mais denso porém dentro de 4 páginas | — |
| D7 | Análise crítica | ATENDE | §5.1 fortalecida: a desvantagem do A\* em grids esparsos passa de observação a achado estatisticamente validado ("real e reprodutível") | ⚠ A ancoragem final em [2] segue frágil (ver E4) |
| D8 | Organização do repositório | ATENDE PARCIALMENTE | Estrutura de R2 excelente (inclui `docs/` e `paper/`) | ⚠ README com números desatualizados (ver E-README na Seção 3) |
| D9 | Apresentação oral | FORA DE ESCOPO | — | — |

## 3. Checagens de integridade (Bloco E)

| ID | Resultado | Evidência | Severidade |
|----|-----------|-----------|------------|
| E1 | **ATENDE — sanado.** D1-v2 lista dois autores (Fábio Krein · Valdomiro Souza), dentro do intervalo 2–4 exigido por D2 | D1-v2, cabeçalho | — |
| E2 | **ATENDE.** 540 execuções, 122 inviáveis, 418 viáveis; todas as 18 médias de nós, 18 médias de tempo e 9 razões da Tabela 1 conferem exatamente com `results/results.csv` de R2 (ex.: 200×200/30%: 8,10 vs. 30,52 ms; razão 0,265 → 0,27). As frações de percolação do §3.2 (100%, 86% = 77/90, 47% = 42/90) conferem com o CSV, assim como "sem concentração em um tamanho" (grids inviáveis a 30%: 13/17/18 por tamanho). A imprecisão da Versão I ("predominantemente no 200×200 com 30%") foi **corrigida** pela caracterização via percolação | Análise pandas sobre R2 `results/results.csv` nesta avaliação | — |
| E3 | **ATENDE.** (a) e (b) inalterados e fiéis ao Teorema 1 e Lema 2 de D3. (c) A adição da referência [3] (Dijkstra, 1959) corrige a citação órfã da Versão I. Ressalva residual mantida: D3 §IV-A não nomeia Dijkstra; a frase de §5 "a otimalidade de [1]: Dijkstra é o caso h ≡ 0 do A\*" segue sendo inferência padrão da literatura, não afirmação literal de D3 | D1-v2 §2, §5; D3 §IV-A | P2 |
| E4 | **ATENDE PARCIALMENTE — gap persiste.** D1-v2 §5.1 reformula para "Ardiansyah et al. [2] observam o mesmo em malhas viárias: ganho em expansões nem sempre se traduz em tempo". Em D4, contudo, o A\* melhora **ambas** as métricas, e o tempo cai **mais** que proporcionalmente aos nós (Tabela 4 de D4: nós 8/11 ≈ −27%; tempo 1,9/2,8 ms ≈ −32%); D4 não observa o fenômeno alegado. A atribuição permanece infiel, agora agravada por afirmar que [2] "observa o mesmo" que um achado estatisticamente validado deste trabalho | D1-v2 §5.1; D4 Tabela 4 e §IV-C/D | **P1** |
| E5 | **ATENDE.** Definição do artigo ("cardinalidade dos nós removidos da fila, medida determinística") coincide com `len(visited)` em ambos os algoritmos de R2 (código idêntico ao de R1 neste ponto). O adendo "independente da máquina" é correto e verificado: `visited_nodes` e `path_cost` reproduzidos de forma bit-idêntica na re-execução da Versão I | R2 `src/dijkstra.py`, `src/astar.py` | — |
| E6 | **ATENDE — sanado.** Tabela 1 agora usa ponto exclusivamente como separador de milhar nos nós ("2.254", "5.479") e vírgula como decimal nos tempos ("2,23", "8,10") — convenção PT-BR internamente consistente | D1-v2 Tabela 1 | — |
| E7 | **ATENDE (verificação forte).** (i) `python -m src.significance` executado nesta avaliação sobre o CSV versionado regenerou a tabela de significância com **todos os valores idênticos** ao `significance.csv` versionado (estatísticas W, p-valores, razões, vereditos); (ii) a alegação central "todas as diferenças significativas (p < 0,001)" é verificável: maior p de Wilcoxon = 4,88×10⁻⁴; (iii) a direção por cenário confere: A\* mais lento nas três configurações a 10%, mais rápido nas seis a 20–30%, exatamente como §5.1 afirma; (iv) `TIMING_REPETITIONS = 10` com mediana em `experiments.py` corresponde à metodologia declarada em §3.2. Ressalva: `build_pdf.py` requer Chrome headless, não disponível neste ambiente — pipeline de PDF verificado apenas por inspeção de código | Execução real de `src.significance`; R2 `src/experiments.py`, `paper/build_pdf.py` | — |
| E-README *(nova checagem, regra 4)* | **NÃO ATENDE.** O README de R2 ("Principais resultados") mantém números da cronometragem antiga da Versão I: "~4–9% mais lento" a 10% (artigo/CSV atuais: 10–15%) e "~25% do tempo" em 200×200/30% (atual: 0,27×, i.e., 27%). A seção "Métricas avaliadas" também não menciona a mediana de 10 medições nem o teste de Wilcoxon, embora a "Estrutura" liste `significance.py`. Divergência numérica artigo ↔ repositório | R2 README "Principais resultados" vs. D1-v2 Tabela 1/§4.3 e CSV | **P1** |

## 4. Gaps priorizados

| Prioridade | Gap | Requisito violado (ID) | Recomendação acionável | Esforço estimado |
|------------|-----|------------------------|------------------------|------------------|
| P1 | Citação [2] segue sobre-interpretada ("observam o mesmo") | E4 / D7 | Reescrever a frase final de §5.1 para "Ardiansyah et al. [2] comparam as mesmas métricas em malha viária" ou remover a analogia, pois D4 reporta ganho de tempo mais que proporcional ao de expansões | 5 min |
| P1 | README de R2 com números da medição antiga | E-README / D8 | Atualizar "Principais resultados" do README com os valores da nova cronometragem (10–15% mais lento a 10%; ~27% do tempo a 200×200/30%) e adicionar bullet sobre mediana de 10 medições + Wilcoxon na seção "Métricas avaliadas" | 10 min |
| P1 | Referência [2] bibliograficamente incompleta | C2 | Completar a entrada [2]: "bit-Tech, v. 8, n. 2, p. 2974–2983, 2025. doi: 10.32877/bt.v8i2.3474" | 5 min |
| P1 | Repositório entregável ambíguo | B2 (rastreabilidade da entrega) | O artigo aponta para o fork (valdomirosouza), enquanto o repositório original (Fabexseven) não contém `significance.py`, `paper/` nem a nova cronometragem. Abrir PR do fork para o repositório principal (ou declarar oficialmente o fork como entregável ao professor) para que artigo e repositório de entrega coincidam | 15 min |
| P2 | Legendas das Figuras 1–2 dizem "sobre 30 sementes" | C4 / D6 | Alinhar as legendas das figuras com a da Tabela 1: "sobre as sementes com caminho viável" (12–30 por configuração) | 5 min |
| P2 | Atribuição de "Dijkstra = caso h ≡ 0" a [1] | E3(c) | Ajustar §5 para "o caso h ≡ 0 discutido em [1, §IV-A] equivale à busca de custo uniforme de [3]" | 5 min |

## 5. Observações complementares (fora da especificação)

1. A pasta `docs/` versiona "enunciado + artigos citados"; redistribuir PDFs de terceiros (IEEE, bit-Tech) em repositório público pode violar os termos de licença das editoras — considerar substituir por arquivo de links/DOIs.
2. O `paper_revisado.diff` versionado é uma prática exemplar de rastreabilidade de revisão, acima do exigido; mencioná-lo na resposta aos revisores/professor agrega valor.
3. O `significance.py` reporta também um teste t pareado como verificação complementar, mas o artigo cita apenas o Wilcoxon; uma nota de rodapé de meia linha ("o teste t pareado corrobora, p ≤ 2,6×10⁻⁷") aproveitaria o trabalho já feito.
4. O README informa "62%" de nós a 20% enquanto o artigo diz "~60%"; o CSV dá 61–64% conforme o tamanho — pequena divergência de arredondamento a alinhar junto com a atualização do README.
5. A observação de §5.2 sobre tamanho máximo da fronteira como métrica futura poderia ser instrumentada com uma linha de código (`max(len(queue))`) em trabalho futuro, dado que a infraestrutura de CSV já existe.

## 6. Veredicto final

- **Conformidade global:** 22 de 24 itens avaliáveis em ATENDE (Versão I: 17); 2 em ATENDE PARCIALMENTE (C2, D8); 0 em NÃO ATENDE nos blocos A–D. Os quatro gaps estruturais da Versão I (autoria única, complexidade ausente, pasta `paper/` inexistente, separador ambíguo) foram todos sanados.
- **Itens FORA DE ESCOPO:** B5, D9 (apresentação oral).
- **Recomendação: APTO COM AJUSTES MENORES** — os quatro P1 remanescentes são textuais/administrativos (uma frase no §5.1, uma entrada bibliográfica, atualização do README e consolidação R1↔R2), com esforço total estimado inferior a 40 minutos e sem impacto na base experimental, que está integralmente verificada e reprodutível, incluindo a nova camada de validação estatística.
