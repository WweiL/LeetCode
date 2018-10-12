# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import collections
class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        one_before_middle = self.findOneBeforeMiddle(head)
        self.reverse(head, one_before_middle)
        middle = one_before_middle.next
        # Do the reorder
        first = head
        second = middle
        while first != middle:
            f_next = first.next
            s_next = second.next
            first.next = second
            second.next = second.next if f_next == middle else f_next
            first = f_next
            second = s_next
        
        
    def findOneBeforeMiddle(self, head):
        one_step = head
        two_step = head
        while two_step.next:
            prev = one_step
            one_step = one_step.next
            two_step = two_step.next
            if two_step.next == None:
                break
            two_step = two_step.next
        return prev
    
    def reverse(self, head, one_before_middle):
        prev = one_before_middle.next
        curr = prev.next
        tmp = prev
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        one_before_middle.next = prev
        tmp.next = None
# TLE:
# class Solution:
#     def reorderList(self, head):
#         """
#         :type head: ListNode
#         :rtype: void Do not return anything, modify head in-place instead.
#         """
#         while head and head.next:
#             before_tail, tail = self.tail(head)
#             if head in [before_tail, tail]:
#                 break
#             tail.next = head.next
#             head.next = tail
#             before_tail.next = None
#             head = tail.next
        
#     def tail(self, head):
#         if head.next == None:
#             return None, head
#         while head.next.next != None:
#             head = head.next
#         return head, head.next
