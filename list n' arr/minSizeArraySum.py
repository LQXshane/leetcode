#209


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        min_len = float("inf")
        j = 0
        tmp = 0
        for i in range(len(nums)):
            while j < len(nums) and tmp < s: 
                # the trick is j also only loops through the array once!
                tmp += nums[j]
                j +=1
            if tmp >= s:
                min_len = min(min_len,j - i)
            tmp -= nums[i]
        return min_len if min_len!=float("inf") else 0
