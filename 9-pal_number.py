class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def isPal(x):
            if len(x) == 1 or len(x) == 0:
                return True
            elif x[0] != x[-1]:
                return False
            else:
                return isPal(x[1:-1])

        if x < 0:
            return False
        return isPal(str(x))

            
