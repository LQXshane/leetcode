# 523. Continuous Subarray Sum

# class Solution(object):
#     def checkSubarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         for i in range(1, len(nums)):
#             for j in range(i):
#                 if (k != 0 and sum(nums[j:i + 1])%k == 0) or sum(nums[j:i + 1])==0:
#                     return True
#         return False
# O(n^3)

# https://leetcode.com/problems/continuous-subarray-sum/solution/

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        runningSum = 0
        seen = {0:-1}
        for i, x in enumerate(nums):
            runningSum += x
            if k != 0: runningSum %= k
            if runningSum in seen:
                if i - seen[runningSum] > 1:
                    return True
            else:
                seen[runningSum] = i
            # print seen, runningSum
        return False

sol = Solution()
sol.checkSubarraySum([23,2,6,4,7], 6)
