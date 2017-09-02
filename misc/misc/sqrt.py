
# 69. Sqrt(x)

class Newton(object):
    def mySqrt(self, x):
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r

class Solution(object):
    def mySqrt(self, x):
        '''binary search'''
        if not x: return 0
        left, right = 1, x
        while True:
            mid = (left + right) / 2
            if mid > x / mid:
                right = mid - 1
            else:
                if mid + 1 > x / (mid + 1):
                    return mid
                left = mid + 1
