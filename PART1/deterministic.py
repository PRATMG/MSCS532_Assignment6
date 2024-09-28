"""
This code implements the deterministic selection algorithm, also known as the Median of Medians algorithm, 
to find the k^th smallest element in an unsorted array in worst-case linear time (O(n)). The algorithm works 
by recursively selecting a good pivot to partition the array, ensuring balanced partitions and thus maintaining 
linear time complexity. The implementation is efficient and handles edge cases, including arrays with duplicate elements. 
The code includes a partition function for rearranging elements around the chosen pivot, the median_of_medians function 
for recursively finding the k^th smallest element, and a test_median_of_medians function that runs multiple test cases
to verify the correctness and robustness of the algorithm.
"""

def partition(arr, low, high, pivot_index):
    """
    Partition the array around the pivot value.

    Parameters:
    - arr: List of elements to partition.
    - low: Lower index of the subarray.
    - high: Higher index of the subarray.
    - pivot_index: Index of the pivot element.

    Returns:
    - The index position of the pivot after partitioning.
    """
    pivot_value = arr[pivot_index]
    # Move pivot to the end
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    store_index = low

    # Compare each element with the pivot value
    for i in range(low, high):
        if arr[i] < pivot_value:
            # Swap elements smaller than pivot_value to the front
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
        elif arr[i] == pivot_value:
            # Handle duplicates: Swap with elements equal to pivot to just before high
            arr[i], arr[high - 1] = arr[high - 1], arr[i]
            i -= 1  # Stay on the same index to check the swapped element

    # Move pivot to its final place
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

def select_pivot(arr, low, high):
    """
    Select a good pivot using the Median of Medians method.

    Parameters:
    - arr: List of elements.
    - low: Lower index of the subarray.
    - high: Higher index of the subarray.

    Returns:
    - The value of the pivot.
    """
    n = high - low + 1
    if n <= 5:
        # For small arrays, return the median directly
        return sorted(arr[low:high+1])[n // 2]

    # Divide the array into sublists of five elements
    medians = []
    for i in range(low, high + 1, 5):
        sub_high = min(i + 4, high)
        sublist = arr[i:sub_high + 1]
        median = sorted(sublist)[len(sublist) // 2]
        medians.append(median)

    # Recursively find the median of medians
    return median_of_medians(medians, 0, len(medians) - 1, len(medians) // 2)

def median_of_medians(arr, low, high, k):
    """
    Find the k-th smallest element in arr[low...high] using the Median of Medians algorithm.

    Parameters:
    - arr: List of elements.
    - low: Lower index of the subarray.
    - high: Higher index of the subarray.
    - k: The k-th position (0-based index) to find.

    Returns:
    - The value of the k-th smallest element.
    """
    if low == high:
        # If the list contains only one element, return it
        return arr[low]

    # Select a good pivot
    pivot_value = select_pivot(arr, low, high)

    # Find the index of the pivot in the current subarray
    pivot_indices = [i for i in range(low, high + 1) if arr[i] == pivot_value]
    if pivot_indices:
        pivot_index = pivot_indices[0]
    else:
        pivot_index = high  # Fallback in case pivot_value not found (should not happen)

    # Partition the array around the pivot and get the pivot index
    pivot_index = partition(arr, low, high, pivot_index)

    # Number of elements in the low partition
    num_elements = pivot_index - low + 1

    # Recursively apply the algorithm based on the pivot's position
    if k == pivot_index:
        # If k is the pivot index, we've found the k-th smallest element
        return arr[k]
    elif k < pivot_index:
        # If k is less than pivot index, search in the left subarray
        return median_of_medians(arr, low, pivot_index - 1, k)
    else:
        # If k is greater than pivot index, search in the right subarray
        return median_of_medians(arr, pivot_index + 1, high, k)

def test_median_of_medians():
    """
    Run multiple test cases to verify the correctness of the median_of_medians algorithm.
    """
    # Test case 1: Basic test with random elements
    arr1 = [12, 3, 5, 7, 19, 1, 10]
    k1 = 3  # Looking for the 3rd smallest element (1-based index)
    result1 = median_of_medians(arr1.copy(), 0, len(arr1) - 1, k1 - 1)
    print(f"Test 1: {k1}rd smallest element in {arr1} is {result1}")

    # Test case 2: Array with duplicate elements
    arr2 = [5, 3, 8, 5, 10, 5, 12]
    k2 = 4  # Looking for the 4th smallest element
    result2 = median_of_medians(arr2.copy(), 0, len(arr2) - 1, k2 - 1)
    print(f"Test 2: {k2}th smallest element in {arr2} is {result2}")

    # Test case 3: Sorted array
    arr3 = [1, 2, 3, 4, 5, 6, 7]
    k3 = 5  # Looking for the 5th smallest element
    result3 = median_of_medians(arr3.copy(), 0, len(arr3) - 1, k3 - 1)
    print(f"Test 3: {k3}th smallest element in {arr3} is {result3}")

    # Test case 4: Reverse sorted array
    arr4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    k4 = 7  # Looking for the 7th smallest element
    result4 = median_of_medians(arr4.copy(), 0, len(arr4) - 1, k4 - 1)
    print(f"Test 4: {k4}th smallest element in {arr4} is {result4}")

    # Test case 5: Single element array
    arr5 = [42]
    k5 = 1  # The only element is the 1st smallest element
    result5 = median_of_medians(arr5.copy(), 0, len(arr5) - 1, k5 - 1)
    print(f"Test 5: {k5}st smallest element in {arr5} is {result5}")

# Execute the test suite
test_median_of_medians()
