# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        nodes = {}
        # random may points to None!
        nodes[None] = None
        curr = head
        # store all nodes' labels
        while curr:
            nodes[curr] = RandomListNode(curr.label)
            curr = curr.next
        
        curr = head
        while curr:
            n = nodes[curr]
            n.next = nodes[curr.next]
            n.random = nodes[curr.random]
            curr = curr.next
            
        return nodes[head]
