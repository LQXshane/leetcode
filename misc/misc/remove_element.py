# 203. Remove Linked List Elements
class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(None)
        dummy.next = head
        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return dummy.next
