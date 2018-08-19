# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not(l1 and l2):
            return None
        
        
        head = ListNode((l1.val + l2.val) % 10)
        c_out = (l1.val + l2.val) // 10
        l1 = l1.next
        l2 = l2.next
        curr = head
        while l1 or l2:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            val = (val1+val2 + c_out) % 10
            c_out = (val1+val2 + c_out) // 10
            curr.next = ListNode(val)
            curr = curr.next
        
        if c_out:
            curr.next = ListNode(c_out)
        return head
