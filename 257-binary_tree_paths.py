# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return self.pathFinder(root)
    
    def pathFinder(self, root):
        # base case
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        # recursion step
        left = self.pathFinder(root.left)
        right = self.pathFinder(root.right)
        ans = []
        for i in left+right:
            ans.append(str(root.val) + "->" + i)
        return ans
