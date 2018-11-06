class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return self.helper(0, x, x)
    
    def helper(self, lower, higher, x):
        half = int((lower+higher)/2)
        half_square = half ** 2
        if half_square <= x and (half+1) ** 2 > x:
            return half
        else:
            if half_square > x:
                higher = half
            else:
                lower = half
            return self.helper(lower, higher, x)

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l < r:
            mid = (l+r+1) // 2
            if (mid**2 <= x):
                l = mid
            else: # mid^2 > x, mid cannot be inside the interval
                r = mid-1
        return l
