# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            head, tail, valid = self.flatten(root)
            return valid
        
    def flatten(self, root):
        if not root.left and not root.right:
            return root, root, True
        else:
            head = tail = root
            valid = True
            if root.left:
                left, right, v = self.flatten(root.left)
                head = left
                valid = valid and right.val < root.val and v and root.left.val < root.val

            if root.right:
                left, right, v = self.flatten(root.right)
                tail = right
                valid = valid and left.val > root.val and v and root.right.val > root.val

            return head, tail, valid
