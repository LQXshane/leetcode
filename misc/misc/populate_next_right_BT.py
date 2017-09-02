# 116. Populating Next Right Pointers in Each Node
''' Assumming Perfect BST's '''
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
#
# [1,2,3,4,5,6,7]


'''Level order traversal works, but not optimal!
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            while size > 0:
                cur = queue.popleft()
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                size -= 1
                cur.next = None if size == 0 else queue[0]
'''
                
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        head = root
        while head: # head/; far left of the level
            cur = head
            while cur:
                if cur.left: cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            head = head.left # next level
