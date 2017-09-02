# 114. Flatten Binary Tree to Linked List
'''[1,2,5,3,4,6]
flatten(1)
flatten(2)
flatten(3), pre = 3
flatten(None), return
root = 2, tmp = 4
2 -> 3(pre) -> 4
flatten(4)
...
'''
class Solution(object):
    def flatten(self, root):
        if not root: return
        self.prev = root
        self.flatten(root.left)
        tmp = root.right
        root.right, root.left = root.left, None
        self.prev.right = tmp
        self.flatten(tmp)
