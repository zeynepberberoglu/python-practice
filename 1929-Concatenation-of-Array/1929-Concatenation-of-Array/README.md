# 1929. Concatenation of Array

## 🔗 Problem Link
[LeetCode Problem 1929 - Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/)

## ✍️ Problem Description
Given an integer array `nums` of length $n$, the goal is to create a new array `ans` of length $2n$. This new array `ans` must be the **concatenation** of two copies of the original `nums` array. Specifically, for $0 \le i < n$:
* $ans[i] == nums[i]$
* $ans[i + n] == nums[i]$

***

## 💡 Solution Approach
This solution follows the problem definition directly by **iterating** through the input array $\text{nums}$ and manually building the result array $\text{ans}$ to be $2n$ in length.

1.  **Initialization:** An empty list, $\text{ans}$, is initialized to store the final result. The length of the input array, $n$, is calculated.
2.  **First Concatenation:** A standard **for loop** is used to iterate from $i=0$ to $n-1$. In this loop, each element $\text{nums}[i]$ is appended to $\text{ans}$, forming the first copy of the array.
3.  **Second Concatenation:** A **while loop** is then used to perform the second iteration. It also appends each element from $\text{nums}$ to $\text{ans}$, completing the concatenation and resulting in an array of length $2n$.

While a more idiomatic Python solution would use the list concatenation operator (`return nums + nums`), this approach explicitly demonstrates the construction of the array using fundamental iterative loops.

## ⏱️ Complexity Analysis

* **Time Complexity:** $O(n)$
    * The solution involves iterating through the input array $\text{nums}$ exactly twice (once in the `for` loop and once in the `while` loop), where $n$ is the length of $\text{nums}$. The time taken grows linearly with the input size.

* **Space Complexity:** $O(n)$
    * An auxiliary array $\text{ans}$ of size $2n$ is created to store the result. Since $2n$ is proportional to $n$, the space complexity is linear with respect to the input size.
