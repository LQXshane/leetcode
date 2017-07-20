
# definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # fast and slow (pointer) will meet if the linked list has cycle
        # tortoise and hare algo:
        # https://zh.wikipedia.org/wiki/Floyd判圈算法
        # constant space O(1)
        
        slow, fast = head, head
        if not head: return False
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
            

# Also check this fabulous EAFP implementation by StefanPochmann 
# In discussion:

# def hasCycle(self, head):
#     try:
#         slow = head
#         fast = head.next
#         while slow is not fast:
#             slow = slow.next
#             fast = fast.next.next
#         return True
#     except:
#         return False
