import time
import random

from deterministic import deterministic_selection
from random_quicksort import randomized_selection

# Wrapper functions to call the selection algorithms
def test_deterministic(arr, k):
    start_time = time.time()
    result = deterministic_selection(arr, k)
    return time.time() - start_time

def test_randomized(arr, k):
    start_time = time.time()
    result = randomized_selection(arr, k)
    return time.time() - start_time

# Helper function to generate random, sorted, reverse-sorted, and duplicate arrays
def generate_test_cases(n):
    random_array = [random.randint(1, 1000000) for _ in range(n)]
    sorted_array = sorted(random_array)
    reverse_sorted_array = sorted(random_array, reverse=True)
    duplicate_array = [random.choice(random_array) for _ in range(n)]
    
    return random_array, sorted_array, reverse_sorted_array, duplicate_array

# Function to print the results in a formatted way
def run_empirical_tests():
    sizes = [10**3, 10**4, 10**5]  # Small, medium, large input sizes
    headers = ["Input Size", "Input Type", "Deterministic Time (s)", "Randomized Time (s)"]
    
    # Print the header
    print(f"{headers[0]:<12} | {headers[1]:<16} | {headers[2]:<22} | {headers[3]:<22}")
    print("-" * 80)
    
    # Loop through the different sizes and test cases
    for n in sizes:
        random_arr, sorted_arr, reverse_sorted_arr, duplicate_arr = generate_test_cases(n)
        k = n // 2  # Find the median element for testing

        # Test on random array
        deterministic_time = test_deterministic(random_arr[:], k)
        randomized_time = test_randomized(random_arr[:], k)
        print(f"{n:<12} | {'Random':<16} | {deterministic_time:<22.6f} | {randomized_time:<22.6f}")

        # Test on sorted array
        deterministic_time = test_deterministic(sorted_arr[:], k)
        randomized_time = test_randomized(sorted_arr[:], k)
        print(f"{n:<12} | {'Sorted':<16} | {deterministic_time:<22.6f} | {randomized_time:<22.6f}")

        # Test on reverse sorted array
        deterministic_time = test_deterministic(reverse_sorted_arr[:], k)
        randomized_time = test_randomized(reverse_sorted_arr[:], k)
        print(f"{n:<12} | {'Reverse Sorted':<16} | {deterministic_time:<22.6f} | {randomized_time:<22.6f}")

        # Test on duplicate array
        deterministic_time = test_deterministic(duplicate_arr[:], k)
        randomized_time = test_randomized(duplicate_arr[:], k)
        print(f"{n:<12} | {'Duplicates':<16} | {deterministic_time:<22.6f} | {randomized_time:<22.6f}")

# Run the empirical tests
run_empirical_tests()
