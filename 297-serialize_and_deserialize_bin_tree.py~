# def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         if not root: return ''
#         # bfs
#         queue = collections.deque()
#         queue.append(root)
#         result = []
#         while queue:
#             node = queue.popleft()
#             # op at node
#             result.append(str(node.val) if node else 'null')
            
#             # go down to children
#             if node:
#                 queue.append(node.left)
#                 queue.append(node.right)
#         return ' '.join(result)
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         if not data: return None
        
#         vals = data.split(' ')
#         root = TreeNode(int(vals[0]))
#         # bfs
#         queue = collections.deque()
#         queue.append(root)
#         endIndex = 0
#         while queue:
#             node = queue.popleft()
#             # if node:
#             endIndex += 1
#             if vals[endIndex] != 'null':
#                 node.left = TreeNode(int(vals[endIndex]))
#                 queue.append(node.left)
#             endIndex += 1
#             if vals[endIndex] != 'null':
#                 node.right = TreeNode(int(vals[endIndex]))
#                 queue.append(node.right)
                
#         return root
            
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # CAUTION!
        if root == None:
            return []
        
        queue = collections.deque()
        queue.append(root)
        ans = []
        while queue:
            root = queue.popleft()
            if not root:
                ans.append(None)
            else:
                ans.append(root.val)
                queue.append(root.left)
                queue.append(root.right)
        return ans
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # CAUTION!
        if data == []:
            return []
        queue = collections.deque()
        root = TreeNode(data.pop(0))
        queue.append(root)
        endIdx = 0
        while queue and endIdx < len(data):
            r = queue.popleft()
            if r:
                # GOOD! TODO: use a pointer
                # NOT GOOD!
                left = TreeNode(data.pop(0)) if data[0] != None else data.pop(0)  # CAUTION!
                right = TreeNode(data.pop(0)) if data[0] != None else data.pop(0) # CAUTION!
                r.left = left
                r.right = right
                queue.append(left)
                queue.append(right)

        return root if root else []

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
