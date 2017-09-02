# 121. Buy n Sell stock 1: One transcation only
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float("inf")
        profit = maxProfit = 0
        for p in prices:
            if p < minPrice: minPrice = p
            profit = p - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit

''' Solution 2: like continuous subarray sum'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        preSum = res = 0
        for i in range(1, len(prices)):
            preSum += prices[i] - prices[i-1]
            if preSum >= 0:
                res = max(res, preSum)
            else:
                preSum = 0
            # print preSum
        return res
