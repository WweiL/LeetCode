# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
                
        if not root:
            self.stack = None
            return
        
        self.stack = deque()
        self.pushLeft(root)
        # while root.left:
            # self.stack.append(root.left)
            # root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack == None:
            return False
        return len(self.stack) != 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        if node.right:
            self.pushLeft(node.right)
        return node.val
        
    def pushLeft(self, root):
        while root:
            self.stack.append(root)
            root = root.left
       
        
    
            

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
