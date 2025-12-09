class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        # 1. Calculate the expected sum of a perfect set (1 to n) using the arithmetic series formula.
        # Sum = n * (n + 1) / 2
        # Note: In Python 3, using // 2 for integer division might be safer if not strictly defined as float.
        expectedSum = (n * (n + 1)) // 2
        
        # 2. Calculate the actual sum of the given array (includes the duplicate).
        theSum = sum(nums)
        
        # 3. Calculate the sum of the array without the duplicate using the set structure.
        withoutDuplicate = sum(set(nums))
        
        # 4. Find the duplicated number:
        # The difference between the actual sum (which has the duplicate) and the sum without duplicates
        # must be equal to the value of the duplicated number itself.
        # Example: [1, 2, 2, 4] -> Sum=9, Set Sum=7. Duplicate = 9 - 7 = 2.
        duplicateNum = theSum - withoutDuplicate
        
        # 5. Find the missing number:
        # The difference between the Expected Sum and the Sum without Duplicates
        # must be equal to the missing number's value.
        # Example: Expected Sum (1 to 4) = 10. Set Sum = 7. Missing = 10 - 7 = 3.
        missingNum = expectedSum - withoutDuplicate
        
        return [duplicateNum, missingNum]
