# 549. Binary Tree Longest Consecutive Sequence II
'''CONSECUTIUVE could be both increasing or decreasing, in step of 1
also, child-parent path is also allowed, e.g. [2,1,3]'''
class Solution(object):
    def longestConsecutive(self, root):

        self.ans = 0

        def dfs(node):
            if not node: return 0,0
            inc, dec = 1, 1
            if node.left:
                l = dfs(node.left)
                if node.val == node.left.val + 1:
                    dec = l[1] + 1
                elif node.val == node.left.val - 1:
                    inc = l[0] + 1
            if node.right:
                r = dfs(node.right)
                if node.val == node.right.val + 1:
                    dec = max(r[1] + 1, dec)
                elif node.val == node.right.val - 1:
                    inc = max(r[0] + 1, inc)
            self.ans = max(self.ans, inc + dec - 1)
            return inc, dec

        dfs(root)
        return self.ans
