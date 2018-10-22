from collections import defaultdict
from bisect import bisect_left
class Solution:
    def buildDict(self, t):
        self.letter_pos = defaultdict(list)
        for i in range(len(t)):
            self.letter_pos[t[i]].append(i)

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # follow up
        m = len(s)
        n = len(t)
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False

        self.buildDict(t)
        pos = 0
        for i in s:
            if i not in self.letter_pos:
                return False
            pos_i = self.letter_pos[i]
            k = bisect_left(pos_i, pos)
            if k == len(pos_i):
                return False
            pos = pos_i[k] + 1
        return True
        # iterate over t, slow
#         m = len(s)
#         n = len(t)
#         if len(s) == 0:
#             return True
#         if len(t) == 0:
#             return False
        
#         i, j = 0, 0
#         while i < m and j < n:
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
#         return i == m
#         # still iterate over t, but faster
#         if len(t) == 1 and s != t:
#             return False
#         index = 0
#         for i in range(len(s)):
#             ind = t.find(s[i], index)
#             if ind == -1:
#                 return False
            
#             #print("found", s[i],"at", ind)
#             index = ind +1
            
#         return True
        
