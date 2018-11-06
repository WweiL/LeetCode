# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list = []
        self.flatten(nestedList, self.list)
        self.pos = 0
        self.len = len(self.list)
        
    def flatten(self, nestedList, curr):
        for nInt in nestedList:
            if nInt.isInteger():
                curr.append(nInt.getInteger())
            else:
                self.flatten(nInt.getList(), curr)

    def next(self):
        """
        :rtype: int
        """
        ans = self.list[self.pos]
        self.pos += 1
        return ans
    

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pos < self.len
    

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
