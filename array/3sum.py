 
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n, cur = len(nums), 0
        if n <= 2: return []
        if n == 3 and sum(nums) == 0: return [sorted(nums)]
        
        nums.sort()
        res = []
        
        for i in range(n-2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            print i
            lo, hi = i+1, n-1
            cur = nums[i]
            
            while lo < hi:
                if nums[lo] + nums[hi] == -cur:
                    if nums[lo] == nums[lo-1] and lo != i+1: pass
                    else:
                        res.append([nums[i], nums[lo], nums[hi]])
                    # print res
                if nums[lo] + nums[hi] > -cur: #WARNING ELIF DOESN"T WORK
                    hi -= 1
                else: # careful: this statement is executed when (nums[lo] + nums[hi] == -cur), too!
                    
                    lo += 1
        return res
                
                
