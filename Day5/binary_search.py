# Overview
# Iterative binary search halves the search space each step (O(log n) vs O(n) linear). find_closest() 
# uses the same binary search then compares neighbours at the miss point. Benchmarks both 
# approaches with time.perf_counter. This is the most commonly asked algorithm in technical 
# interviews.
# Problem
# Binary search a sorted price list. Find exact match index or closest price. Compare speed vs linear search.
# Constraints
# • List must be sorted first
# • Return index (0-based)
# • O(log n) -- not O(n)
# Bonus: Implement recursive binary search and compare with iterative.

import time

def binary_search(prices, target):
    left = 0
    right = len(prices) - 1

    while left <= right:
        mid = (left + right) // 2

        if prices[mid] == target:
            return mid

        elif prices[mid] < target:
            left = mid + 1

        else:
            right = mid - 1        

    return -1

def linear_search(prices, target):
    for i in range(len(prices)):
        if prices[i] == target:
            return i
    return -1


def find_closest(prices, target):
    left = 0
    right = len(prices) - 1

    while left <= right:
        mid = (left + right) // 2

        if prices[mid] == target:
            return mid

        elif prices[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    # Target smaller than first element
    if left == 0:
        return 0

    # Target larger than last element
    if left == len(prices):
        return len(prices) - 1

    # Compare neighbours
    before = prices[left - 1]
    after = prices[left]

    if abs(before - target) <= abs(after - target):
        return left - 1
    else:
        return left


# Bonus: Recursive Binary Search
def recursive_binary_search(prices, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if prices[mid] == target:
        return mid

    elif prices[mid] < target:
        return recursive_binary_search(
            prices, target, mid + 1, right
        )

    else:
        return recursive_binary_search(
            prices, target, left, mid - 1
        )


prices = [99, 149, 199, 249, 299, 349, 399, 449, 499]

target = int(input("Enter product price to search: "))

# Binary Search Benchmark
start = time.perf_counter()
binary_index = binary_search(prices, target)
binary_time = time.perf_counter() - start

# Linear Search Benchmark
start = time.perf_counter()
linear_index = linear_search(prices, target)
linear_time = time.perf_counter() - start

# Recursive Search Benchmark
start = time.perf_counter()
recursive_index = recursive_binary_search(
    prices, target, 0, len(prices) - 1
)
recursive_time = time.perf_counter() - start


if binary_index != -1:
    print(f"\nExact match found at index {binary_index}")
else:
    closest_index = find_closest(prices, target)
    print("\nExact price not found")
    print(
        f"Closest price: {prices[closest_index]} "
        f"(index {closest_index})"
    )

print("\n--- Performance Comparison ---")
print(f"Linear Search    : {linear_time:.10f} seconds")
print(f"Binary Search    : {binary_time:.10f} seconds")
print(f"Recursive Search : {recursive_time:.10f} seconds")

