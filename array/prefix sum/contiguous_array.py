# 525. Contiguous Array

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        preSum = 0
        firstIndex = {0: -1}
        for i, x in enumerate(nums):
            if not x:
                preSum -= 1
            else:
                preSum += 1
            if preSum not in firstIndex:
                firstIndex[preSum] = i
            if preSum in firstIndex:
                ans = max(ans, i - firstIndex[preSum])
        return ans

# O(n)
