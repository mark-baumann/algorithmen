# 📊 Algorithmen — Google Colab Notebooks

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Colab](https://img.shields.io/badge/Google%20Colab-Open%20in%20Colab-F9AB00.svg)](https://colab.research.google.com/)

Interaktive **Jupyter Notebooks** zu klassischen Algorithmen — Sortier-, Such- und Graphenalgorithmen (BFS, DFS, Dijkstra) mit Erklärungen und Schritt-für-Schritt-Code. Alle Algorithmen sind in reinem Python implementiert und direkt in **Google Colab** ausführbar.

## ✨ Features

- **🔄 Sortieralgorithmen** — Bubble Sort, Quick Sort, Merge Sort und Heap Sort mit Laufzeitvergleich
- **🔍 Suchalgorithmen** — Lineare Suche vs. Binäre Suche mit Komplexitätsvergleich
- **🕸️ Graphenalgorithmen** — BFS, DFS und Dijkstra mit Erklärungen
- **📊 Komplexitätsanalyse** — O(n²) vs. O(n log n) live erleben
- **📓 Lern-Notebooks** — Sortier-, Such- und Graphenalgorithmen mit Erklärungen

## 🚀 In Google Colab öffnen

Jedes Notebook lässt sich direkt in Google Colab öffnen und ausführen:

| Notebook | Inhalt | Colab |
|----------|--------|-------|
| `sortieralgorithmen.ipynb` | Bubble Sort, Quick Sort, Merge Sort, Heap Sort, Binary Search | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mark-baumann/algorithmen/blob/main/sortieralgorithmen.ipynb) |
| `graphenalgorithmen.ipynb` | BFS, DFS, Dijkstra | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mark-baumann/algorithmen/blob/main/graphenalgorithmen.ipynb) |
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
├── sortieralgorithmen.ipynb       # Sortier- & Suchalgorithmen
├── graphenalgorithmen.ipynb       # BFS, DFS, Dijkstra
└── Djkstra.ipynb                  # Dijkstra (Kurzreferenz)
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
