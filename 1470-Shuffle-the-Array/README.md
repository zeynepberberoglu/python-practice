# 1470. Shuffle the Array

## 🔗 Problem Link
[LeetCode Problem 1470 - Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/)

## ✍️ Problem Description
Given an array `nums` composed of $2n$ elements structured as $\text{[x}_1, \text{x}_2, \dots, \text{x}_n, \text{y}_1, \text{y}_2, \dots, \text{y}_n]$. The task is to return a new array that is "shuffled" into the form $\text{[x}_1, \text{y}_1, \text{x}_2, \text{y}_2, \dots, \text{x}_n, \text{y}_n]$. The parameter $n$ indicates the length of the first and second sub-arrays.

***

## 💡 Solution Approach
This problem can be solved efficiently by iterating through the first half of the array and the second half **simultaneously** and appending the elements to the result array in the required interleaved order.

The array $\text{nums}$ is logically divided into two parts:
1.  **First Half (X):** Indices $0$ to $n-1$.
2.  **Second Half (Y):** Indices $n$ to $2n-1$.

We use a single loop to iterate $n$ times. In each iteration, we append one element from the X-half and one element from the Y-half:
1.  A pointer (e.g., $\text{a}$) tracks the index of the element $\text{x}_i$ from the beginning of the array.
2.  The main loop variable (e.g., $\text{i}$) tracks the index of the element $\text{y}_i$ from the middle of the array (starting at index $n$).
3.  Inside the loop, we append $\text{nums}[\text{a}]$ (the $\text{x}$ element) followed immediately by $\text{nums}[\text{i}]$ (the $\text{y}$ element) to the result array.

4.  * **Time Complexity:** $O(n)$
    * We iterate exactly $n$ times (where $n$ is half the total length of the array). Since we perform a constant number of operations (two appends and one increment) inside the loop, the time complexity grows linearly with the input size $n$.

* **Space Complexity:** $O(n)$
    * We create a new result array ($\text{out}$) of size $2n$ to store the shuffled elements. The space used is directly proportional to the size of the input, making the complexity linear.
