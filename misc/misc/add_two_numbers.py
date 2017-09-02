class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = head = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            x, y = 0, 0
            if l1:
                x = l1.val
                l1 = l1.next
            if l2:
                y = l2.val
                l2 = l2.next
            head.next = ListNode((x + y + carry) % 10)
            carry = (x + y + carry) / 10
            head = head.next
        return dummy.next
