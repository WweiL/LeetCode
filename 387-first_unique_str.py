class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = {}
        for i in s:
            word[i] = word.get(i, 0) + 1
        for i in range(len(s)):
            if word[s[i]] == 1:
                return i
        return -1
