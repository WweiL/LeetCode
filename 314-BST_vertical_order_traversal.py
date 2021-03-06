# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l = {}
        self.traversal(0, 0, root, l)
        sort = [item[1] for item in sorted(l.items(), key=lambda d: d[0])]
        ans = []
        for i in sort:
            ans.append([j[1] for j in sorted(i, key=lambda d: d[0])])
        return ans
        
    def traversal(self, i, j, root, l):
        if not root:
            return
        else:
            l[i] = l.get(i, [])
            l[i].append((j, root.val))
            self.traversal(i-1, j+1, root.left, l)
            self.traversal(i+1, j+1, root.right, l)

    
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = collections.deque()
        q.append((root, 0))
        l, r = 0, 0
        level_node = collections.defaultdict(list)
        while q:
            node, vertical_level = q.popleft()
            l, r = min(l, vertical_level), max(r, vertical_level)
            level_node[vertical_level].append(node)
            if node.left:
                q.append((node.left, vertical_level-1))
            if node.right:
                q.append((node.right, vertical_level+1))
        
        return [[node.val for node in level_node[i]] for i in range(l, r+1)]
            
#     def verticalOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         l = {}
#         self.traversal(0, 0, root, l)
#         sort = [item[1] for item in sorted(l.items(), key=lambda d: d[0])]
#         ans = []
#         for i in sort:
#             ans.append([j[1] for j in i])
#         return ans
        
#     def traversal(self, i, j, root, l):
#         if not root:
#             return 
#         else:
#             l[i] = l.get(i, [])
#             l[i].append((j, root.val))
#             self.traversal(i-1, j+1, root.left, l)
#             self.traversal(i+1, j+1, root.right, l)

        
