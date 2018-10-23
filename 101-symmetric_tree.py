# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.symHelper(root.left, root.right)
        
    def symHelper(self, node1, node2):
        if not node1 and not node2:
            return True
        elif node1 == None or node2 == None:
            return False
        elif node1.val != node2.val:
            return False
        else:
            return self.symHelper(node1.right, node2.left) and self.symHelper(node2.right, node1.left)
