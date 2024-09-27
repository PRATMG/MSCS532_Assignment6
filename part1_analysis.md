# Report: Assignment 6 - Part 1: Medians and Order Statistics

## 1. Implementation Overview

In this part of the assignment, we implemented two selection algorithms to find the \(k^{th}\) smallest element (order statistics) in an array:

1. **Deterministic Algorithm (Median of Medians):**
   - The deterministic selection algorithm guarantees \(O(n)\) time complexity, even in the worst case. It achieves this by carefully selecting a pivot using the Median of Medians strategy, which ensures that at least 30% of the elements are eliminated in each recursive step.
   
2. **Randomized Algorithm (Quickselect):**
   - The randomized Quickselect algorithm achieves expected \(O(n)\) time complexity by randomly choosing a pivot and partitioning the array. This approach is similar to QuickSort, but the recursion only continues on one side of the array (the relevant partition). The algorithm has a worst-case time complexity of \(O(n^2)\) when the pivot selection consistently results in unbalanced partitions, but this is rare in practice.

## 2. Performance Analysis

### Deterministic Algorithm (Median of Medians)

- **Time Complexity:** \(O(n)\) in the worst case.
  - The Median of Medians algorithm divides the array into groups of 5, finds the median of each group, recursively selects the median of these medians, and partitions the array. The recurrence relation:
  \[
  T(n) = T\left(\frac{n}{5}\right) + T\left(\frac{7n}{10}\right) + O(n)
  \]
  solves to \(O(n)\), ensuring linear performance even in the worst-case scenario.
  
- **Space Complexity:** \(O(\log n)\)
  - The space complexity arises from the recursion stack, which has a depth of \(O(\log n)\), given that each recursive call eliminates a significant portion of the array.

### Randomized Algorithm (Quickselect)

- **Time Complexity:** Expected \(O(n)\), but worst case \(O(n^2)\).
  - The randomized algorithm selects a pivot at random, which on average results in balanced partitions. The expected recurrence:
  \[
  T(n) = T\left(\frac{n}{2}\right) + O(n)
  \]
  solves to \(O(n)\) in the average case. However, if poor pivots are chosen repeatedly, the algorithm may degrade to \(O(n^2)\) time complexity.

- **Space Complexity:** \(O(\log n)\)
  - Similar to the deterministic algorithm, the recursion depth on average is \(O(\log n)\) due to balanced partitions.

## 3. Empirical Results

The empirical analysis was conducted using arrays of different sizes and distributions (random, sorted, reverse-sorted, and duplicates). Here are the results of the comparison between the deterministic and randomized algorithms:

| **Input Size** | **Input Type**    | **Deterministic Time (s)** | **Randomized Time (s)**  |
|----------------|-------------------|----------------------------|--------------------------|
| 1000           | Random            | 0.000850                   | 0.000308                 |
| 1000           | Sorted            | 0.000775                   | 0.000343                 |
| 1000           | Reverse Sorted    | 0.000709                   | 0.000242                 |
| 1000           | Duplicates        | 0.000927                   | 0.000271                 |
| 10000          | Random            | 0.011737                   | 0.001850                 |
| 10000          | Sorted            | 0.008816                   | 0.002427                 |
| 10000          | Reverse Sorted    | 0.008828                   | 0.004347                 |
| 10000          | Duplicates        | 0.009729                   | 0.002051                 |
| 100000         | Random            | 0.108913                   | 0.050256                 |
| 100000         | Sorted            | 0.113051                   | 0.030449                 |
| 100000         | Reverse Sorted    | 0.107411                   | 0.055827                 |
| 100000         | Duplicates        | 0.118142                   | 0.036655                 |

### Observations:

- For small arrays (size = 1000), the randomized algorithm consistently outperformed the deterministic algorithm. The overhead of selecting the Median of Medians leads to a slight slowdown in the deterministic algorithm.
- As the input size increased, the deterministic algorithm's performance remained steady and predictable, while the randomized algorithm's performance varied slightly depending on the pivot choice and input distribution.
- In most cases, the randomized algorithm outperformed the deterministic algorithm, especially for random and sorted inputs. However, for reverse-sorted arrays, the randomized algorithm showed more variability due to the possibility of selecting poor pivots.

## 4. Conclusion

Based on the theoretical and empirical analysis:

- **Deterministic Algorithm (Median of Medians):** 
  - Guarantees worst-case \(O(n)\) performance, making it ideal when reliable performance is required, regardless of the input distribution. However, it carries more overhead than the randomized algorithm due to the extra work of selecting good pivots.
  
- **Randomized Algorithm (Quickselect):** 
  - In practice, Quickselect is faster on average and outperforms the deterministic algorithm in most cases. However, it carries the risk of \(O(n^2)\) performance for adversarial inputs. For most real-world applications, Quickselect provides a faster and simpler solution.

## Time Complexity Analysis Summary

| **Algorithm**               | **Time Complexity (Worst Case)** | **Time Complexity (Average Case)** | **Space Complexity** |
|-----------------------------|-----------------------------------|-------------------------------------|----------------------|
| **Deterministic (Median of Medians)** | \(O(n)\)                          | \(O(n)\)                            | \(O(\log n)\)         |
| **Randomized (Quickselect)**         | \(O(n^2)\)                        | \(O(n)\)                            | \(O(\log n)\)         |

## Code Repository:

The source code for both algorithms and the empirical tests can be found in the following GitHub repository: [GitHub Repository Link]
