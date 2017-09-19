# 637. Average of Levels in Binary Tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        if not root: return []
        # level order traversal
        res = []
        queue = collections.deque([root])
        while queue:
            size = N = len(queue) # number of nodes on the level
            level_sum = 0
            while size > 0:
                node = queue.popleft()
                level_sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                size -= 1
            res.append(float(level_sum)/ N)
        return res
