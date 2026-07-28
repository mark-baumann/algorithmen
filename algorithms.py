"""
Klassische Algorithmen in Python
================================
Sortieren, Suchen, Graphen, Dynamische Programmierung —
implementiert zum Verstehen, nicht zum Produktiv-Einsatz.
"""

from typing import List, TypeVar, Optional
import heapq

T = TypeVar("T")


# ═══════════════════════════════════════════════════════════════
# Sortieralgorithmen
# ═══════════════════════════════════════════════════════════════

def bubble_sort(arr: List[T]) -> List[T]:
    """O(n²) — einfach, aber langsam. Gut zum Lernen."""
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


def quick_sort(arr: List[T]) -> List[T]:
    """O(n log n) average — Divide & Conquer."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr: List[T]) -> List[T]:
    """O(n log n) — stabil, gut für Linked Lists."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: List[T], right: List[T]) -> List[T]:
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


# ═══════════════════════════════════════════════════════════════
# Suchalgorithmen
# ═══════════════════════════════════════════════════════════════

def binary_search(arr: List[T], target: T) -> int:
    """O(log n) — Voraussetzung: sortiertes Array."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# ═══════════════════════════════════════════════════════════════
# Graphenalgorithmen
# ═══════════════════════════════════════════════════════════════

def bfs(graph: dict, start: T) -> List[T]:
    """Breitensuche — kürzester Pfad in ungewichtetem Graphen."""
    visited = {start}
    queue = [start]
    order = []
    while queue:
        node = queue.pop(0)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def dfs(graph: dict, start: T, visited: set = None) -> List[T]:
    """Tiefensuche — rekursiv."""
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))
    return order


def dijkstra(graph: dict, start: T) -> dict:
    """Dijkstra — kürzeste Pfade in gewichtetem Graphen."""
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node].items():
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist


# ═══════════════════════════════════════════════════════════════
# Dynamische Programmierung
# ═══════════════════════════════════════════════════════════════

def fibonacci(n: int) -> int:
    """O(n) mit DP — statt O(2^n) rekursiv."""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def knapsack(values: List[int], weights: List[int], capacity: int) -> int:
    """0/1 Rucksackproblem — DP-Lösung O(n*W)."""
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


def longest_common_subsequence(a: str, b: str) -> int:
    """LCS — DP-Lösung O(n*m)."""
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


# ═══════════════════════════════════════════════════════════════
# Tests
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Sortieren
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Bubble Sort:  {bubble_sort(arr)}")
    print(f"Quick Sort:   {quick_sort(arr)}")
    print(f"Merge Sort:   {merge_sort(arr)}")

    # Suchen
    sorted_arr = [11, 12, 22, 25, 34, 64, 90]
    print(f"\nBinary Search 22: index {binary_search(sorted_arr, 22)}")
    print(f"Binary Search 99: index {binary_search(sorted_arr, 99)}")

    # Graphen
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    print(f"\nBFS from A: {bfs(graph, 'A')}")
    print(f"DFS from A: {dfs(graph, 'A')}")

    weighted = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2},
        "E": {"C": 10, "D": 2},
    }
    print(f"Dijkstra from A: {dijkstra(weighted, 'A')}")

    # DP
    print(f"\nFibonacci(10): {fibonacci(10)}")
    print(f"Fibonacci(50): {fibonacci(50)}")

    values = [60, 100, 120]
    weights = [10, 20, 30]
    print(f"Knapsack (W=50): {knapsack(values, weights, 50)}")

    print(f"LCS('ABCDGH', 'AEDFHR'): {longest_common_subsequence('ABCDGH', 'AEDFHR')}")
