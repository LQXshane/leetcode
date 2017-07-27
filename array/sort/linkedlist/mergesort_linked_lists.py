# Bottom-up Merge Sort, Space complexity O(1), uses iterative algo.
# Singly linked lists

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        # count the len of this list
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        dummy = ListNode(0)
        dummy.next = head

        left = right = tail = ListNode(None)

        step = 1
        while step < length:
            tail, cur = dummy, dummy.next
            while cur:
                left = cur
                right = self.split(left, step) # will define split later
                tail = self.merge(left, right, tail)
            step <<= 1 # bit operator

        return dummy.next

    def split(self, head, step_size):
        i = 1
        while head:
            if i >= step_size:
                break
            head = head.next
            i += 1
        if not head:
            return None
        second = head.next
        head.next = None
        return second

    def merge(self, l, r, head):
        cur = head
        while l and r:
            if l.val > r.val:
                cur.next = r
                cur = r
                r = r.next
            else:
                cur.next = l
                cur = l
                l = l.next

        cur.next = l or r
        while cur.next:
            cur = cur.next
        return cur




