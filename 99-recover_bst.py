# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        tree = []
        def inorder_traversal(root):
            if root.left:
                inorder_traversal(root.left)
            tree.append(root)
            if root.right:
                inorder_traversal(root.right)
        inorder_traversal(root)
        n = len(tree)
        for i in range(n-1):
            if tree[i].val > tree[i+1].val:
                tree[i].val, tree[i+1].val = tree[i+1].val, tree[i].val
        
        for i in range(n-1, 0, -1):
            if tree[i].val < tree[i-1].val:
                tree[i].val, tree[i-1].val = tree[i-1].val, tree[i].val
        
            
