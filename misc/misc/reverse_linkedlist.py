# 206. Reverse Linked List

"""Iterative"""
class Solution(object):
    def reverseList(self, head):
        if not head: return head
        pre = None

        while head:
            head.next, head, pre = pre, head.next, head
        return pre
"""Recursive"""

# e.g. 1->2->3<-4
# for node 2, 2.next.next = 3.next = 2
# then cut off the tail by 2.next = None
# or there will be cycle
class Solution2(object):
    def reverseList(self, head):
        if not head or not head.next: return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


# 92. Reverse Linked List II
'''Reverse a linked list from position m to n. Do it in-place and in one-pass.
'''
class Solution(object):
    def reverseBetween(self, head, m, n):
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        for i in range(m - 1): pre = pre.next
        start = pre.next
        then = start.next
        for i in range(n - m):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
        return dummy.next


'''
关于slow fast指针

        # slow, fast = head, head.next
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow
如果是奇数长度的链表，slow返回的是 (n+1)/2 处的node
如果是偶数长度的链表，slow返回的是 n/2处的node
'''


class Solution(object):
    def reverseSecondHalf(self, head, m, n):
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        slow, fast = head, head.next
        while fast and fast.next:
            pre = pre.next
            slow = slow.next
            fast = fast.next.next

        then = slow.next
        while slow.next:
            slow.next = then.next
            then.next = pre.next
            pre.next = then
            then = slow.next
        return dummy.next
