# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        one = head
        two = head
        while(two):
            one = one.next
            if two.next:
                two = two.next.next
            else:
                break
            if(one == two):
                return True
            
        return False
