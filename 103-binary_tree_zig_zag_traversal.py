# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        q = deque()
        # q.append((root, 0, 0))
        q.append((root, 0))
        ans = []
        while q:
            # node, level, reverse = q.popleft()
            node, level = q.popleft()
            if level >= len(ans):
                ans.append([])
            ans[level].append(node.val)
            # if reverse == 1:
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
            # else:
                # if node.right:
                    # q.append((node.right, level+1, 1-reverse))
                # if node.left:
                    # q.append((node.left, level+1, 1-reverse))
        for i in range(len(ans)):
            if i % 2 == 1:
                ans[i].reverse()
        return ans
