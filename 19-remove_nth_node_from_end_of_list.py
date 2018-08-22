# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        sentinel = ListNode(0)
        sentinel.next = head
        def remove(head, n):
            if not head.next:
                return 0
            else:
                loc = 1 + remove(head.next, n)
                if loc == n:
                    head.next = head.next.next
                return loc
            
        remove(sentinel, n)
        return sentinel.next
