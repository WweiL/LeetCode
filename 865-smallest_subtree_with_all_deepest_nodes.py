# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        n, _ = self.subTreeHelper(root, 0)
        return n

    def subTreeHelper(self, root, depth):
        if not root.left and not root.right:
            return root, depth
        left, distL = self.subTreeHelper(root.left, depth+1) if root.left else (None, 0)
        right, distR = self.subTreeHelper(root.right, depth+1) if root.right else (None, 0)
        if distL == distR:
            return root, distL
        return (left, distL) if distL > distR else (right, distR)
