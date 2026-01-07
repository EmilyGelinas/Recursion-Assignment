import time
import sys
import random

sys.setrecursionlimit(3000)
SIZE = 50

# Recursive function to fill the array
# WARNING: This will likely hit recursion limit for SIZE=500 in Python
# For demonstration, use a smaller size or iterative approach for large arrays

def populate_recursive(arr, i=0, j=0):
    if i >= SIZE:
        return
    if j >= SIZE:
        populate_recursive(arr, i + 1, 0)
        return
    arr[i][j] = random.randint(0, 10000)
    populate_recursive(arr, i, j + 1)

def timed_populate_recursive():
    arr = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    start = time.time()
    populate_recursive(arr)
    elapsed = time.time() - start
    return arr, elapsed

if __name__ == "__main__":
    try:
        _, rec_time = timed_populate_recursive()
        print(f"Recursion (size {SIZE}x{SIZE}): {rec_time:.4f} seconds")
    except RecursionError:
        print("RecursionError: Maximum recursion depth exceeded. Try a smaller SIZE.")
