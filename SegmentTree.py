class SegmentTreeNode():
    def __init__(
        self, 
        start, 
        end, 
        sum, 
        left = None, 
        right = None
    ):
        self.start = start
        self.end = end
        self.sum = sum
        self.left = left
        self.right = right
        self.mid = (start + end) // 2

# index: left, right inclusive
# [i, j]
class SegmentTree():
    def __init__(self, array):
        self.root = self.buildTree(0, len(array)-1, array)

    def buildTree(self, start, end, vals):
        if start == end:
            return SegmentTreeNode(start, end, vals[start])
        mid = (start + end) // 2
        left = self.buildTree(start, mid, vals)
        right = self.buildTree(mid+1, end, vals)
        return SegmentTreeNode(start, end, left.sum + right.sum, left, right)

    def updateTree(self, index, val):
        self._updateTree(self.root, index, val)

    def _updateTree(self, root, index, val):
        if root.start == root.end == index:
            root.sum = val
            return 
        if index <= root.mid:
            self._updateTree(root.left, index, val)
        else:
            self._updateTree(root.right, index, val)
        root.sum = root.left.sum + root.right.sum

    def querySum(self, i, j):
        return self._querySum(self.root, i, j)
    
    def _querySum(self, root, i, j):
        if root.start == i and root.end == j:
            return root.sum
        if j <= root.mid:
            return self._querySum(root.left, i, j)
        elif i > root.mid:
            return self._querySum(root.right, i, j)
        else:
            return self._querySum(root.left, i, root.mid) + \
                    self._querySum(root.right, root.mid+1, j)