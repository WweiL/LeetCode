# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def tra(root, level, ans):
            if not root:
                return
            if level == len(ans):
                ans.append([root.val])
            else:
                ans[level].append(root.val)
            tra(root.left, level+1, ans)
            tra(root.right, level+1, ans)
        
        ans = []
        tra(root, 0, ans)
        return ans
