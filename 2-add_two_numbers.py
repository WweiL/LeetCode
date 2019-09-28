# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        carryout, l = 0, head
        while l1 or l2:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            l.next = ListNode((v1 + v2 + carryout) % 10)
            carryout = (v1 + v2 + carryout) // 10
            l = l.next
        if carryout:
            l.next = ListNode(carryout)
        return head.next
