# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return
        ans = [float('inf')]
        self.tra(root, target, ans)
        return ans[0]
    
    def tra(self, root, target, ans):
        if not root:
            return
        if abs(ans[0]-target) > abs(root.val-target):
                ans[0] = root.val
        if target == root.val:
            return root.val
        elif target < root.val:
            self.tra(root.left, target, ans)
        else:
            self.tra(root.right, target, ans)
            
