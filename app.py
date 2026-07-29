"""
Streamlit-App: Algorithmen-Visualisierung
========================================
Sortieralgorithmen animieren, Suchalgorithmen vergleichen, Graphen visualisieren.
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
from pathlib import Path

# Repo-Pfad zum Importieren der Algorithmen
sys.path.insert(0, str(Path(__file__).parent))
from algorithms import (
    bubble_sort, quick_sort, merge_sort,
    binary_search, bfs, dfs, dijkstra,
    fibonacci, knapsack, longest_common_subsequence,
)

st.set_page_config(
    page_title="Algorithmen-Visualisierung",
    page_icon="🔬",
    layout="wide",
)

st.title("🔬 Algorithmen-Visualisierung")
st.markdown("### Sortieren · Suchen · Graphen · Dynamische Programmierung")

# ── Sidebar: Navigation ──
kategorie = st.sidebar.radio(
    "📂 Kategorie wählen",
    ["Sortieralgorithmen", "Suchalgorithmen", "Graphen", "Dynamische Programmierung"],
)

# ═══════════════════════════════════════════════════════════════
# SORTIERALGORITHMEN
# ═══════════════════════════════════════════════════════════════
if kategorie == "Sortieralgorithmen":
    st.header("📊 Sortieralgorithmen animieren")

    col1, col2 = st.columns([1, 2])

    with col1:
        algo = st.selectbox(
            "Algorithmus",
            ["Bubble Sort", "Quick Sort", "Merge Sort"],
        )
        n_elements = st.slider("Anzahl Elemente", 5, 50, 20)
        geschwindigkeit = st.slider("Geschwindigkeit (ms)", 10, 500, 100)
        seed = st.number_input("Zufalls-Seed", 0, 9999, 42)

        if st.button("▶️ Sortierung starten", use_container_width=True):
            st.session_state.sort_running = True
            st.session_state.sort_step = 0

    with col2:
        if "sort_running" not in st.session_state:
            st.session_state.sort_running = False

        # Array generieren
        rng = np.random.RandomState(seed)
        arr = rng.randint(1, 100, n_elements).tolist()

        # Sortieralgorithmus mit Schritt-Tracking
        def bubble_sort_steps(arr):
            arr = arr.copy()
            n = len(arr)
            steps = [arr.copy()]
            for i in range(n):
                swapped = False
                for j in range(n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                        steps.append(arr.copy())
                if not swapped:
                    break
            return steps

        def quick_sort_steps(arr):
            arr = arr.copy()
            steps = [arr.copy()]

            def _qs(a, lo, hi):
                if lo < hi:
                    pivot = a[(lo + hi) // 2]
                    i, j = lo, hi
                    while i <= j:
                        while a[i] < pivot:
                            i += 1
                        while a[j] > pivot:
                            j -= 1
                        if i <= j:
                            a[i], a[j] = a[j], a[i]
                            steps.append(a.copy())
                            i += 1
                            j -= 1
                    _qs(a, lo, j)
                    _qs(a, i, hi)

            _qs(arr, 0, len(arr) - 1)
            return steps

        def merge_sort_steps(arr):
            arr = arr.copy()
            steps = [arr.copy()]

            def _ms(a, lo, hi):
                if lo < hi:
                    mid = (lo + hi) // 2
                    _ms(a, lo, mid)
                    _ms(a, mid + 1, hi)
                    # Merge
                    left = a[lo:mid + 1]
                    right = a[mid + 1:hi + 1]
                    i = j = 0
                    k = lo
                    while i < len(left) and j < len(right):
                        if left[i] <= right[j]:
                            a[k] = left[i]
                            i += 1
                        else:
                            a[k] = right[j]
                            j += 1
                        k += 1
                        steps.append(a.copy())
                    while i < len(left):
                        a[k] = left[i]
                        i += 1
                        k += 1
                        steps.append(a.copy())
                    while j < len(right):
                        a[k] = right[j]
                        j += 1
                        k += 1
                        steps.append(a.copy())

            _ms(arr, 0, len(arr) - 1)
            return steps

        # Schritte berechnen
        if algo == "Bubble Sort":
            steps = bubble_sort_steps(arr)
        elif algo == "Quick Sort":
            steps = quick_sort_steps(arr)
        else:
            steps = merge_sort_steps(arr)

        st.markdown(f"**{len(steps)} Schritte** | Algorithmus: **{algo}** | O-Komplexität: **{'O(n²)' if algo == 'Bubble Sort' else 'O(n log n)'}**")

        # Animation
        chart_placeholder = st.empty()
        progress_bar = st.progress(0)

        if st.session_state.sort_running:
            for i, step_arr in enumerate(steps):
                fig, ax = plt.subplots(figsize=(10, 4))
                colors = ['#4ECDC4'] * len(step_arr)
                # Letzte i Elemente sind sortiert (bei Bubble)
                if algo == "Bubble Sort":
                    for k in range(len(step_arr) - i % (len(step_arr) + 1), len(step_arr)):
                        if k >= 0:
                            colors[k] = '#FF6B6B'
                bars = ax.bar(range(len(step_arr)), step_arr, color=colors, edgecolor='white')
                ax.set_ylim(0, max(arr) * 1.1)
                ax.set_xlabel("Index")
                ax.set_ylabel("Wert")
                ax.set_title(f"{algo} — Schritt {i + 1}/{len(steps)}")
                chart_placeholder.pyplot(fig)
                plt.close(fig)
                progress_bar.progress((i + 1) / len(steps))
                time.sleep(geschwindigkeit / 1000)

            st.success(f"✅ Sortierung abgeschlossen! {len(steps)} Schritte.")

        # Vergleich der Algorithmen
        st.markdown("---")
        st.subheader("📈 Algorithmen-Vergleich")

        if st.button("⏱️ Laufzeit messen", use_container_width=True):
            import timeit

            test_arr = rng.randint(1, 1000, 200).tolist()

            t_bubble = timeit.timeit(lambda: bubble_sort(test_arr), number=10) / 10
            t_quick = timeit.timeit(lambda: quick_sort(test_arr), number=100) / 100
            t_merge = timeit.timeit(lambda: merge_sort(test_arr), number=100) / 100

            fig, ax = plt.subplots(figsize=(8, 4))
            algos = ['Bubble Sort\nO(n²)', 'Quick Sort\nO(n log n)', 'Merge Sort\nO(n log n)']
            times = [t_bubble * 1000, t_quick * 1000, t_merge * 1000]
            colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
            ax.bar(algos, times, color=colors, edgecolor='white')
            ax.set_ylabel("Zeit (ms)")
            ax.set_title("Laufzeitvergleich (200 Elemente)")
            for i, v in enumerate(times):
                ax.text(i, v + 0.1, f"{v:.2f} ms", ha='center')
            st.pyplot(fig)
            plt.close(fig)

# ═══════════════════════════════════════════════════════════════
# SUCHALGORITHMEN
# ═══════════════════════════════════════════════════════════════
elif kategorie == "Suchalgorithmen":
    st.header("🔍 Suchalgorithmen vergleichen")

    col1, col2 = st.columns([1, 2])

    with col1:
        array_size = st.slider("Array-Größe", 10, 100, 30)
        target = st.number_input("Zielwert suchen", 1, 100, 50)
        search_type = st.radio("Suchverfahren", ["Lineare Suche", "Binäre Suche"])

    with col2:
        # Sortiertes Array
        arr = sorted(np.random.RandomState(42).randint(1, 100, array_size).tolist())

        st.markdown(f"**Sortiertes Array** ({array_size} Elemente):")
        st.code(str(arr))

        if search_type == "Lineare Suche":
            st.markdown("### 🔄 Lineare Suche — O(n)")
            steps = 0
            found_idx = -1
            for i, val in enumerate(arr):
                steps += 1
                if val == target:
                    found_idx = i
                    break

            if found_idx >= 0:
                st.success(f"✅ Gefunden an Index **{found_idx}** nach **{steps}** Schritten")
            else:
                st.warning(f"❌ Nicht gefunden nach **{steps}** Schritten")
        else:
            st.markdown("### 🎯 Binäre Suche — O(log n)")
            result = binary_search(arr, target)
            max_steps = int(np.ceil(np.log2(len(arr))))
            if result >= 0:
                st.success(f"✅ Gefunden an Index **{result}** (max. {max_steps} Schritte)")
            else:
                st.warning(f"❌ Nicht gefunden (max. {max_steps} Schritte)")

        # Visualisierung
        fig, ax = plt.subplots(figsize=(10, 4))
        colors = ['#4ECDC4'] * len(arr)
        if search_type == "Binäre Suche" and result >= 0:
            colors[result] = '#FF6B6B'
        elif search_type == "Lineare Suche":
            for i in range(steps):
                if i < len(arr):
                    colors[i] = '#FFE66D'
            if found_idx >= 0:
                colors[found_idx] = '#FF6B6B'

        ax.bar(range(len(arr)), arr, color=colors, edgecolor='white')
        ax.axhline(y=target, color='red', linestyle='--', label=f'Ziel: {target}')
        ax.set_xlabel("Index")
        ax.set_ylabel("Wert")
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    # Komplexitätsvergleich
    st.markdown("---")
    st.subheader("📊 Komplexitätsvergleich")

    sizes = [10, 50, 100, 500, 1000]
    linear_steps = sizes
    binary_steps = [int(np.ceil(np.log2(s))) for s in sizes]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(sizes, linear_steps, 'o-', color='#FF6B6B', label='Lineare Suche O(n)')
    ax.plot(sizes, binary_steps, 's-', color='#4ECDC4', label='Binäre Suche O(log n)')
    ax.set_xlabel("Array-Größe (n)")
    ax.set_ylabel("Maximale Schritte")
    ax.set_title("Suchkomplexität im Vergleich")
    ax.legend()
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)

# ═══════════════════════════════════════════════════════════════
# GRAPHEN
# ═══════════════════════════════════════════════════════════════
elif kategorie == "Graphen":
    st.header("🕸️ Graphen visualisieren")

    col1, col2 = st.columns([1, 2])

    with col1:
        graph_preset = st.selectbox(
            "Graph wählen",
            ["Standard-Graph (ungerichtet)", "Gewichteter Graph (Dijkstra)", "Eigener Graph"],
        )

        algo_choice = st.radio(
            "Algorithmus",
            ["BFS (Breitensuche)", "DFS (Tiefensuche)", "Dijkstra (kürzeste Pfade)"],
        )

        if graph_preset == "Standard-Graph (ungerichtet)":
            graph = {
                "A": ["B", "C"],
                "B": ["A", "D", "E"],
                "C": ["A", "F"],
                "D": ["B"],
                "E": ["B", "F"],
                "F": ["C", "E"],
            }
            start_node = st.selectbox("Startknoten", list(graph.keys()), index=0)
        elif graph_preset == "Gewichteter Graph (Dijkstra)":
            graph = {
                "A": {"B": 4, "C": 2},
                "B": {"A": 4, "C": 1, "D": 5},
                "C": {"A": 2, "B": 1, "D": 8, "E": 10},
                "D": {"B": 5, "C": 8, "E": 2},
                "E": {"C": 10, "D": 2},
            }
            start_node = st.selectbox("Startknoten", list(graph.keys()), index=0)
        else:
            st.info("Definiere deinen eigenen Graphen im Code.")

    with col2:
        # Graph visualisieren mit NetworkX-ähnlichem Layout
        def draw_graph(graph, highlight_nodes=None, highlight_edges=None, title="Graph"):
            if highlight_nodes is None:
                highlight_nodes = []
            if highlight_edges is None:
                highlight_edges = []

            # Einfaches Kreis-Layout
            nodes = list(graph.keys())
            n = len(nodes)
            angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
            pos = {node: (np.cos(a), np.sin(a)) for node, a in zip(nodes, angles)}

            fig, ax = plt.subplots(figsize=(8, 8))

            # Kanten zeichnen
            drawn_edges = set()
            for node, neighbors in graph.items():
                if isinstance(neighbors, dict):  # Gewichtet
                    for neighbor, weight in neighbors.items():
                        edge_key = tuple(sorted([node, neighbor]))
                        if edge_key in drawn_edges:
                            continue
                        drawn_edges.add(edge_key)
                        x1, y1 = pos[node]
                        x2, y2 = pos[neighbor]
                        color = '#FF6B6B' if (node, neighbor) in highlight_edges or (neighbor, node) in highlight_edges else '#888888'
                        ax.plot([x1, x2], [y1, y2], '-', color=color, linewidth=2, alpha=0.6)
                        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                        ax.text(mx, my, str(weight), fontsize=9, ha='center', va='center',
                                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
                else:  # Ungerichtet
                    for neighbor in neighbors:
                        edge_key = tuple(sorted([node, neighbor]))
                        if edge_key in drawn_edges:
                            continue
                        drawn_edges.add(edge_key)
                        x1, y1 = pos[node]
                        x2, y2 = pos[neighbor]
                        color = '#FF6B6B' if (node, neighbor) in highlight_edges or (neighbor, node) in highlight_edges else '#888888'
                        ax.plot([x1, x2], [y1, y2], '-', color=color, linewidth=2, alpha=0.6)

            # Knoten zeichnen
            for node, (x, y) in pos.items():
                color = '#FF6B6B' if node in highlight_nodes else '#4ECDC4'
                ax.scatter(x, y, s=800, color=color, edgecolors='white', linewidth=2, zorder=5)
                ax.text(x, y, node, fontsize=14, ha='center', va='center', fontweight='bold', color='white')

            ax.set_xlim(-1.5, 1.5)
            ax.set_ylim(-1.5, 1.5)
            ax.set_aspect('equal')
            ax.axis('off')
            ax.set_title(title, fontsize=14)
            return fig

        if graph_preset == "Standard-Graph (ungerichtet)":
            if algo_choice == "BFS (Breitensuche)":
                result = bfs(graph, start_node)
                st.markdown(f"**BFS ab '{start_node}'**: `{' → '.join(result)}`")
                fig = draw_graph(graph, highlight_nodes=result, title=f"BFS ab {start_node}")
                st.pyplot(fig)
                plt.close(fig)

            elif algo_choice == "DFS (Tiefensuche)":
                result = dfs(graph, start_node)
                st.markdown(f"**DFS ab '{start_node}'**: `{' → '.join(result)}`")
                fig = draw_graph(graph, highlight_nodes=result, title=f"DFS ab {start_node}")
                st.pyplot(fig)
                plt.close(fig)
            else:
                st.warning("Dijkstra benötigt einen gewichteten Graphen. Bitte wähle den gewichteten Graphen.")

        elif graph_preset == "Gewichteter Graph (Dijkstra)":
            if algo_choice == "Dijkstra (kürzeste Pfade)":
                result = dijkstra(graph, start_node)
                st.markdown(f"**Dijkstra ab '{start_node}'**:")
                for node, dist in sorted(result.items()):
                    st.markdown(f"- `{start_node} → {node}`: **{dist:.0f}**")
                fig = draw_graph(graph, highlight_nodes=list(result.keys()), title=f"Dijkstra ab {start_node}")
                st.pyplot(fig)
                plt.close(fig)
            else:
                st.info("BFS/DFS funktionieren auch auf gewichteten Graphen (Gewichte werden ignoriert).")
                unweighted = {k: list(v.keys()) for k, v in graph.items()}
                if algo_choice == "BFS (Breitensuche)":
                    result = bfs(unweighted, start_node)
                else:
                    result = dfs(unweighted, start_node)
                st.markdown(f"**{algo_choice} ab '{start_node}'**: `{' → '.join(result)}`")
                fig = draw_graph(graph, highlight_nodes=result, title=f"{algo_choice} ab {start_node}")
                st.pyplot(fig)
                plt.close(fig)

# ═══════════════════════════════════════════════════════════════
# DYNAMISCHE PROGRAMMIERUNG
# ═══════════════════════════════════════════════════════════════
elif kategorie == "Dynamische Programmierung":
    st.header("🧩 Dynamische Programmierung")

    tab1, tab2, tab3 = st.tabs(["Fibonacci", "Rucksackproblem", "LCS"])

    with tab1:
        st.subheader("🐇 Fibonacci — DP vs. Rekursiv")

        n = st.slider("n (Fibonacci-Zahl)", 0, 50, 10, key="fib_n")

        col_a, col_b = st.columns(2)
        with col_a:
            t0 = time.time()
            result = fibonacci(n)
            t_dp = (time.time() - t0) * 1000
            st.metric("DP O(n)", f"F({n}) = {result}", f"{t_dp:.3f} ms")

        with col_b:
            # Rekursive Berechnung (nur für kleine n)
            if n <= 30:
                def fib_rec(n):
                    if n <= 1:
                        return n
                    return fib_rec(n - 1) + fib_rec(n - 2)

                t0 = time.time()
                result_rec = fib_rec(n)
                t_rec = (time.time() - t0) * 1000
                st.metric("Rekursiv O(2ⁿ)", f"F({n}) = {result_rec}", f"{t_rec:.1f} ms")
            else:
                st.warning("⚠️ Rekursive Berechnung für n > 30 zu langsam")

        # Fibonacci-Werte visualisieren
        values = [fibonacci(i) for i in range(min(n + 1, 20))]
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.bar(range(len(values)), values, color='#4ECDC4', edgecolor='white')
        ax.set_xlabel("n")
        ax.set_ylabel("F(n)")
        ax.set_title("Fibonacci-Zahlen")
        st.pyplot(fig)
        plt.close(fig)

    with tab2:
        st.subheader("🎒 0/1 Rucksackproblem")

        col1, col2 = st.columns(2)
        with col1:
            capacity = st.slider("Kapazität", 10, 100, 50, key="knap_cap")
            num_items = st.slider("Anzahl Gegenstände", 3, 8, 4, key="knap_items")

        # Zufällige Gegenstände
        rng = np.random.RandomState(42)
        values = rng.randint(10, 100, num_items).tolist()
        weights = rng.randint(5, 30, num_items).tolist()

        with col2:
            st.markdown("**Gegenstände:**")
            for i, (v, w) in enumerate(zip(values, weights)):
                st.markdown(f"- Item {i + 1}: Wert **{v}**, Gewicht **{w}** (Ratio: {v / w:.1f})")

        result = knapsack(values, weights, capacity)
        st.success(f"💰 Maximaler Wert bei Kapazität {capacity}: **{result}**")

        # Visualisierung
        fig, ax = plt.subplots(figsize=(8, 4))
        x = np.arange(num_items)
        width = 0.35
        ax.bar(x - width / 2, values, width, label='Wert', color='#4ECDC4', edgecolor='white')
        ax.bar(x + width / 2, weights, width, label='Gewicht', color='#FF6B6B', edgecolor='white')
        ax.set_xlabel("Gegenstand")
        ax.set_ylabel("Wert / Gewicht")
        ax.set_title("Rucksackproblem — Gegenstände")
        ax.set_xticks(x)
        ax.set_xticklabels([f"Item {i + 1}" for i in range(num_items)])
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    with tab3:
        st.subheader("📝 Longest Common Subsequence (LCS)")

        col1, col2 = st.columns(2)
        with col1:
            str_a = st.text_input("String A", "ABCDGH")
        with col2:
            str_b = st.text_input("String B", "AEDFHR")

        if str_a and str_b:
            result = longest_common_subsequence(str_a, str_b)
            st.metric("LCS-Länge", result)

            # DP-Tabelle visualisieren
            m, n = len(str_a), len(str_b)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if str_a[i - 1] == str_b[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            fig, ax = plt.subplots(figsize=(max(6, n + 1), max(4, m + 1)))
            im = ax.imshow(dp, cmap='YlOrRd', aspect='auto')
            ax.set_xticks(range(n + 1))
            ax.set_xticklabels([''] + list(str_b))
            ax.set_yticks(range(m + 1))
            ax.set_yticklabels([''] + list(str_a))
            ax.set_xlabel("String B")
            ax.set_ylabel("String A")
            ax.set_title(f"DP-Tabelle — LCS = {result}")
            for i in range(m + 1):
                for j in range(n + 1):
                    ax.text(j, i, dp[i][j], ha='center', va='center', fontsize=10)
            plt.colorbar(im, ax=ax)
            st.pyplot(fig)
            plt.close(fig)

st.sidebar.markdown("---")
st.sidebar.markdown("📁 **Repo:** [algorithmen](https://github.com/mark-baumann/algorithmen)")
st.sidebar.markdown("🐍 **Python 3.13** · **Streamlit** · **Matplotlib**")
