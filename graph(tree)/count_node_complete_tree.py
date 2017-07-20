# 1. Straight forward sol'n
# if left sub tree height == right's
# then left sub tree is a perfect BT
# else, right is perfect
# return the count of perfect trees using power of 2
# count others recuisively
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root):
            
            """
            :type root: TreeNode
            :rtype: int
            """
            if not root: return 0
            return 1+depth(root.left)
        
        if not root: return 0
        
        leftkid = depth(root.left)
        rightkid = depth(root.right)
        
        if leftkid == rightkid:
            # left sub tree perfect
            return pow(2, leftkid)+self.countNodes(root.right)
        else:
            # right sub tree perfect
            return pow(2, rightkid)+self.countNodes(root.left)

# LEARN USAGE OF NESTED FUNCTIONS IN PYTHON
