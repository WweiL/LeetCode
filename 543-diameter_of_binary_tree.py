# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.d = 0
        self.diameterFinder(root)
        return self.d-1

    def diameterFinder(self, root):
        if not root:
            return 0
            
        left = self.diameterFinder(root.left)
        right = self.diameterFinder(root.right)
        self.d = max(self.d, left + right + 1)
        return max(left, right) + 1
        
