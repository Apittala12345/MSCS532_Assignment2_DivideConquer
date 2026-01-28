import time
import random
import csv
import tracemalloc

from sorts import merge_sort, quick_sort

# -----------------------------
# Dataset generators
# -----------------------------
def generate_sorted(n):
    return list(range(n))

def generate_reverse(n):
    return list(range(n, 0, -1))

def generate_random(n):
    return [random.randint(0, n) for _ in range(n)]


# -----------------------------
# Benchmark function
# -----------------------------
def benchmark():
    sizes = [1000, 5000, 10000]
    datasets = {
        "sorted": generate_sorted,
        "reverse": generate_reverse,
        "random": generate_random
    }

    results = []

    print("Starting benchmarks...\n")

    for size in sizes:
        for name, generator in datasets.items():
            data = generator(size)

            # ---- Merge Sort ----
            tracemalloc.start()
            start = time.perf_counter()
            merge_sort(data)
            end = time.perf_counter()
            mem_merge = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()

            results.append([
                "Merge Sort", name, size, end - start, mem_merge
            ])

            # ---- Quick Sort ----
            data_q = data[:]  # copy
            tracemalloc.start()
            start = time.perf_counter()
            quick_sort(data_q)
            end = time.perf_counter()
            mem_quick = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()

            results.append([
                "Quick Sort", name, size, end - start, mem_quick
            ])

            print(f"Completed {name} dataset, size {size}")

    # -----------------------------
    # Save results to CSV
    # -----------------------------
    with open("results/results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Algorithm", "Dataset", "Size", "Time (sec)", "Memory (bytes)"])
        writer.writerows(results)

    print("\nBenchmark complete!")
    print("Results saved to results/results.csv")


# -----------------------------
# Run benchmark
# -----------------------------
if __name__ == "__main__":
    benchmark()
