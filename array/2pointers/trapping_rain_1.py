# 42. Trapping rain water
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        res = 0
        if l >= r: return res
        leftheight, rightheight = height[l], height[r]
        while l < r:
            if leftheight < rightheight:
                l += 1
                if leftheight > height[l]:
                    res += leftheight - height[l]
                else:
                    leftheight = height[l] # udpate left wall
                    
            else:
                r -= 1
                if rightheight > height[r]:
                    res += rightheight - height[r]
                else:
                    rightheight = height[r]
        return res
