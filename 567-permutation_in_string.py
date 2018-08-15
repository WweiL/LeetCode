class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        fin = {}
        working = {}
        for i in s1+s2:
            fin[i] = 0
            working[i] = 0
        for i in s1:
            fin[i] += 1
        
        for i in s2[:len(s1)]:
            working[i] += 1
        
        if working == fin: return True
        start = 0
        end = len(s1)
        while end < len(s2):
            working[s2[end]] += 1
            working[s2[start]] -= 1
            if working == fin:
                return True
            end += 1
            start += 1
        return False
