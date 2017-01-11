
# coding: utf-8

# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
# 
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# In[1]:

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        K = 2 # of transactions
        maxprof = 0
        n = len(prices)
        
        # error handling
        if n < 1: return 0
        
        
        M = [[0] * n for i in range(K)]
        
        # M[k][n] is the profit gained by k transactions up to day n
        
        for i in range(K):
            
            tmpmax = M[i-1][0] - prices[0]
            
            # initialize temporary maximum profit for each row 
            
            for j in range(n):
            
                M[i][j] = max(M[i][j-1], prices[j] + tmpmax)
                
                tmpmax = max(tmpmax, M[i-1][j] - prices[j])
                
                # to day j with the i-th transaction, two scenarios:
                
                # 1. sell stock at prices[j] and gain a profit out of max(M[i-1][j] - prices[j])
                
                # 2. not sell, if the profit does not exceed M[i][j-1]
                
                # concrete DP expression:
                
                # maxProfit[2][n] = max( maxprofit[2][n-1], max(maxProfit[1][n] - prices[n]))
                
                maxprof = max(M[i][j], maxprof)
                
        return maxprof#, M
            
        


# In[2]:

prices = [7, 1, 5, 3, 6, 4]

sol = Solution()

sol.maxProfit(prices)


# In[ ]:



