# Algorithmen

Klassische Algorithmen in Python — implementiert zum Verstehen, nicht für den Produktiv-Einsatz.

## Enthaltene Algorithmen

### Sortieren
- **Bubble Sort** — O(n²), einfach, mit Early-Exit-Optimierung
- **Quick Sort** — O(n log n) average, Divide & Conquer
- **Merge Sort** — O(n log n), stabil

### Suchen
- **Binary Search** — O(log n), setzt sortiertes Array voraus

### Graphen
- **BFS** (Breitensuche) — kürzester Pfad in ungewichtetem Graphen
- **DFS** (Tiefensuche) — rekursiv
- **Dijkstra** — kürzeste Pfade in gewichtetem Graphen (Min-Heap)

### Dynamische Programmierung
- **Fibonacci** — O(n) mit DP statt O(2ⁿ) rekursiv
- **0/1 Rucksackproblem** — DP-Lösung O(n·W)
- **LCS** (Longest Common Subsequence) — DP-Lösung O(n·m)

## Ausführen

```bash
# Direkt ausführen (Demo)
python3 algorithms.py

# Tests ausführen
pip install pytest
pytest test_algorithms.py -v
```

## Struktur

```
algorithmen/
├── algorithms.py        # Alle Algorithmen + Demo-Main
├── test_algorithms.py   # pytest Unit-Tests
├── Djkstra.ipynb        # Jupyter Notebook: Dijkstra (ältere Variante)
└── README.md
```
