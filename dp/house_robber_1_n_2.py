###### 1. Houses Adjacent ############
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        T = [0] * len(nums)
        
        for i in range(len(nums)):
            T[i] = max(T[i-2]+nums[i], T[i-1])
        return T[i]


########## 2. Houses in Cycle ############
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(nums,lo,hi):
            
            T = [0] *(hi-lo+1)
            
            for i in range(len(T)):
                
                T[i] = max(T[i-2]+nums[i+lo], T[i-1])
            
            return T[-1]
            

        if len(nums) == 1 or len(nums) == 2: return max(nums)
        if not nums: return 0
        n = len(nums)
        return max(helper(nums,0,n-2), helper(nums,1,n-1))
