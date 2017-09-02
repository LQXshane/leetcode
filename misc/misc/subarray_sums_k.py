# 560. Subarray Sum Equals K

# O(n) preSum, Space also O(n)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = collections.defaultdict(int)
        seen[0] = 1
        count = 0
        r = 0
        for i in range(len(nums)):
            r += nums[i]
            if r - k in seen:
                count += seen[r-k]
            seen[r] += 1
        return count

# 2 loops, O(n^2) with O(1) Space, TLE

class Solution2(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k: count += 1
        return count
