class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def findWord(s, i):
            res = ""
            while i < len(s) and s[i] == ' ':
                i += 1
            while i < len(s) and s[i] != ' ':
                res += s[i]
                i += 1
            return res, i
        
        if not input:
            return ""
        else:
            i = 0
            ans = []
            while i < len(s):
                word, pos = findWord(s, i)
                if i > 0 and word == "": break
                ans.append(word)
                i = pos
            ans.reverse()
            return " ".join(ans)
        
