import time
import random

SIZE = 500

def populate_array_for_loop():
    start = time.time()
    arr = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            arr[i][j] = random.randint(0, 10000)  # Fill with random numbers
    elapsed = time.time() - start
    return arr, elapsed

if __name__ == "__main__":
    _, for_time = populate_array_for_loop()
    print(f"For loop (size {SIZE}x{SIZE}): {for_time:.4f} seconds")
