"""
Tests für algorithms.py — pytest-basierte Unit-Tests.
Ausführen mit: pytest test_algorithms.py -v
"""

import pytest
from algorithms import (
    bubble_sort, quick_sort, merge_sort,
    binary_search,
    bfs, dfs, dijkstra,
    fibonacci, knapsack, longest_common_subsequence,
)


# ═══════════════════════════════════════════════════════════════
# Sortieralgorithmen
# ═══════════════════════════════════════════════════════════════

class TestSorting:
    def test_bubble_sort_empty(self):
        assert bubble_sort([]) == []

    def test_bubble_sort_single(self):
        assert bubble_sort([5]) == [5]

    def test_bubble_sort_sorted(self):
        assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_bubble_sort_reverse(self):
        assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_bubble_sort_duplicates(self):
        assert bubble_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]

    def test_bubble_sort_does_not_mutate_original(self):
        arr = [3, 1, 2]
        result = bubble_sort(arr)
        assert arr == [3, 1, 2]
        assert result == [1, 2, 3]

    def test_quick_sort_basic(self):
        assert quick_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

    def test_quick_sort_empty(self):
        assert quick_sort([]) == []

    def test_quick_sort_single(self):
        assert quick_sort([42]) == [42]

    def test_quick_sort_duplicates(self):
        assert quick_sort([5, 2, 5, 1, 2]) == [1, 2, 2, 5, 5]

    def test_merge_sort_basic(self):
        assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]

    def test_merge_sort_empty(self):
        assert merge_sort([]) == []

    def test_merge_sort_single(self):
        assert merge_sort([7]) == [7]

    def test_merge_sort_stable(self):
        # Stabilität: gleiche Werte behalten relative Reihenfolge.
        # Da Python Tupel elementweise vergleicht, ist (2, "a") < (2, "b"),
        # daher wird nach dem ersten Element sortiert und "a" kommt vor "b".
        data = [(2, "b"), (1, "a"), (2, "a")]
        result = merge_sort(data)
        assert result == [(1, "a"), (2, "a"), (2, "b")]

    def test_all_sorts_same_result(self):
        import random
        arr = [random.randint(0, 100) for _ in range(50)]
        expected = sorted(arr)
        assert bubble_sort(arr) == expected
        assert quick_sort(arr) == expected
        assert merge_sort(arr) == expected


# ═══════════════════════════════════════════════════════════════
# Suchalgorithmen
# ═══════════════════════════════════════════════════════════════

class TestSearching:
    def test_binary_search_found_first(self):
        assert binary_search([1, 2, 3, 4, 5], 1) == 0

    def test_binary_search_found_last(self):
        assert binary_search([1, 2, 3, 4, 5], 5) == 4

    def test_binary_search_found_middle(self):
        assert binary_search([1, 2, 3, 4, 5], 3) == 2

    def test_binary_search_not_found(self):
        assert binary_search([1, 2, 3, 4, 5], 99) == -1

    def test_binary_search_empty(self):
        assert binary_search([], 1) == -1

    def test_binary_search_single_found(self):
        assert binary_search([42], 42) == 0

    def test_binary_search_single_not_found(self):
        assert binary_search([42], 7) == -1


# ═══════════════════════════════════════════════════════════════
# Graphenalgorithmen
# ═══════════════════════════════════════════════════════════════

class TestGraph:
    @pytest.fixture
    def simple_graph(self):
        return {
            "A": ["B", "C"],
            "B": ["A", "D", "E"],
            "C": ["A", "F"],
            "D": ["B"],
            "E": ["B", "F"],
            "F": ["C", "E"],
        }

    @pytest.fixture
    def weighted_graph(self):
        return {
            "A": {"B": 4, "C": 2},
            "B": {"A": 4, "C": 1, "D": 5},
            "C": {"A": 2, "B": 1, "D": 8, "E": 10},
            "D": {"B": 5, "C": 8, "E": 2},
            "E": {"C": 10, "D": 2},
        }

    def test_bfs_start_node_first(self, simple_graph):
        result = bfs(simple_graph, "A")
        assert result[0] == "A"

    def test_bfs_visits_all_nodes(self, simple_graph):
        result = bfs(simple_graph, "A")
        assert set(result) == {"A", "B", "C", "D", "E", "F"}

    def test_bfs_single_node(self):
        assert bfs({"X": []}, "X") == ["X"]

    def test_dfs_start_node_first(self, simple_graph):
        result = dfs(simple_graph, "A")
        assert result[0] == "A"

    def test_dfs_visits_all_nodes(self, simple_graph):
        result = dfs(simple_graph, "A")
        assert set(result) == {"A", "B", "C", "D", "E", "F"}

    def test_dfs_single_node(self):
        assert dfs({"X": []}, "X") == ["X"]

    def test_dijkstra_basic(self, weighted_graph):
        dist = dijkstra(weighted_graph, "A")
        assert dist["A"] == 0
        assert dist["B"] == 3
        assert dist["C"] == 2
        assert dist["D"] == 8
        assert dist["E"] == 10

    def test_dijkstra_unreachable(self):
        graph = {"A": {}, "B": {}}
        dist = dijkstra(graph, "A")
        assert dist["A"] == 0
        assert dist["B"] == float("inf")


# ═══════════════════════════════════════════════════════════════
# Dynamische Programmierung
# ═══════════════════════════════════════════════════════════════

class TestDP:
    def test_fibonacci_zero(self):
        assert fibonacci(0) == 0

    def test_fibonacci_one(self):
        assert fibonacci(1) == 1

    def test_fibonacci_small(self):
        assert fibonacci(10) == 55

    def test_fibonacci_large(self):
        assert fibonacci(50) == 12586269025

    def test_knapsack_basic(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        assert knapsack(values, weights, 50) == 220

    def test_knapsack_zero_capacity(self):
        assert knapsack([10, 20], [1, 2], 0) == 0

    def test_knapsack_no_items(self):
        assert knapsack([], [], 10) == 0

    def test_knapsack_item_too_heavy(self):
        assert knapsack([100], [50], 10) == 0

    def test_lcs_identical(self):
        assert longest_common_subsequence("ABC", "ABC") == 3

    def test_lcs_no_common(self):
        assert longest_common_subsequence("ABC", "XYZ") == 0

    def test_lcs_basic(self):
        assert longest_common_subsequence("ABCDGH", "AEDFHR") == 3

    def test_lcs_empty(self):
        assert longest_common_subsequence("", "ABC") == 0
        assert longest_common_subsequence("ABC", "") == 0

    def test_lcs_substring(self):
        assert longest_common_subsequence("ABCDEF", "BCD") == 3

    def test_lcs_repeated(self):
        assert longest_common_subsequence("AAAA", "AA") == 2


# ═══════════════════════════════════════════════════════════════
# Edge Cases & Robustheit
# ═══════════════════════════════════════════════════════════════

class TestEdgeCases:
    def test_binary_search_duplicates(self):
        # Bei Duplikaten: irgendein gültiger Index
        idx = binary_search([1, 2, 2, 2, 3], 2)
        assert idx in (1, 2, 3)

    def test_bfs_disconnected_graph(self):
        graph = {"A": ["B"], "B": ["A"], "C": ["D"], "D": ["C"]}
        result = bfs(graph, "A")
        assert set(result) == {"A", "B"}

    def test_dfs_disconnected_graph(self):
        graph = {"A": ["B"], "B": ["A"], "C": ["D"], "D": ["C"]}
        result = dfs(graph, "A")
        assert set(result) == {"A", "B"}

    def test_fibonacci_negative(self):
        assert fibonacci(-1) == -1

    def test_knapsack_exact_fit(self):
        assert knapsack([10, 20], [5, 10], 15) == 30

    def test_large_input_performance(self):
        # Sicherstellen, dass große Eingaben nicht crashen
        arr = list(range(1000, 0, -1))
        result = merge_sort(arr)
        assert result == sorted(arr)
        assert binary_search(result, 500) >= 0
