class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Get the length of the input array
        n = len(nums)
        # Initialize the result array 'ans'
        ans = []
        
        # 1. Append the first copy of nums to ans
        for i in range(n):
            ans.append(nums[i])
            
        # 2. Append the second copy of nums to ans
        # Using a while loop for the second iteration
        a = 0 
        while a < n:
            ans.append(nums[a])
            a += 1
            
        return ans

# --- Alternative (More concise Python solution using list concatenation) ---
# class Solution (object):
#     def getConcatenation(self, nums):
#         return nums + nums