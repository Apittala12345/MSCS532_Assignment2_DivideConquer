from sorts import merge_sort, quick_sort
import random

def run_tests():
    for test_num in range(1, 11):
        arr = [random.randint(-1000, 1000) for _ in range(100)]
        expected = sorted(arr)

        # Merge Sort test (returns new list)
        if merge_sort(arr) != expected:
            print("❌ Merge Sort failed on test", test_num)
            return

        # Quick Sort test (in-place)
        arr2 = arr[:]
        quick_sort(arr2)
        if arr2 != expected:
            print("❌ Quick Sort failed on test", test_num)
            return

    print("✅ All tests passed for Merge Sort and Quick Sort!")

if __name__ == "__main__":
    run_tests()
