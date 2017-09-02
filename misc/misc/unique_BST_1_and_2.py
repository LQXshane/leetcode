
# 96. Unique Binary Search Trees


'''--------------------------------------------------
G(n) = F(1, n) + F(2, n) + ... + F(n, n)
G(n) is the number of valid BST's consist of 1,2,..., n
F(i, n) is the number of such valid BST's with root at i
Simplify the equation:
F(i, n) = G(i-1) * G(n - i), where G(0) = 1, G(1) = 1
it follows,
G(n) = G(0) * G(n - 1) + G(1) * G(n - 2) +  + … + G(n-1) * G(0)
-----------------------------------------------------'''


class Solution_96(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        trees = [0 for _ in xrange(n + 1)]
        trees[0] = trees[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                trees[i] += trees[j -1 ] * trees[i - j]
        return trees[n]





# 95. Unique Binary Search Trees II

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''same idea, choose root at i,
and choose its left child from left_nodes,
right child from right_nodes'''

class Solution(object):
    def generateTrees(self, n):
        if not n: return []
        def helper(start, end):
            res = []
            for i in range(start, end + 1):
                left_nodes = helper(start, i - 1)
                right_nodes = helper(i + 1, end)
                for left in left_nodes:
                    for right in right_nodes:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)

            return res or [None]
        return helper(1, n)
