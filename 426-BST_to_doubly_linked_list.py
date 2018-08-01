"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return None
        else:
            left, right = self.flatten(root)
            left.left = right
            right.right = left
            return left

    def flatten(self, root):
        if not root.left and not root.right:
            return root, root
        else:
            head = tail = root
            if root.left:
                left, right = self.flatten(root.left)
                head = left
                root.left = right
                right.right = root
            if root.right:
                left, right = self.flatten(root.right)
                tail = right
                root.right = left
                left.left = root
            return head, tail
