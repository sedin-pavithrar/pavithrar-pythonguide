# Sorting Algorithms -- Leaderboard Sorter
# Bubble Sort Merge Sort Quick Sort time complexity
# Real-world App
# BGMI / MPL / Kahoot
# Overview
# Implements Bubble Sort (O(n^2) swap-based), Merge Sort (O(n log n) divide-and-conquer), and 
# Quick Sort (O(n log n) pivot-partition) from scratch on a list of player dicts. compare_sorts() times all 
# three on the same dataset. Understanding these algorithms is essential for every backend engineer 
# and ML practitioner.
# Problem
# Implement Bubble, Merge, and Quick Sort from scratch. Sort a player leaderboard by score. 
# Compare execution times.
# Time Complexity
# Algorithm Best Average Worst
# Bubble Sort O(n) O(n^2) O(n^2)
# Merge Sort O(n log n) O(n log n) O(n log n)
# Quick Sort O(n log n) O(n log n) O(n^2)
# Constraints
# • No sorted() or .sort()
# • Sort by score descending
# • Bonus: Add Python Timsort and show it win


import random
import time


players = [
    {"name": f"Player{i}", "score": random.randint(100, 10000)}
    for i in range(1, 21)
]


# Bubble Sort
# Time: O(n²)

def bubble_sort(data):
    arr = data.copy()
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if arr[j]["score"] < arr[j + 1]["score"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


# Merge Sort
# Time: O(n log n)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i]["score"] >= right[j]["score"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Quick Sort
# Average Time: O(n log n)
# Worst Time: O(n²)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    higher = []
    lower = []

    for player in arr[:-1]:
        if player["score"] >= pivot["score"]:
            higher.append(player)
        else:
            lower.append(player)

    return quick_sort(higher) + [pivot] + quick_sort(lower)


# Python Timsort


def timsort(data):
    return sorted(data, key=lambda p: p["score"], reverse=True)


#  Execution Times


def compare_sorts(data):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Timsort", timsort)
    ]

    for name, func in algorithms:

        start = time.perf_counter()
        result = func(data)
        end = time.perf_counter()

        print(f"\n{name}")
        print("-" * 40)

        for player in result[:5]:
            print(player)

        print(f"Execution Time: {(end - start):.8f} seconds")

def main():
    print("Original Leaderboard")
    print("-" * 40)

    for player in players:
        print(player)

    compare_sorts(players)


if __name__ == "__main__":
    main()

   