"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        node = Node(insertVal, None)
        if not head:
            return node
        if not head.next or head.next == head:
            head.next = node
            node.next = head
            return head
        smaller = self.findNextSmaller(head, insertVal)
        node.next = smaller.next
        smaller.next = node
        return head

    def findNextSmaller(self, head, val):
        if head.val <= val and head.next.val >= val:
            return head
        elif head.val >= head.next.val:
            if val > head.val or val < head.next.val:
                return head
            return self.findNextSmaller(head.next, val)
        else:
            print(head.val, val, head.next.val)
            return self.findNextSmaller(head.next, val)
