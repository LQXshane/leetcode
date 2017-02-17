

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for i in range(len(nums)):
            
            xor = xor ^ i ^ nums[i]
            
        return xor^(len(nums))
