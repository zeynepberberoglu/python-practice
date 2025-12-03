class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 'a' acts as the primary pointer/index for iterating through the array.
        a = 0
        # 'con' stores the count of consecutive ones in the current sequence.
        con = 0
        # 'general' list stores the consecutive counts found in each sequence (before hitting a 0).
        # We will take the max of this list at the end.
        general = []
        n = len(nums)
        
        while a < n:
            # Inner loop to count consecutive ones starting from the current 'a'
            while a < n:
                if nums[a] == 1:
                    con += 1
                    a += 1
                elif nums[a] == 0:
                    a += 1  # Move past the zero
                    break   # Break the inner loop (consecutive sequence is broken)
            
            # After the inner loop breaks (due to a 0 or end of array), 
            # the current consecutive count ('con') is stored.
            general.append(con)
            # Reset the current consecutive counter for the next search.
            con = 0

        # The result is the largest count found in the 'general' list.
        return max(general)