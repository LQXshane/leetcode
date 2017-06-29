# House in Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.helper(root)
        return max(res)
        
    def helper(self, root):
        if root is None: return [0,0]
        left, right  = self.helper(root.left), self.helper(root.right)
        res = [0,0]
        # root house is not robbed
        res[0] = max(left[0], left[1])+max(right[0],right[1])
        
        # root house is robbed
        res[1] = root.val+left[0]+right[0]
        return res
        
