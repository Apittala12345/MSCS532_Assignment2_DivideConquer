from __future__ import annotations
from typing import List
import random

# ==========================================================
# MERGE SORT (Divide-and-Conquer)
# - Returns a NEW sorted list (does NOT modify original list)
# ==========================================================

def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort algorithm.
    Time complexity: Θ(n log n) for best/avg/worst
    Space complexity: O(n) extra
    """
    n = len(arr)
    if n <= 1:
        return arr[:]  # copy

    mid = n // 2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])

    return _merge(left_sorted, right_sorted)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted lists into one sorted list."""
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# ==========================================================
# QUICK SORT (Divide-and-Conquer)
# - Sorts IN PLACE (modifies original list)
# - Uses randomized pivot to reduce worst-case chance
# ==========================================================

def quick_sort(arr: List[int]) -> None:
    """
    Quick Sort algorithm (in-place).
    Average time: Θ(n log n)
    Worst time: O(n^2) (rare with random pivot)
    """
    if len(arr) <= 1:
        return
    _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr: List[int], low: int, high: int) -> None:
    if low >= high:
        return

    pivot_index = _partition_random(arr, low, high)
    _quick_sort(arr, low, pivot_index - 1)
    _quick_sort(arr, pivot_index + 1, high)


def _partition_random(arr: List[int], low: int, high: int) -> int:
    pivot_i = random.randint(low, high)
    arr[pivot_i], arr[high] = arr[high], arr[pivot_i]
    return _partition_lomuto(arr, low, high)


def _partition_lomuto(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i
