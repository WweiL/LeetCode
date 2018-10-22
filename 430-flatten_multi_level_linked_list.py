"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        self.flattenHelper(head)
        return head

    def flattenHelper(self, head):
        # flatten the linked list after node head
        # retutn the tail of the flattened list
        if head.child:# Definition for a binary tree node.
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
            
            next = head.next
            child = head.child
            tail = self.flattenHelper(child)
            head.next = child
            child.prev = head
            head.child = None
            tail.next = next
            if next:
                next.prev = tail
            # if not next:
            #     return tail
            # self.flattenHelper(tail.next)
            head = tail
        if not head.next:
            return head
        return self.flattenHelper(head.next)
