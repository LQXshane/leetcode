
# coding: utf-8

# In[2]:

import numpy as np

nums= [-2,1,-3,4,-1,2,1,-5,4]

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
######## IDEA: maintain an 2D array M[idx, len] to find the maximum starting at each index
        
        n = len(nums)
        M = [[- np.inf ]*n for i in range(n)]
        
        
        for i in range(n):
            
            M[i][0] = nums[i]
                
            for j in range(i+1, n):
                
                M[i][j-i] = M[i][j-i-1]+ nums[j]
        
        arr = np.array(M).flatten()

        return int(max(arr))


####### This DP version naively runs in O(n)


# In[44]:

sol = Solution()


# In[45]:

sol.maxSubArray(nums)


# In[46]:

#### Kadane's algorithm solving max subarray sum problem

class Solution(object):
    def maxSubArray(self, nums):
        
        cur_sum = opt_sum = nums[0]
        
        for num in nums[1:]:
            
            
            
            if cur_sum + num < 0: cur_sum = 0
            
            cur_sum = max(cur_sum + num, num)
                
            opt_sum = max(cur_sum, opt_sum)
            
        return opt_sum
            
            
            
            
###### This runs in O(n) and beats 32% of python submissions

            


# In[47]:

sol2 = Solution()


# In[48]:

sol2.maxSubArray(nums)


# In[ ]:



