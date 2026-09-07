# 📊 Algorithmen — Google Colab Notebooks

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Colab](https://img.shields.io/badge/Google%20Colab-Open%20in%20Colab-F9AB00.svg)](https://colab.research.google.com/)

Interaktive **Jupyter Notebooks** zu klassischen Algorithmen — modular aufgebaut: **ein Notebook pro Algorithmus**. Sortier-, Such- und Graphenalgorithmen (BFS, DFS, Dijkstra) mit Erklärungen und Schritt-für-Schritt-Code. Alle Algorithmen sind in reinem Python implementiert und direkt in **Google Colab** ausführbar.

## ✨ Features

- **🔄 Sortieralgorithmen** — Bubble Sort, Quick Sort, Merge Sort und Heap Sort
- **🔍 Suchalgorithmen** — Lineare Suche und Binäre Suche
- **🕸️ Graphenalgorithmen** — BFS, DFS und Dijkstra
- **📓 Modular** — ein eigenes Notebook pro Algorithmus, wie `Djkstra.ipynb`

## 🚀 In Google Colab öffnen

Jedes Notebook lässt sich direkt in Google Colab öffnen und ausführen:

| Notebook | Inhalt | Colab |
|----------|--------|-------|
| `bubble_sort.ipynb` | Bubble Sort | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mark-baumann/algorithmen/blob/main/bubble_sort.ipynb) |
| `quick_sort.ipynb` | Quick Sort | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mark-baumann/algorithmen/blob/main/quick_sort.ipynb) |
| `merge_sort.ipynb` | Merge Sort | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mark-baumann/algorithmen/blob/main/merge_sort.ipynb) |
| `heap_sort.ipynb` | Heap Sort | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mark-baumann/algorithmen/blob/main/heap_sort.ipynb) |
| `lineare_suche.ipynb` | Lineare Suche | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mark-baumann/algorithmen/blob/main/lineare_suche.ipynb) |
| `binaere_suche.ipynb` | Binäre Suche | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mark-baumann/algorithmen/blob/main/binaere_suche.ipynb) |
| `bfs.ipynb` | BFS (Breitensuche) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mark-baumann/algorithmen/blob/main/bfs.ipynb) |
| `dfs.ipynb` | DFS (Tiefensuche) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mark-baumann/algorithmen/blob/main/dfs.ipynb) |
| `Djkstra.ipynb` | Dijkstra (Kurzreferenz) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mark-baumann/algorithmen/blob/main/Djkstra.ipynb) |

> 💡 **Tipp:** In Colab: Datei → In Drive speichern → mit GPU/TPU ausführen.

## 🛠️ Lokal ausführen (optional)

```bash
git clone https://github.com/mark-baumann/algorithmen.git
cd algorithmen
uv venv
source .venv/bin/activate
uv pip install jupyter numpy matplotlib
jupyter notebook
```

## 📁 Projektstruktur

```
algorithmen/
├── bubble_sort.ipynb      # Bubble Sort
├── quick_sort.ipynb       # Quick Sort
├── merge_sort.ipynb       # Merge Sort
├── heap_sort.ipynb        # Heap Sort
├── lineare_suche.ipynb    # Lineare Suche
├── binaere_suche.ipynb    # Binäre Suche
├── bfs.ipynb              # BFS (Breitensuche)
├── dfs.ipynb              # DFS (Tiefensuche)
└── Djkstra.ipynb          # Dijkstra (Kurzreferenz)
```

## 📖 Enthaltene Algorithmen

### Sortieren
| Algorithmus | Komplexität (avg) | Komplexität (worst) | Stabil |
|-------------|-------------------|---------------------|--------|
| **Bubble Sort** | O(n²) | O(n²) | ✅ |
| **Quick Sort** | O(n log n) | O(n²) | ❌ |
| **Merge Sort** | O(n log n) | O(n log n) | ✅ |
| **Heap Sort** | O(n log n) | O(n log n) | ❌ |

### Suchen
| Algorithmus | Komplexität | Voraussetzung |
|-------------|-------------|---------------|
| **Lineare Suche** | O(n) | Keine |
| **Binäre Suche** | O(log n) | Sortiertes Array |

### Graphen
| Algorithmus | Komplexität | Anwendung |
|-------------|-------------|-----------|
| **BFS** (Breitensuche) | O(V + E) | Kürzeste Pfade (ungewichtet), Level-Order |
| **DFS** (Tiefensuche) | O(V + E) | Zyklen-Erkennung, Topologische Sortierung |
| **Dijkstra** | O((V+E) log V) | Kürzeste Pfade (gewichtet, positiv) |

## 👤 Autor

**Mark Baumann** — [GitHub](https://github.com/mark-baumann)

---

*Algorithmen sind das Handwerkszeug jedes Entwicklers. Diese Notebooks machen abstrakte Konzepte durch Code und Erklärungen greifbar.*
