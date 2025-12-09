# 645. Set Mismatch

## 🔗 Problem Link
[LeetCode Problem 645 - Set Mismatch](https://leetcode.com/problems/set-mismatch/)

## ✍️ Problem Description
Given an array $\text{nums}$ which initially contained all integers from 1 to $n$, but has suffered an error resulting in one number being duplicated and one number being lost. The goal is to identify the number that is repeated and the number that is missing, returning them as an array $[\text{duplicated\_num}, \text{missing\_num}]$.

***

## 💡 Solution Approach (Mathematical Summation)
This problem is solved efficiently by utilizing the mathematical properties of the set and the array, specifically the expected sum of the numbers from 1 to $n$.

1.  **Expected Sum:** The total sum of a perfect set (1 to $n$) is calculated using the arithmetic series formula: $S_{\text{expected}} = \frac{n(n+1)}{2}$.
2.  **Actual Sums:** Two actual sums are computed:
    * $S_{\text{actual}}$: The sum of the given input array $\text{nums}$ (includes the duplicate).
    * $S_{\text{set}}$: The sum of the elements after converting $\text{nums}$ to a `set` (this sum *excludes* the duplicate, but *includes* the missing number's space).
3.  **Finding the Duplicate:** The difference between $S_{\text{actual}}$ and $S_{\text{set}}$ directly yields the value of the duplicated number, as it is the only element included in $S_{\text{actual}}$ but removed from $S_{\text{set}}$.
    * $\text{Duplicated} = S_{\text{actual}} - S_{\text{set}}$
4.  **Finding the Missing:** The difference between $S_{\text{expected}}$ and $S_{\text{set}}$ gives the value of the missing number, as $S_{\text{set}}$ is exactly $S_{\text{expected}}$ minus the missing value.
    * $\text{Missing} = S_{\text{expected}} - S_{\text{set}}$

This method provides an extremely clean and highly performant solution in Python.

## ⏱️ Complexity Analysis

* **Time Complexity:** $O(N)$
    * Converting the list to a set takes $O(N)$ time.
    * Calculating sums (`sum()` function) takes $O(N)$ time.
    * All other operations are $O(1)$. Thus, the overall complexity is linear.

* **Space Complexity:** $O(N)$
    * We create a new `set` data structure which, in the worst case, holds $N-1$ elements. Therefore, the space complexity is linear.
