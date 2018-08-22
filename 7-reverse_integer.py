class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = 1
        if x < 0:
            x = -x
            neg = -1
        ans = 0
        y = x
        i = 0.1
        while y:
            y //= 10
            i *= 10
            
        while x:
            ans += x % 10 * i
            x //= 10
            i //= 10

        ans = int(ans * neg)
        return ans if -2**31 < ans < 2**31 -1 else 0
