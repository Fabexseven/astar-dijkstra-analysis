# A* vs Dijkstra — análise empírica

Comparação experimental dos algoritmos **Dijkstra** e **A\*** (com heurística de Manhattan) em grids 2D com obstáculos aleatórios.

Trabalho da disciplina de Algoritmos — Unisinos.

## Estrutura

```
src/
  grid.py         # geração do grid + vizinhos
  dijkstra.py     # Dijkstra
  astar.py        # A* com heurística de Manhattan
  experiments.py  # bateria de experimentos -> results/results.csv
  plots.py        # gera os gráficos a partir do CSV
results/
  results.csv     # saída bruta dos experimentos
graphs/           # gráficos (path_cost, runtime, visited_nodes) por taxa de obstáculo
paper/            # relatório
```

## Configuração dos experimentos

- Tamanhos de grid: `50`, `100`, `200`
- Taxas de obstáculos: `10%`, `20%`, `30%`
- Repetições por configuração: `30` (seeds `0..29`)
- Métricas coletadas: caminho encontrado, custo do caminho, nós visitados, tempo de execução (ms)

## Como rodar

```bash
pip install -r requirements.txt

# 1) gera results/results.csv
cd src && python experiments.py

# 2) gera os PNGs em graphs/
python plots.py
```

## Resultados

Para cada taxa de obstáculo (10/20/30%) os gráficos em `graphs/` mostram média ± desvio padrão em função do tamanho do grid:

- `path_cost_*.png` — custo do caminho ótimo (deve coincidir entre os dois)
- `runtime_*.png` — tempo de execução
- `visited_nodes_*.png` — nós expandidos (onde A\* tipicamente vence)
