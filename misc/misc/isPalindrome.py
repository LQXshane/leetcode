class Solution(object):
    def isPalindrome(self, head):
        prev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            prev, prev.next, slow = slow, prev, slow.next # reverse the first half
        if fast: # odd length
            slow = slow.next
        while prev and prev.val == slow.val:
            slow = slow.next
            prev = prev.next
        return not prev
