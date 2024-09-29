# Assignment 6: Medians, Order Statistics & Elementary Data Structures

## Overview

This assignment covers the implementation and analysis of two parts of Assignment 6:

1. **Part 1: Selection Algorithms (Medians and Order Statistics)**
   - Implementation of deterministic (Median of Medians) and randomized (Quickselect) algorithms for selecting the \(k^{th}\) smallest element.
   - Detailed time complexity and space complexity analysis of both algorithms.
   - Empirical analysis comparing performance on different input sizes and distributions (random, sorted, reverse-sorted).

2. **Part 2: Elementary Data Structures**
   - Implementation of basic data structures: arrays, matrices, stacks, queues, and linked lists (with an optional binary tree implementation).
   - Time complexity analysis for basic operations of each data structure.
   - Practical applications and trade-offs between data structures in real-world scenarios.

---

## How to Run the Code

### Requirements:
- Python 3.x

### Running the Code:
1. Download the source code from the provided `.py` file or copy the provided code.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `.py` file is saved.
4. Run the Python script by typing the following command:
   for windows:
   ``` bash
   python filename.py
   ```
   for MacOS (or Linux):
   ``` bash
   python3 filename.py
   ```
   Replace `<filename>` with the actual name of the Python file.

   ---

## Design Choices and Implementation Details

### Part 1: Selection Algorithms
- **Deterministic Algorithm (Median of Medians)**: Guarantees worst-case \(O(n)\) time complexity by recursively selecting a good pivot.
- **Randomized Algorithm (Quickselect)**: Achieves expected \(O(n)\) time, but can degrade to \(O(n^2)\) in the worst case.

### Part 2: Data Structures
- **Arrays and Matrices**: Implemented with operations for insertion, deletion, and access.
- **Stacks and Queues**: Implemented using arrays, supporting push, pop, enqueue, and dequeue operations.
- **Linked Lists**: Singly linked list with operations for insertion, deletion, and traversal.
- **Binary Tree (Optional)**: A basic binary tree with insertion and traversal operations.

---

## Part 1: Detailed Analysis

### Time Complexity

#### Deterministic Algorithm (Median of Medians)

- **Worst-case time complexity**: \(O(n)\)
- **Why \(O(n)\)?** The algorithm divides the array into groups of 5, recursively finds the median, and partitions the array, reducing the problem size at each step.

#### Randomized Algorithm (Quickselect)

- **Expected time complexity**: \(O(n)\)
- **Worst-case time complexity**: \(O(n^2)\)
- **Why \(O(n)\)?** On average, the pivot chosen randomly splits the array evenly, resulting in expected linear performance.

### Space Complexity

- Both algorithms have **space complexity** of \(O(\log n)\) due to recursion depth.

### Empirical Analysis

- The **deterministic algorithm** consistently performs in \(O(n)\) regardless of input distribution.
- The **randomized algorithm** is faster on random inputs but may degrade on sorted or reverse-sorted arrays.

---

## Part 2: Elementary Data Structures Performance

### Arrays
- **Access**: \(O(1)\)
- **Insertion (End)**: \(O(1)\), **Insertion (Middle)**: \(O(n)\)
- **Deletion (End)**: \(O(1)\), **Deletion (Middle)**: \(O(n)\)

### Stacks (Array-based)
- **Push/Pop**: \(O(1)\)
- **Space-efficient**, but fixed-size arrays require resizing.

### Queues (Array-based)
- **Enqueue**: \(O(1)\)
- **Dequeue**: \(O(n)\) (due to shifting elements)

### Linked Lists
- **Insertion/Deletion at Head**: \(O(1)\)
- **Access/Traversal**: \(O(n)\)

### Binary Trees
- **Balanced Trees**: \(O(log n)\) for insertion, deletion, and search.

---

## Practical Applications

### Arrays
- Best for scenarios requiring **random access** like image processing or database indexing.

### Linked Lists
- Efficient for **dynamic data** where insertions and deletions occur frequently, such as in implementing stacks, queues, or dynamic memory allocation.

### Stacks
- Ideal for **function call management** (e.g., recursion), **expression evaluation**, and **undo operations**.

### Queues
- Used in **task scheduling**, **BFS in graph traversal**, and **customer service systems**.

### Binary Trees
- Best for hierarchical data and **efficient searching** in applications like databases, file systems, and priority queues.

