# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.d = -float('inf')
        self.pathSum(root)
        return self.d

    def pathSum(self, root):
        if not root:
            return 0
        left = self.pathSum(root.left)
        right = self.pathSum(root.right)
        self.d = max(self.d, left+root.val, right+root.val, left+right+root.val, root.val)
        return max(left+root.val, right+root.val, root.val)
