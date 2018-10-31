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
            if low == hi:
                return low
            
            middle = (low+hi) // 2
            if isBadVersion(middle):
                return binSearch(low, middle)
            else:
                return binSearch(middle+1, hi)
            
        return binSearch(1, n)
        # lo, hi = 1, n
        # while lo < hi:
        #     mid = lo + (hi-lo) // 2
        #     if isBadVersion(mid):
        #         hi = mid
        #     else:
        #         lo = mid+1
        # return lo
