# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        return self.mergeSort(head)
    
    def mergeSort(self, head):
        if not head.next:
            return head
        # get middle, middle->next = None to split
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None
        # mergeSort head to middle, middle to tail
        head = self.mergeSort(head)
        middle = self.mergeSort(middle)
        # merge head->middle, middle->tail
        head = self.merge(head, middle)
        return head
        
    def merge(self, n1, n2):
        dummy = ListNode(0)
        curr = dummy
        while n1 or n2:
            if not n1 or not n2:
                if not n1:
                    curr.next = n2
                    n2 = n2.next
                else:
                    curr.next = n1
                    n1 = n1.next
            else:
                if n1.val < n2.val:
                    curr.next = n1
                    n1 = n1.next
                else:
                    curr.next = n2
                    n2 = n2.next
            curr = curr.next
        r = dummy.next
        return dummy.next
