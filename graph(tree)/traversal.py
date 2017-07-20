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



# 3. Post order:

# can be done in two ways: one, strictly follow the concept of postorder traversal; 
# second is to reverse the result of a **modified** pre-order traversal


# https://discuss.leetcode.com/topic/17540/share-my-two-python-iterative-solutions-post-order-and-modified-preorder-then-reverse ##
# also, check this detailed tutorial using 2 stacks:
# http://www.geeksforgeeks.org/iterative-postorder-traversal/
# using 2nd idea:


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res, stack = [], [root] # using two stacks
        ans = []
        while stack:
            
            node = stack.pop()

            res.append(node)
            if node.left is not None:
                stack.append(node.left) 
            if node.right is not None:
                stack.append(node.right) 
            
        while res:
            
            node = res.pop()
            ans.append(node.val)
            
        return ans
