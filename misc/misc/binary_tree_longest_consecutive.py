# 298. Binary Tree Longest Consecutive Sequence


'''DFS'''
class Solution(object):
    def longestConsecutive(self, root):
        '''CONSECUTIUVE means non-decreasing in step of 1'''
        self.ans = 0
        if not root: return 0
        def dfs(root, pval, count):
            if not root:
                self.ans = max(self.ans, count + 1)
                return
            if root.val != pval + 1:
                self.ans = max(self.ans, count + 1)
                # reset
                dfs(root.left, root.val, 0); dfs(root.right, root.val, 0)
            else:
                dfs(root.left, root.val, count + 1); dfs(root.right, root.val, count + 1)


        dfs(root.left, root.val, 0)
        dfs(root.right, root.val, 0)
        return self.ans

'''bfs'''
class Solution(object):
    def longestConsecutive(self, root):
        if not root: return 0
        q = [(root, 1)]
        ans = 0
        while q:
            cur, count = q.pop(0)
            ans = max(ans, count)
            for child in (cur.left, cur.right):
                if child:
                    c = count + 1 if child.val == cur.val + 1 else 1
                    q.append((child, c))
        return ans
