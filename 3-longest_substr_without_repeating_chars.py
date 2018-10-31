class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_pos = {}
        start, end = 0, 0
        s = s + "@"
        ret = 0
        while end < len(s):
            ret = max(ret, end-start)
            if s[end] in char_pos:
                start = max(char_pos[s[end]] + 1, start)
            char_pos[s[end]] = end
            end += 1
        return ret
        # from collections import defaultdict
        # d = defaultdict(int)
        # start = end = 0
        # ans = 0
        # while end < len(s):
        #     d[s[end]] += 1
        #     while d[s[end]] == 2:
        #         d[s[start]] -= 1
        #         start += 1
        #     end += 1
        #     ans = max(ans, end-start)
        # return ans
