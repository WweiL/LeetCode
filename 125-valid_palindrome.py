class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s)-1
        
        while start < end:
            while start < len(s) and not (s[start].isalpha() or s[start].isdigit()):
                start += 1
                
            while end >= 0 and not (s[end].isalpha() or s[end].isdigit()):
                end -= 1
            if start == len(s) or end == -1:
                break

            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
