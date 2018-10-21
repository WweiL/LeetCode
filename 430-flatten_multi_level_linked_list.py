"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        self.flattenHelper(head)
        return head

    def flattenHelper(self, head):
        # flatten the linked list after node head
        # retutn the tail of the flattened list
        if head.child:
            next = head.next
            child = head.child
            tail = self.flattenHelper(child)
            head.next = child
            child.prev = head
            head.child = None
            tail.next = next
            if next:
                next.prev = tail
            # if not next:
            #     return tail
            # self.flattenHelper(tail.next)
            head = tail
        if not head.next:
            return head
        return self.flattenHelper(head.next)
