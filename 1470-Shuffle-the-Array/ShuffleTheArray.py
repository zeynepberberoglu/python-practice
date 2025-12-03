class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # The goal is to interleave the first half (x1...xn) and the second half (y1...yn).
        
        # 'a' will track the index for the first half (x1, x2, ...), starting at 0.
        a = 0
        
        # Initialize the result array 'out'.
        out = []
        
        # Iterate through the second half of the array. The second half starts at index n
        # and goes up to the end (2*n - 1).
        for i in range(n, 2 * n):
            # 1. Append the element from the first half (nums[a] which is xi)
            out.append(nums[a])
            
            # 2. Append the element from the second half (nums[i] which is yi)
            out.append(nums[i])
            
            # Move the pointer for the first half to the next element (x_i+1)
            a += 1
            
        return out