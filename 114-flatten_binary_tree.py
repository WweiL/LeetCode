# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.postOrder(root)
    
    def postOrder(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root
        leftLeaf = self.postOrder(root.left)
        rightLeaf = self.postOrder(root.right)
        if leftLeaf:
            leftLeaf.right = root.right
            root.right = root.left
            root.left = None
        return rightLeaf if rightLeaf else leftLeaf
