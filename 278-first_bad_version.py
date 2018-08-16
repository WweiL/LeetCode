# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def binSearch(low, hi):
            middle = (low+hi) // 2
            if middle == low:
                return low if isBadVersion(low) else hi
            
            if isBadVersion(middle):
                return binSearch(low, middle)
            else:
                return binSearch(middle, hi)
            
        return binSearch(1, n)
