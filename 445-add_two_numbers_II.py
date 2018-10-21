# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution():
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.getLength(l1)
        n2 = self.getLength(l2)
        if n1 > n2:
            l1, l2 = l2, l1
            n1, n2 = n2, n1
        head = self.sumNode(l1, l2, n1, n2)
        next = head.next
        head.next = None
        h = self.reverseAndAdd(head, next, 0)
        r = h
        while(r):
            print(r.val)
            r = r.next
        return h

    def reverseAndAdd(self, head, next, carryIn):
        carryOut = 0
        head.val += carryIn
        if head.val >= 10:
            head.val -= 10
            carryOut = 1
        # base case
        if not next:
            if carryOut == 1:
                next = ListNode(1)
                return self.reverseAndAdd(head, next, 0)
            return head

        tmp = next.next
        next.next = head
        return self.reverseAndAdd(next, tmp, carryOut)

    def sumNode(self, l1, l2, n1, n2):
        # length of l1 is less than length of l2
        head = None
        while n2 > 0:
            if n2 > n1:
                head = self.addFront(l2.val, head)
                n2 -= 1
                l2 = l2.next
            else:
                head = self.addFront(l1.val+l2.val, head)
                l1, l2 = l1.next, l2.next
                n1, n2 = n1-1, n2-1
        return head

    def addFront(self, val, currHead):
        head = TreeNode(val)
        head.next = currHead
        return head
        
    def getLength(self, l):
        ret = 0
        while l:
            ret += 1
            l = l.next
        return ret
        
        
