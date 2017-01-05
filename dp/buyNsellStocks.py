
# coding: utf-8

# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# 
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# 
# 
# ## A variation of maximum subarray problem and can be solved using Kadane's algo

# In[9]:

import numpy as np
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur_profit = opt_profit = 0
        n = len(prices)
        minprice = np.inf
        for i in range(0, n):
            
            if prices[i] < minprice:
                minprice = prices[i]
    
            cur_profit = prices[i] - minprice

            opt_profit = max(cur_profit, opt_profit)

        return opt_profit


# In[10]:

prices = [7, 1, 5, 3, 6, 4]


# In[11]:

sol = Solution()


# In[12]:

sol.maxProfit(prices)


# In[ ]:


5



