# 📊 Algorithmen Visualisierung

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![Status](https://img.shields.io/badge/Status-Aktiv-brightgreen.svg)]()

Interaktive Visualisierung **klassischer Algorithmen** — Sortieralgorithmen animieren, Suchalgorithmen vergleichen und Graphenalgorithmen (BFS, DFS, Dijkstra) auf echten Graphen ausführen. Alle Algorithmen sind in reinem Python implementiert und werden Schritt für Schritt in der Streamlit-App dargestellt.

## ✨ Features

- **🔄 Sortieralgorithmen animieren** — Bubble Sort, Quick Sort und Merge Sort mit Schritt-für-Schritt-Animation
- **🔍 Suchalgorithmen vergleichen** — Lineare Suche vs. Binäre Suche mit Komplexitätsvergleich
- **🕸️ Graphen visualisieren** — BFS, DFS und Dijkstra auf interaktiven Graphen mit farbiger Knotenmarkierung
- **📊 Komplexitätsanalyse** — O(n²) vs. O(n log n) live erleben
- **⚡ Performance-Vergleich** — Alle drei Sortieralgorithmen nebeneinander mit Metriken
- **✅ Getestet** — Unit-Tests für alle Algorithmen

## 🚀 Installation

```bash
# Repository klonen
git clone https://github.com/mark-baumann/algorithmen.git
cd algorithmen

# Virtuelle Umgebung erstellen
uv venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Abhängigkeiten installieren
uv pip install numpy matplotlib networkx streamlit pytest
```

## 🎯 Nutzung

```bash
# Streamlit-App starten
streamlit run app.py
```

Die App öffnet sich im Browser unter `http://localhost:8501`. Wähle einen Modus aus der Seitenleiste: Sortieren, Suchen oder Graphen.

## 🧪 Tests ausführen

```bash
pytest test_algorithms.py -v
```

## 🛠️ Tech-Stack

| Technologie | Einsatz |
|-------------|---------|
| **Python** | Alle Algorithmen in reinem Python implementiert |
| **NumPy** | Numerische Hilfsfunktionen |
| **Matplotlib** | Balkendiagramme für Sortieranimationen |
| **NetworkX** | Graph-Layout und -Visualisierung |
| **Streamlit** | Interaktive Web-App |
| **Pytest** | Test-Framework |

## 📁 Projektstruktur

```
algorithmen/
├── app.py                  # Streamlit-Hauptapp (3 Modi)
├── algorithms.py           # Alle Algorithmen-Implementierungen
└── test_algorithms.py      # Unit-Tests
```

## 📖 Enthaltene Algorithmen

### Sortieren
| Algorithmus | Komplexität (avg) | Komplexität (worst) | Stabil |
|-------------|-------------------|---------------------|--------|
| **Bubble Sort** | O(n²) | O(n²) | ✅ |
| **Quick Sort** | O(n log n) | O(n²) | ❌ |
| **Merge Sort** | O(n log n) | O(n log n) | ✅ |

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

*Algorithmen sind das Handwerkszeug jedes Entwicklers. Diese App macht abstrakte Konzepte durch Animation und interaktive Visualisierung greifbar.*
