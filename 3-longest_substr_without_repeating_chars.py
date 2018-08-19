class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        d = defaultdict(int)
        start = end = 0
        ans = 0
        while end < len(s):
            d[s[end]] += 1
            while d[s[end]] == 2:
                d[s[start]] -= 1
                start += 1
            end += 1
            ans = max(ans, end-start)
        return ans
