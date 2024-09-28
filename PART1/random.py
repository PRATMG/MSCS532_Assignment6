"""
This code implements the Randomized Quickselect algorithm to efficiently find the k^th smallest element in an unsorted array. 
The algorithm achieves an expected linear time complexity by randomly selecting a pivot for partitioning, which helps in evenly 
dividing the array on average. The implementation handles edge cases, such as arrays with duplicate elements, ensuring accurate 
results regardless of the input. The provided test cases demonstrate the algorithm's correctness across various scenarios, 
including arrays with duplicates, sorted arrays, reverse sorted arrays, and single-element arrays.
"""

import random

def partition_random(arr, low, high):
    """
    Partition the array around a randomly selected pivot.

    Parameters:
    - arr: The list of elements to partition.
    - low: The starting index of the subarray.
    - high: The ending index of the subarray.

    Returns:
    - The index position of the pivot after partitioning.
    """
    # Randomly select a pivot index between low and high
    pivot_index = random.randint(low, high)
    # Swap the pivot element with the last element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot_value = arr[high]  # Pivot value is now at the end
    store_index = low

    # Compare each element with the pivot value
    for i in range(low, high):
        if arr[i] < pivot_value:
            # Swap elements smaller than pivot_value to the front
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    # Swap the pivot value to its correct position
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

def quickselect(arr, low, high, k):
    """
    Find the k-th smallest element in the array using Quickselect algorithm.

    Parameters:
    - arr: The list of elements.
    - low: The starting index of the subarray.
    - high: The ending index of the subarray.
    - k: The index (0-based) of the k-th smallest element to find.

    Returns:
    - The value of the k-th smallest element.
    """
    if low == high:
        # If the list contains only one element
        return arr[low]

    # Partition the array and get the pivot index
    pivot_index = partition_random(arr, low, high)

    if k == pivot_index:
        # The pivot value is the k-th smallest element
        return arr[k]
    elif k < pivot_index:
        # Recurse on the left subarray
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        # Recurse on the right subarray
        return quickselect(arr, pivot_index + 1, high, k)

def test_quickselect():
    """
    Run multiple test cases to verify the correctness of the Quickselect algorithm.
    """
    # Test case 1: Basic test with random elements
    arr1 = [12, 3, 5, 7, 19, 1, 10]
    k1 = 3  # Looking for the 3rd smallest element (1-based index)
    result1 = quickselect(arr1.copy(), 0, len(arr1) - 1, k1 - 1)
    print(f"Test 1: {k1}rd smallest element in {arr1} is {result1}")

    # Test case 2: Array with duplicate elements
    arr2 = [5, 3, 8, 5, 10, 5, 12]
    k2 = 4  # Looking for the 4th smallest element
    result2 = quickselect(arr2.copy(), 0, len(arr2) - 1, k2 - 1)
    print(f"Test 2: {k2}th smallest element in {arr2} is {result2}")

    # Test case 3: Sorted array
    arr3 = [1, 2, 3, 4, 5, 6, 7]
    k3 = 5  # Looking for the 5th smallest element
    result3 = quickselect(arr3.copy(), 0, len(arr3) - 1, k3 - 1)
    print(f"Test 3: {k3}th smallest element in {arr3} is {result3}")

    # Test case 4: Reverse sorted array
    arr4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    k4 = 7  # Looking for the 7th smallest element
    result4 = quickselect(arr4.copy(), 0, len(arr4) - 1, k4 - 1)
    print(f"Test 4: {k4}th smallest element in {arr4} is {result4}")

    # Test case 5: Single element array
    arr5 = [42]
    k5 = 1  # The only element is the 1st smallest element
    result5 = quickselect(arr5.copy(), 0, len(arr5) - 1, k5 - 1)
    print(f"Test 5: {k5}st smallest element in {arr5} is {result5}")

# Execute the test suite
test_quickselect()
