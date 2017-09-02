# 117. Populating Next Right Pointers in Each Node II
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        '''Idea is keep a dummy node to traverse down the tree level by level,
        and use head node to link the nodes on that level'''
        dummy = TreeLinkNode(0)
        head = dummy
        while root: # e.g. [1,2,3,4,#,#,5]
            if root.left:
                head.next = root.left # wind dummy to next level e.g. head -> 2
                head = head.next
            if root.right:
                head.next = root.right
                head = head.next
            root = root.next
            if not root:
                # rewind the head to head of next level and start traversing next level
                head = dummy
                root = dummy.next
                dummy.next = None # cut it head
