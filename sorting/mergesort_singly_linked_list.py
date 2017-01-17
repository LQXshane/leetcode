# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
        if not head or not head.next: return head
        
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev, slow, fast  = slow, slow.next, fast.next.next
        prev.next = None
        
        return self.mergeList(*map(self.sortList, (head, slow)))
        

    def mergeList(self, l1, l2):
        dummy = tail = ListNode(None)
        while l1 and l2: #both l1 and l2 are sorted lists
            if l1.val < l2.val:
                tail.next, tail, l1 = l1, l1, l1.next
            else:
                tail.next, tail, l2 = l2, l2, l2.next
                
        # if l1 or l2 does not have more than one elements, break the loop
        tail.next = l1 or l2
        return dummy.next
                
            
