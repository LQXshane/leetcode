
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0: return False
        bucket = {}
        window = t + 1
        for i in range(len(nums)):
            idx = nums[i]/window
            
            if idx in bucket: return True
            if idx-1 in bucket and abs(nums[i]-bucket[idx-1]) < window: return True
            if idx+1 in bucket and abs(nums[i]-bucket[idx+1]) < window: return True
        
            bucket[idx] = nums[i]
            
            if len(bucket) > k: del bucket[nums[i-k]/window]
        return False
