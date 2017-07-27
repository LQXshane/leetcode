# 378

from heapq import *
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        h = [(row[0], row, 1) for row in matrix] #min-heap
        heapify(h)
        
        for _ in xrange(k-1): # geneator that ranges lazily!!
            
            num, row, idx = h[0]
            
            if idx < len(row): # pop the smallest of that heap"h[0]"" and insert the second-smallest of that row into comparison
                heapreplace(h, (row[idx], row, idx+1))
            else: # there are no bigger numbers in this row
                heappop(h)
        return h[0][0]
