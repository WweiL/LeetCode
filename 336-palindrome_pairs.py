class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPal(s):
            l = 0
            r = len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                r -= 1
                l += 1
            return True

        w = {}
        for i, v in enumerate(words):
            w[v] = i
        ans = set()
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n+1):
                prefix = word[:j]
                p_reverse = word[j:]
                p_reverse = p_reverse[::-1]
                if isPal(prefix) and p_reverse in w and w[p_reverse] != i:
                    ans.add((w[p_reverse], i))
                suffix = word[n-j:]
                s_reverse = word[:n-j]
                s_reverse = s_reverse[::-1]
                if isPal(suffix) and s_reverse in w and w[s_reverse] != i:
                    ans.add((i, w[s_reverse]))
        res = []
        for i in ans:
            res.append([i[0], i[1]])
        return res
                    
