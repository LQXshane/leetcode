# 295. Data Stream Median
from heapq import *

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.small) == len(self.large):
            heappush(self.large, - heappushpop(self.small, -num))
        else:
            heappush(self.small, - heappushpop(self.large, num))
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return (- self.small[0] + self.large[0]) / 2.0
        else:
            return float(self.large[0])
