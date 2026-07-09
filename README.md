# A\* vs Dijkstra — análise empírica

> Comparação experimental de **Dijkstra** e **A\*** para menor caminho em
> grids 2D com obstáculos aleatórios. Trabalho da disciplina de **Análise
> de Algoritmos** — Unisinos.

**Sumário:** [Descrição](#descrição) · [Principais resultados](#principais-resultados) · [Algoritmos](#algoritmos-implementados) · [Cenário experimental](#cenário-experimental) · [Métricas](#métricas-avaliadas) · [Instalação](#instalação) · [Rodar experimentos](#como-rodar-os-experimentos) · [Gerar gráficos](#como-gerar-os-gráficos) · [Significância](#como-rodar-o-teste-de-significância) · [Estrutura](#estrutura-do-repositório)

## Descrição

Este projeto compara experimentalmente os algoritmos **Dijkstra** (baseline) e
**A\*** (algoritmo principal) no problema de menor caminho em mapas
bidimensionais com obstáculos aleatórios. Os dois algoritmos retornam o
caminho ótimo; o objetivo é medir o ganho prático do A\* em relação ao
Dijkstra quando uma heurística admissível está disponível.

## Principais resultados

Resumo dos achados sobre as 540 execuções (detalhes nos gráficos em
`graphs/` e no relatório em `paper/`):

- **Custos de caminho idênticos** entre Dijkstra e A\* em todas as
  configurações — ambos retornam o caminho ótimo, como esperado.
- **A\* visita significativamente menos nós** que o Dijkstra. A vantagem
  cresce com a densidade de obstáculos: a 10% o A\* visita ~87% dos nós do
  Dijkstra, a 20% cerca de 62%, e a 30% apenas ~20–39%.
- **Em cenários grandes e com mais obstáculos, o A\* é claramente mais
  rápido** — em 200×200 a 30% de obstáculos, o A\* roda em ~27% do tempo do
  Dijkstra (≈3,8× mais rápido).
- **Em cenários fáceis (10% de obstáculos), o A\* é mais lento** em tempo
  de parede (~10–15%): o ganho em nós visitados não compensa o overhead
  por nó do cálculo da heurística.
- **A vantagem do A\* escala com o problema**: tanto o tamanho do grid
  quanto a densidade de obstáculos amplificam o ganho relativo.
- **Todas as diferenças de tempo são estatisticamente significativas**
  (teste de Wilcoxon pareado por semente, p < 0,001 nas nove configurações —
  ver `results/significance.csv`).

## Algoritmos implementados

Ambos foram implementados do zero, sem usar bibliotecas externas de grafos.

- **Dijkstra** (`src/dijkstra.py`) — busca uniforme com fila de prioridade
  (`heapq`). Custo de aresta fixo igual a 1.
- **A\*** (`src/astar.py`) — mesma estrutura do Dijkstra, mas com prioridade
  `f = g + h`, onde `h` é a distância de **Manhattan** até o objetivo
  (admissível e consistente para grids 4-conectados).
- **Grid e vizinhança** (`src/grid.py`) — geração de grid `n × n` com
  obstáculos aleatórios reprodutíveis por `seed`; vizinhança 4-conectada.

## Cenário experimental

| Parâmetro                | Valores                                     |
| ------------------------ | ------------------------------------------- |
| Tamanhos do grid         | 50 × 50, 100 × 100, 200 × 200               |
| Densidades de obstáculos | 10%, 20%, 30%                               |
| Repetições por cenário   | 30 (seeds `0..29`)                          |
| Conectividade            | 4 vizinhos (cima, baixo, esquerda, direita) |
| Início / objetivo        | `(0, 0)` → `(n-1, n-1)`                     |

Total: 3 × 3 × 30 × 2 algoritmos = **540 execuções**.

## Métricas avaliadas

- **Custo do caminho** (`path_cost`) — número de passos do caminho ótimo.
  Serve como sanidade: Dijkstra e A\* devem coincidir.
- **Nós visitados** (`visited_nodes`) — número de nós expandidos. É onde o
  A\* tipicamente vence.
- **Tempo de execução** (`runtime_ms`) — tempo de parede em milissegundos
  (`time.perf_counter`).

## Instalação

Requer **Python 3.9+**.

```bash
git clone https://github.com/Fabexseven/astar-dijkstra-analysis.git
cd astar-dijkstra-analysis

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

## Como rodar os experimentos

A partir da **raiz do projeto**:

```bash
python -m src.experiments
```

Isso (re)gera `results/results.csv` com uma linha por execução
(540 linhas + cabeçalho).

> O arquivo `results/results.csv` versionado contém os resultados usados no
> relatório. Rodar o comando acima sobrescreve o CSV; os números podem variar
> ligeiramente no tempo de execução por dependerem da máquina, mas
> `path_cost` e `visited_nodes` são determinísticos para cada seed.

## Como gerar os gráficos

A partir da **raiz do projeto**, depois de gerar o CSV:

```bash
python -m src.plots
```

Para cada taxa de obstáculo (10/20/30%) são gerados três PNGs em `graphs/`
(9 no total), sempre com média ± desvio padrão em função do tamanho do grid:

- `path_cost_*.png` — custo do caminho ótimo (coincide entre os dois).
- `visited_nodes_*.png` — nós expandidos (vantagem do A\*).
- `runtime_*.png` — tempo de execução.

## Como rodar o teste de significância

A partir da **raiz do projeto**, depois de gerar o CSV:

```bash
python -m src.significance
```

Pareia Dijkstra e A\* por `(tamanho, densidade, seed)` — mantendo apenas as
sementes solúveis por ambos — e aplica um teste de **Wilcoxon de postos
sinalizados** (com t pareado como verificação secundária) sobre `runtime_ms`
em cada configuração. Imprime uma tabela e grava `results/significance.csv`.

### Artigo (Google Docs)

- **Versão Editável:** <https://docs.google.com/document/d/1dzePI1h46R3mK-tsvD_SQ9BCKzldnLkK/edit>

## Estrutura do repositório

```
astar-dijkstra-analysis/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py         # marca `src` como pacote Python
│   ├── grid.py             # geração do grid + vizinhança 4-conectada
│   ├── dijkstra.py         # Dijkstra (baseline)
│   ├── astar.py            # A* com heurística de Manhattan
│   ├── experiments.py      # bateria de experimentos → results/results.csv
│   ├── plots.py            # gera os PNGs de graphs/ a partir do CSV
│   └── significance.py     # teste de Wilcoxon pareado → results/significance.csv
├── results/
│   ├── results.csv         # saída bruta dos experimentos (1 linha por run)
│   └── significance.csv    # significância dos tempos (A* vs Dijkstra) por cenário
├── graphs/                 # gráficos comparativos (PNG, 300 dpi)
│   ├── path_cost_{10,20,30}.png
│   ├── visited_nodes_{10,20,30}.png
│   └── runtime_{10,20,30}.png
├── paper/                  # o artigo (short-paper) e os pareceres de revisão
│   ├── Análise empírica de A∗ versus Dijkstra para menor caminho em grids 2D com obstáculos.pdf
|                           # versão em PDF do artigo
├── prompts/                # prompt de avaliação usado para gerar os pareceres
│   └── prompt-avaliacao-artigo-astar-dijkstra-v1.0.0.md
└── docs/                   # material de referência
    ├── TrabalhoI.pdf       # enunciado da disciplina
    ├── A_Formal_Basis_for_the_Heuristic_Determination_of_Minimum_Cost_Paths.pdf
    │                       #   Hart, Nilsson e Raphael (1968) — ref. [1]
    ├── Comparative_Analysis_of_Dijkstra_and_A_Algorithms_.pdf
    │                       #   Ardiansyah et al. (2025) — ref. [2]
    └── A_Note_on_Two_Problems_in_Connexion_with_Graphs.pdf
                            #   Dijkstra (1959) — ref. [3]
```
