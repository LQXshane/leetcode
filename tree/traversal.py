# 1. INORDER TRAVERSAL
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.traverse = list()
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.inorderTraversal(root.left)
            self.traverse.append(root.val)
            self.inorderTraversal(root.right)
        
        return self.traverse
        
#### also, iteratively: ########

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans, stack = [], []
        
        while root or stack:
            if root:
                stack.append(root) # put nodes in a stack
                root = root.left
                
            else:
                tmp = stack.pop()
                ans.append(tmp.val)
                root = tmp.right
        return ans

# 2. Preorder

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # remember Stack property: LIFO
        
        res, stack = [], [root]
        
        while stack:
            
            cur = stack.pop()
            
            if cur:
                
                res.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
                
        return res
