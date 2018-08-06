class Solution:
    def validPalindrome(self, s):
        n = len(s)
        if n == 0 or n == 1:
            return True
        
        if self.isPalPart(0, n-1, s):
            return True
        else:
            low = 0
            hi = n-1

            while low < hi:
                if s[low] == s[hi]:
                    low += 1
                    hi -= 1
                else:
                    if self.isPalPart(low, hi-1, s):
                        return True
                    elif self.isPalPart(low+1, hi, s):
                        return True
                    else:
                        return False
            
# class Solution:
#     def validPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         n = len(s)
#         if n == 0 or n == 1:
#             return True
        
#         if self.isPal(s):
#             return True
#         else:
#             for i in range(len(s)):
#                 ss = s[:i] + s[i+1:]
#                 if self.isPal(ss):
#                     return True
#             return False
    def isPalPart(self, i, j, s):
        while(i < j):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def isPalAll(self, s):
        n = len(s)
        for i in range(n):
            if s[i] != s[n-i-1]:
                return False
        return True
