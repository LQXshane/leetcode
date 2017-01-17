class Solution(object):
    # merge sort, recursively
    def sortList(self, head):
        if not head or not head.next:
            return head
        # divide list into two parts
        fast, slow = head.next, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # the reason why this cut-into-half works:
        # init: slow and fast are neighbors
        # 1st loop: slow moves 1, fast moves 2 steps, they are two steps away
        # 2nd loop: 3 steps away
        # 3rd loop: 4 steps away
        # ...
        # the loop will break when fast pointer reaches the end of this list
        second = slow.next
        # cut down the first part, using slow is legit because
        # in python you slow = head(like in init) allows the access of "slow" to the address of this list,
        # we will be making changes to the list then
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    def merge(self, l, r):
        # both l and r are sorted lists
        dummy = tail = ListNode(None)
        while l and r:
            if l.val < r.val:
                tail.next, tail, l = l, l, l.next
            else:
                tail.next, tail, r = r, r, r.next

        # if l1 or l2 does not have more than one elements, break the loop
        tail.next = l or r
        return dummy.next