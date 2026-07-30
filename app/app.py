"""
Streamlit-App: Algorithmen
==========================
Sortieralgorithmen animieren, Suchalgorithmen vergleichen, Graphen visualisieren.
"""

import heapq
import random
import time
from collections import deque

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import streamlit as st


def bfs(graph, start):
    """Breitensuche — kürzester Pfad in ungewichtetem Graphen."""
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def dfs(graph, start, visited=None):
    """Tiefensuche — rekursiv."""
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))
    return order


def dijkstra(graph, start):
    """Dijkstra — kürzeste Pfade in gewichtetem Graphen."""
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in graph.get(node, {}).items():
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist


def binary_search(arr, target):
    """Binäre Suche — O(log n)."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def bubble_sort(arr):
    """Bubble Sort — O(n^2)."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def quick_sort(arr):
    """Quick Sort — O(n log n) average."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """Merge Sort — O(n log n), stabil."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def fibonacci(n):
    """Fibonacci — dynamische Programmierung, O(n)."""
    if n < 0:
        return -1
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def knapsack(values, weights, capacity):
    """0/1 Rucksackproblem — dynamische Programmierung."""
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


def longest_common_subsequence(s1, s2):
    """Längste gemeinsame Teilsequenz — dynamische Programmierung."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


# ── Page Config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Algorithmen Visualisierung",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Algorithmen Visualisierung")
st.markdown("Sortieren · Suchen · Graphen · Dynamische Programmierung")

# ── Sidebar: Modus ───────────────────────────────────────────
mode = st.sidebar.selectbox(
    "Modus wählen",
    ["Sortieralgorithmen animieren", "Suchalgorithmen vergleichen", "Graphen visualisieren"],
)

# ═══════════════════════════════════════════════════════════════
# 1. Sortieralgorithmen animieren
# ═══════════════════════════════════════════════════════════════

if mode == "Sortieralgorithmen animieren":
    st.header("🔄 Sortieralgorithmen animieren")

    col1, col2 = st.columns(2)
    with col1:
        algorithm = st.selectbox(
            "Algorithmus",
            ["Bubble Sort", "Quick Sort", "Merge Sort", "Alle drei vergleichen"],
        )
    with col2:
        array_size = st.slider("Array-Größe", 5, 50, 20)
        speed = st.slider("Geschwindigkeit (ms)", 10, 500, 100, 10)

    if st.button("🔄 Neues Array generieren", use_container_width=True):
        st.session_state.sort_array = [random.randint(1, 100) for _ in range(array_size)]

    if "sort_array" not in st.session_state:
        st.session_state.sort_array = [random.randint(1, 100) for _ in range(array_size)]

    arr = st.session_state.sort_array.copy()

    # ── Visualisierung ───────────────────────────────────────

    def plot_array(arr_data, title, highlight=None, color_map=None):
        fig, ax = plt.subplots(figsize=(10, 4))
        colors = ["#2196F3"] * len(arr_data)
        if highlight is not None:
            for idx in highlight:
                if 0 <= idx < len(colors):
                    colors[idx] = "#FF5722"
        if color_map:
            for idx, c in color_map.items():
                if 0 <= idx < len(colors):
                    colors[idx] = c
        ax.bar(range(len(arr_data)), arr_data, color=colors)
        ax.set_title(title)
        ax.set_xlabel("Index")
        ax.set_ylabel("Wert")
        ax.set_ylim(0, max(arr_data) * 1.1 if arr_data else 10)
        return fig

    # ── Bubble Sort ──────────────────────────────────────────
    def bubble_sort_animate(arr):
        arr = arr.copy()
        n = len(arr)
        steps = []
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                steps.append(("compare", arr.copy(), [j, j+1]))
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    steps.append(("swap", arr.copy(), [j, j+1]))
            if not swapped:
                break
        steps.append(("done", arr.copy(), list(range(n))))
        return steps

    # ── Quick Sort ───────────────────────────────────────────
    def quick_sort_animate(arr):
        arr = arr.copy()
        steps = []

        def _qs(a, lo, hi):
            if lo >= hi:
                return
            pivot = a[(lo + hi) // 2]
            steps.append(("pivot", a.copy(), [(lo + hi) // 2]))
            i, j = lo, hi
            while i <= j:
                while a[i] < pivot:
                    i += 1
                while a[j] > pivot:
                    j -= 1
                if i <= j:
                    a[i], a[j] = a[j], a[i]
                    steps.append(("swap", a.copy(), [i, j]))
                    i += 1
                    j -= 1
            _qs(a, lo, j)
            _qs(a, i, hi)

        _qs(arr, 0, len(arr) - 1)
        steps.append(("done", arr.copy(), list(range(len(arr)))))
        return steps

    # ── Merge Sort ───────────────────────────────────────────
    def merge_sort_animate(arr):
        arr = arr.copy()
        steps = []

        def _ms(a, lo, hi):
            if hi - lo <= 1:
                return a[lo:hi]
            mid = (lo + hi) // 2
            steps.append(("divide", a.copy(), list(range(lo, hi))))
            left = _ms(a, lo, mid)
            right = _ms(a, mid, hi)
            # Merge
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            a[lo:hi] = result
            steps.append(("merge", a.copy(), list(range(lo, hi))))
            return result

        _ms(arr, 0, len(arr))
        steps.append(("done", arr.copy(), list(range(len(arr)))))
        return steps

    # ── Ausführung ───────────────────────────────────────────
    if algorithm == "Bubble Sort":
        if st.button("▶️ Bubble Sort starten", type="primary"):
            steps = bubble_sort_animate(arr)
            plot_placeholder = st.empty()
            status = st.empty()

            for i, (action, state, highlight) in enumerate(steps):
                title = f"Bubble Sort — Schritt {i+1}/{len(steps)}: {action}"
                fig = plot_array(state, title, highlight)
                plot_placeholder.pyplot(fig)
                status.text(f"Vergleiche: {sum(1 for s in steps[:i+1] if s[0]=='compare')} | Swaps: {sum(1 for s in steps[:i+1] if s[0]=='swap')}")
                time.sleep(speed / 1000)
                plt.close(fig)

            status.text(f"✅ Bubble Sort abgeschlossen! Vergleiche: {sum(1 for s in steps if s[0]=='compare')} | Swaps: {sum(1 for s in steps if s[0]=='swap')}")

    elif algorithm == "Quick Sort":
        if st.button("▶️ Quick Sort starten", type="primary"):
            steps = quick_sort_animate(arr)
            plot_placeholder = st.empty()
            status = st.empty()

            for i, (action, state, highlight) in enumerate(steps):
                title = f"Quick Sort — Schritt {i+1}/{len(steps)}: {action}"
                fig = plot_array(state, title, highlight)
                plot_placeholder.pyplot(fig)
                status.text(f"Schritt {i+1}/{len(steps)} — {action}")
                time.sleep(speed / 1000)
                plt.close(fig)

            status.text("✅ Quick Sort abgeschlossen!")

    elif algorithm == "Merge Sort":
        if st.button("▶️ Merge Sort starten", type="primary"):
            steps = merge_sort_animate(arr)
            plot_placeholder = st.empty()
            status = st.empty()

            for i, (action, state, highlight) in enumerate(steps):
                title = f"Merge Sort — Schritt {i+1}/{len(steps)}: {action}"
                fig = plot_array(state, title, highlight)
                plot_placeholder.pyplot(fig)
                status.text(f"Schritt {i+1}/{len(steps)} — {action}")
                time.sleep(speed / 1000)
                plt.close(fig)

            status.text("✅ Merge Sort abgeschlossen!")

    elif algorithm == "Alle drei vergleichen" and st.button("▶️ Alle drei vergleichen", type="primary"):
        col1, col2, col3 = st.columns(3)

        # Bubble
        with col1:
            st.subheader("🫧 Bubble Sort")
            steps = bubble_sort_animate(arr)
            fig = plot_array(steps[-1][1], "Bubble Sort — Fertig", list(range(len(arr))))
            st.pyplot(fig)
            compares = sum(1 for s in steps if s[0] == 'compare')
            swaps = sum(1 for s in steps if s[0] == 'swap')
            st.metric("Vergleiche", compares)
            st.metric("Swaps", swaps)
            st.metric("Schritte", len(steps))

        # Quick
        with col2:
            st.subheader("⚡ Quick Sort")
            steps = quick_sort_animate(arr)
            fig = plot_array(steps[-1][1], "Quick Sort — Fertig", list(range(len(arr))))
            st.pyplot(fig)
            swaps = sum(1 for s in steps if s[0] == 'swap')
            st.metric("Swaps", swaps)
            st.metric("Schritte", len(steps))

        # Merge
        with col3:
            st.subheader("🔀 Merge Sort")
            steps = merge_sort_animate(arr)
            fig = plot_array(steps[-1][1], "Merge Sort — Fertig", list(range(len(arr))))
            st.pyplot(fig)
            merges = sum(1 for s in steps if s[0] == 'merge')
            st.metric("Merges", merges)
            st.metric("Schritte", len(steps))

        st.info("💡 **Bubble Sort** (O(n²)): Einfach, viele Vergleiche. **Quick Sort** (O(n log n)): Schnell, Divide & Conquer. **Merge Sort** (O(n log n)): Stabil, gut für verkettete Listen.")

# ═══════════════════════════════════════════════════════════════
# 2. Suchalgorithmen vergleichen
# ═══════════════════════════════════════════════════════════════

elif mode == "Suchalgorithmen vergleichen":
    st.header("🔍 Suchalgorithmen vergleichen")

    st.markdown("Vergleiche **Lineare Suche** (O(n)) mit **Binärer Suche** (O(log n)).")

    col1, col2 = st.columns(2)
    with col1:
        search_size = st.slider("Array-Größe", 10, 1000, 100, 10)
    with col2:
        target = st.number_input("Zielwert", 0, 999, 42)

    if st.button("🔍 Suchen & Vergleichen", type="primary"):
        # Sortiertes Array
        arr = sorted([random.randint(0, 999) for _ in range(search_size)])

        # ── Lineare Suche ────────────────────────────────────
        linear_steps = 0
        linear_found = -1
        for i, val in enumerate(arr):
            linear_steps += 1
            if val == target:
                linear_found = i
                break

        # ── Binäre Suche ─────────────────────────────────────
        binary_steps = 0
        binary_found = -1
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            binary_steps += 1
            mid = (lo + hi) // 2
            if arr[mid] == target:
                binary_found = mid
                break
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        # ── Ergebnisse ───────────────────────────────────────
        st.divider()
        st.subheader("📊 Ergebnisse")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔍 Lineare Suche")
            st.metric("Schritte", linear_steps)
            st.metric("Gefunden bei Index", linear_found if linear_found >= 0 else "Nicht gefunden")
            st.caption(f"Komplexität: O(n) = O({search_size})")

        with col2:
            st.markdown("### ⚡ Binäre Suche")
            st.metric("Schritte", binary_steps)
            st.metric("Gefunden bei Index", binary_found if binary_found >= 0 else "Nicht gefunden")
            st.caption(f"Komplexität: O(log n) = O({int(np.log2(search_size))})")

        # ── Visualisierung ───────────────────────────────────
        st.subheader("📈 Vergleich")

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

        # Array mit Markierung
        colors = ["#E0E0E0"] * len(arr)
        if linear_found >= 0:
            colors[linear_found] = "#4CAF50"
        # Zeige nur einen Ausschnitt
        window = min(50, len(arr))
        start_idx = max(0, (max(linear_found, 0)) - window // 2)
        end_idx = min(len(arr), start_idx + window)
        ax1.bar(range(start_idx, end_idx), arr[start_idx:end_idx],
                color=colors[start_idx:end_idx])
        ax1.set_title(f"Lineare Suche: {linear_steps} Schritte")
        ax1.set_xlabel("Index")
        ax1.set_ylabel("Wert")

        # Komplexitäts-Vergleich
        sizes = [10, 50, 100, 500, 1000]
        linear_ops = sizes
        binary_ops = [int(np.log2(s)) for s in sizes]
        ax2.plot(sizes, linear_ops, "o-", label="Linear O(n)", color="#FF5722")
        ax2.plot(sizes, binary_ops, "s-", label="Binär O(log n)", color="#4CAF50")
        ax2.set_title("Komplexitäts-Vergleich")
        ax2.set_xlabel("Array-Größe (n)")
        ax2.set_ylabel("Max. Schritte")
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        st.pyplot(fig)

        st.success(f"⚡ Binäre Suche ist **{linear_steps // max(binary_steps, 1)}× schneller** bei n={search_size}!")

# ═══════════════════════════════════════════════════════════════
# 3. Graphen visualisieren
# ═══════════════════════════════════════════════════════════════

elif mode == "Graphen visualisieren":
    st.header("🕸️ Graphen visualisieren")

    graph_algo = st.selectbox(
        "Algorithmus",
        ["BFS (Breitensuche)", "DFS (Tiefensuche)", "Dijkstra (Kürzeste Pfade)", "Alle drei"],
    )

    # Vordefinierte Graphen
    graph_presets = {
        "Einfach (6 Knoten)": {
            "graph": {
                "A": ["B", "C"],
                "B": ["A", "D", "E"],
                "C": ["A", "F"],
                "D": ["B"],
                "E": ["B", "F"],
                "F": ["C", "E"],
            },
            "weighted": {
                "A": {"B": 4, "C": 2},
                "B": {"A": 4, "C": 1, "D": 5},
                "C": {"A": 2, "B": 1, "D": 8, "E": 10},
                "D": {"B": 5, "C": 8, "E": 2},
                "E": {"C": 10, "D": 2},
            },
            "start": "A",
        },
        "Mittel (8 Knoten)": {
            "graph": {
                "A": ["B", "C", "D"],
                "B": ["A", "E", "F"],
                "C": ["A", "G"],
                "D": ["A", "H"],
                "E": ["B"],
                "F": ["B", "G"],
                "G": ["C", "F", "H"],
                "H": ["D", "G"],
            },
            "weighted": {
                "A": {"B": 2, "C": 5, "D": 1},
                "B": {"A": 2, "E": 3, "F": 4},
                "C": {"A": 5, "G": 2},
                "D": {"A": 1, "H": 6},
                "E": {"B": 3},
                "F": {"B": 4, "G": 1},
                "G": {"C": 2, "F": 1, "H": 3},
                "H": {"D": 6, "G": 3},
            },
            "start": "A",
        },
    }

    preset = st.selectbox("Graph auswählen", list(graph_presets.keys()))
    gdata = graph_presets[preset]
    graph = gdata["graph"]
    weighted = gdata["weighted"]
    start_node = st.selectbox("Startknoten", list(graph.keys()), index=list(graph.keys()).index(gdata["start"]))

    if st.button("▶️ Ausführen", type="primary"):
        # ── Graph-Visualisierung ─────────────────────────────

        def draw_graph(graph, title, highlight_order=None, distances=None):
            G = nx.Graph(graph)
            pos = nx.spring_layout(G, seed=42, k=1.5)

            fig, ax = plt.subplots(figsize=(8, 6))
            nx.draw_networkx_edges(G, pos, ax=ax, edge_color="#BDBDBD", width=1.5)

            if highlight_order:
                colors = []
                for node in G.nodes():
                    if node in highlight_order:
                        idx = highlight_order.index(node)
                        colors.append(plt.cm.Blues(0.3 + 0.7 * idx / max(len(highlight_order)-1, 1)))
                    else:
                        colors.append("#E0E0E0")
                nx.draw_networkx_nodes(G, pos, ax=ax, node_color=colors, node_size=600)
                # Nummerierung
                labels = {node: f"{node}\n({highlight_order.index(node)+1})" for node in highlight_order}
            elif distances:
                colors = []
                for node in G.nodes():
                    d = distances.get(node, float("inf"))
                    if d == float("inf"):
                        colors.append("#E0E0E0")
                    else:
                        max_d = max(v for v in distances.values() if v != float("inf"))
                        colors.append(plt.cm.Greens(0.3 + 0.7 * (1 - d / max(max_d, 1))))
                nx.draw_networkx_nodes(G, pos, ax=ax, node_color=colors, node_size=600)
                labels = {node: f"{node}\n({distances.get(node, '∞')})" for node in G.nodes()}
            else:
                nx.draw_networkx_nodes(G, pos, ax=ax, node_color="#2196F3", node_size=600)
                labels = {node: node for node in G.nodes()}

            nx.draw_networkx_labels(G, pos, ax=ax, labels=labels, font_size=10)
            ax.set_title(title)
            ax.axis("off")
            return fig

        if graph_algo == "BFS (Breitensuche)":
            order = bfs(graph, start_node)
            st.subheader(f"🔍 BFS ab '{start_node}'")
            st.write(f"**Reihenfolge**: {' → '.join(order)}")
            fig = draw_graph(graph, f"BFS ab {start_node}", highlight_order=order)
            st.pyplot(fig)
            st.info(f"💡 BFS besucht Knoten ebenenweise. Reihenfolge: {len(order)} Knoten in {len(order)-1} Schritten.")

        elif graph_algo == "DFS (Tiefensuche)":
            order = dfs(graph, start_node)
            st.subheader(f"🔍 DFS ab '{start_node}'")
            st.write(f"**Reihenfolge**: {' → '.join(order)}")
            fig = draw_graph(graph, f"DFS ab {start_node}", highlight_order=order)
            st.pyplot(fig)
            st.info(f"💡 DFS geht zuerst in die Tiefe. Reihenfolge: {len(order)} Knoten.")

        elif graph_algo == "Dijkstra (Kürzeste Pfade)":
            dist = dijkstra(weighted, start_node)
            st.subheader(f"📏 Dijkstra ab '{start_node}'")
            st.write("**Kürzeste Distanzen:**")
            for node, d in sorted(dist.items()):
                st.write(f"- {start_node} → {node}: **{d}**")
            fig = draw_graph(graph, f"Dijkstra ab {start_node}", distances=dist)
            st.pyplot(fig)
            st.info("💡 Dijkstra findet kürzeste Pfade in gewichteten Graphen (nur positive Kantengewichte).")

        elif graph_algo == "Alle drei":
            col1, col2, col3 = st.columns(3)

            with col1:
                st.subheader("🔍 BFS")
                order = bfs(graph, start_node)
                st.write(f"**Reihenfolge**: {' → '.join(order)}")
                fig = draw_graph(graph, "BFS", highlight_order=order)
                st.pyplot(fig)

            with col2:
                st.subheader("🔍 DFS")
                order = dfs(graph, start_node)
                st.write(f"**Reihenfolge**: {' → '.join(order)}")
                fig = draw_graph(graph, "DFS", highlight_order=order)
                st.pyplot(fig)

            with col3:
                st.subheader("📏 Dijkstra")
                dist = dijkstra(weighted, start_node)
                for node, d in sorted(dist.items()):
                    st.write(f"{start_node}→{node}: **{d}**")
                fig = draw_graph(graph, "Dijkstra", distances=dist)
                st.pyplot(fig)

# ═══════════════════════════════════════════════════════════════
# Sidebar: Info
# ═══════════════════════════════════════════════════════════════

st.sidebar.markdown("---")
st.sidebar.subheader("ℹ️ Algorithmen-Übersicht")
st.sidebar.markdown("""
**Sortieren:**
- 🫧 Bubble Sort — O(n²)
- ⚡ Quick Sort — O(n log n)
- 🔀 Merge Sort — O(n log n)

**Suchen:**
- 🔍 Linear — O(n)
- ⚡ Binär — O(log n)

**Graphen:**
- 🔍 BFS — O(V + E)
- 🔍 DFS — O(V + E)
- 📏 Dijkstra — O((V+E) log V)

**DP:**
- Fibonacci — O(n)
- Knapsack — O(n·W)
- LCS — O(n·m)
""")

st.sidebar.markdown("---")
st.sidebar.caption("Algorithmen · Streamlit App")
