# 102. Binary Tree Level Order Traversal
# DFS
class Solution(object):
    def levelOrder(self, root):
        def dfs(node, height):
            if not node: return
            if height >= len(res):
                res.append([])
            res[height].append(node.val)
            dfs(node.left, height + 1)
            dfs(node.right, height + 1)
        res = []
        dfs(root, 0)
        return res
# BFS1: using tuple
class Solution(object):
    def levelOrder(self, root):
        res = []
        if not root: return res
        queue = collections.deque([(root, 0)])
        while queue:
            curr, level = queue.popleft()
            if curr.left: queue.append((curr.left, level + 1))
            if curr.right: queue.append((curr.right, level + 1))
            if len(res) == level + 1:
                res[-1].append(curr.val)
            else:
                res.append([curr.val])
        return res
