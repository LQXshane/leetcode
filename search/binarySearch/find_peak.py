# 162. Find Peak Element
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r)/ 2
            if nums[mid] > nums[r]:
                r -= 1
            else:
                l += 1
                
        return l
                
