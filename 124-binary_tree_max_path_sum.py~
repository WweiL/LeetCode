# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_global = -2**32
        self.maxPathSumFinder(root)
        return self.max_global
    
    def maxPathSumFinder(self, root):
        if not root:
            return 0
        else:
            left = right = 0
            if root.left:
                left = self.maxPathSumFinder(root.left)
            if root.right:
                right = self.maxPathSumFinder(root.right)

            both_side_val = left + right + root.val
            one_side_val = max(left, right) + root.val
            self.max_global = max(both_side_val, one_side_val, root.val, self.max_global)
            return max(one_side_val, root.val)
        
# Floyd-Warshall - IMPOSSIBLE!
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def maxPathSum(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         self.dist = {}
#         self.nodes = []
#         self.build_list(root)
#         self.initial_dist()
#         self.build_dist(root)
#         maxDist = 0
#         for k in self.nodes:
#             for i in self.nodes:
#                 for j in self.nodes:
#                     if self.dist[(i, j)] < self.dist[(i, k)] + self.dist[(k, j)]:
#                         self.dist[(i, j)] = self.dist[(i, k)] + self.dist[(k, j)]
#                         maxDist = max(self.dist[(i, j)], maxDist)
#         return maxDist
                    
#     def initial_dist(self):
#         for node1 in self.nodes:
#             for node2 in self.nodes:
#                 self.dist[(node1, node2)] = self.dist[(node2, node1)] = self.dist.get((node1, node2), 2**32-1)
        
#     def build_dist(self, root):
#         if root:
#             self.dist[(root, root)] = 0
#             if root.left:
#                 self.dist[(root, root.left)] = root.val+root.left.val
#                 self.dist[(root.left, root)] = root.val+root.left.val
#                 self.build_dist(root.left)
#             if root.right:
#                 self.dist[(root, root.right)] = root.val+root.right.val
#                 self.dist[(root.right, root)] = root.val+root.right.val
#                 self.build_dist(root.right)
                
#     def build_list(self, root):
#         if root:
#             self.nodes.append(root)
#             self.build_list(root.left)
#             self.build_list(root.right)
        
