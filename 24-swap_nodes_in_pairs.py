# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        elif not head.next:
            return head
        else:
            tmp = head.next
            head.next = self.swapPairs(head.next.next)
            tmp.next = head
            return tmp
