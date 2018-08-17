# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        iterator = head
        prev = None
        while iterator.next:
            tmp = iterator.next
            iterator.next = prev
            
            prev = iterator
            iterator = tmp

        iterator.next = prev
        return iterator
