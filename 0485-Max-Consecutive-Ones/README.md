# 485. Max Consecutive Ones

## 🔗 Problem Link
[LeetCode Problem 485 - Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/)

## ✍️ Problem Description
Given a binary array $\text{nums}$ (containing only 0s and 1s), the objective is to find and return the largest number of consecutive 1s that exist in the array.

***

## 💡 Solution Approach
This solution uses an **iterative approach** with nested loops to explicitly track the end of a consecutive sequence. The core idea is to find the length of every sequence of consecutive ones and store these lengths to determine the maximum.

1.  **Initialization:** Two counters are used: $\text{a}$ (the main array index) and $\text{con}$ (the current consecutive count). A list, $\text{general}$, is initialized to store the length of every discovered sequence of ones.
2.  **Outer Loop (Progress):** The outer `while` loop ensures we traverse the entire array.
3.  **Inner Loop (Counting Sequence):** The inner `while` loop aggressively counts the consecutive 1s until it encounters a 0 or reaches the end of the array.
    * If $\text{nums}[a]$ is **1**, $\text{con}$ is incremented, and the index $\text{a}$ moves forward.
    * If $\text{nums}[a]$ is **0**, the sequence is broken. The index $\text{a}$ moves past the 0, and the inner loop immediately breaks.
4.  **Tracking:** After the inner loop completes, the current count $\text{con}$ is appended to the $\text{general}$ list. $\text{con}$ is then reset to 0 to prepare for the next sequence.
5.  **Result:** Finally, the maximum value from the $\text{general}$ list is returned as the answer.

### Alternative (Single Pass Optimization)

A more common solution is the **Single Pass** approach, which uses two variables ($\text{current\_count}$ and $\text{max\_count}$) in a single loop, avoiding the need for the $\text{general}$ list. When a **0** is encountered, the $\text{current\_count}$ is reset to 0. In every iteration, $\text{max\_count}$ is updated using $\max(\text{max\_count}, \text{current\_count})$. Both approaches achieve the same efficiency.

## ⏱️ Complexity Analysis

* **Time Complexity:** $O(N)$
    * Both the outer and inner loops contribute to traversing the array $\text{nums}$. Crucially, the index $\text{a}$ is incremented in every step (either in the `if` or `elif` block). Therefore, the total number of operations performed by the nested structure is directly proportional to the length of the array $N$, ensuring a linear time complexity.

* **Space Complexity:** $O(S)$
    * We use an auxiliary list $\text{general}$ to store the length of every consecutive sequence of ones. In the worst-case scenario (e.g., `[1,0,1,0,1,0,...]`), the list $\text{general}$ could have a size proportional to half the size of the input array, $S \approx N/2$. Therefore, the space complexity is linear, $O(N)$.
