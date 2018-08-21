# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return head.next
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if not l1:
#             return l2
#         if not l2:
#             return l1
#         r1 = l1
#         r2 = l2
#         head = l1 if l1.val < l2.val else l2
#         r = head
#         while r1 and r2:
#             if r1.val < r2.val:
#                 val = r1.val
#                 r1 = r1.next
#             else:
#                 val = r2.val
#                 r2 = r2.next
#             n = ListNode(val)
#             r.next = n
#             r = n
#         if r1:
#             r.next = r1
#         if r2:
#             r.next = r2
#         return head.next
