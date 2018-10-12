# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # greedy
        if not intervals:
            return 0
        intervals.sort(key=lambda d: d.start)
        end = intervals[0].end
        erased = 0
        for i in intervals[1:]:
            if i.start < end:
                erased += 1
                end = min(i.end, end)
            else:
                end = i.end
        return erased
#         # dp is good, but TLE
#         def overlap(i, j):
#             # assume i < j, intervals is sorted
#             return intervals[i].end > intervals[j].start
        
#         if not intervals:
#             return 0
#         n = len(intervals)
#         dp = [1] * n
#         ans = 1
#         intervals.sort(key=lambda d: d.start)
        
#         for i in range(n-2, -1, -1):
#             max_remained = 0
#             for j in range(i+1, n):
#                 if not overlap(i, j):
#                     max_remained = max(max_remained, dp[j]+1)

#             dp[i] = max_remained
#             ans = max(ans, dp[i])
#         return n - ansclass Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s) or s == [] and p == []:
            return []
        d_fin = {}
        d_working = {}
        res = []
        len_p = len(p)
        for i in s+p:
            d_fin[i] = 0
            d_working[i] = 0
            
        for i in p:
            d_fin[i] += 1
        
        for i in s[:len_p]:
            d_working[i] += 1
        
        if d_working == d_fin:
            res.append(0)
            
        for i in range(len(s)-len_p):
            # one element before the start of the window, to be deleted
            before_window_start = s[i]
            window_end = s[i+len_p]
            d_working[before_window_start] -= 1
            d_working[window_end] += 1
            if d_working == d_fin:
                res.append(i+1)
                
        return res
        
# Have no clue wtf this is
# class Solution(object):
#     def findAnagrams(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: List[int]
#         """
#         dp = self.build_dict(p)
#         pointer = 0
#         n = len(p)
#         m = len(p)
#         counter = 0
#         ans = []
#         while end < m:
#             i = s[end]
#             dp[i] = dp.get(i, "#")
#             if dp[i] != "#":
#                 dp[i] -= 1
#                 if dp[i] == 0:
#                     counter += 1
#                 if counter == n:
#                     ans.append(start)
#                     counter = 0
#                 end += 1
#             else:
#                 m += end - start + 1
#                 start = end + 1
                
#         while start < len(s)-1:
#             if dp[s[start]] != "#": dp[s[start]] -= 1
#             if end < len(s)-1:
#                 end += 1
#                 dp[s[end]] = dp.get(s[end], "#")
#                 if dp[s[end]] != "#": dp[s[end]] += 1
#             start += 1
#             dp[s[start]] = dp.get(s[start], "#")
#             if dp[s[start]] != "#": dp[s[start]] += 1
#             if dp[s[start]] == 0: counter += 1
#             if dp[s[end]] == 0: counter += 1
#             if counter == n:
#                 ans.append(start)
#                 counter = 0
        
#         return ans
                    
#     def build_dict(self, p):
#         dp = {}
#         for i in p:
#             dp[i] = dp.get(i, 0) + 1
#         return dp

# O(n**2) TLE
# class Solution(object):
#     def findAnagrams(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: List[int]
#         """
#         if len(p) > len(s):
#             return []
#         res = []
#         n = len(p)
#         for i in range(0, len(s) - n + 1):
#             substring = s[i:i+n]
#             if self.isAnagram(substring, p):
#                 res.append(i)
#         return res
            
#     def isAnagram(self, s, p):
#         n = len(p)
#         s_dict = {}
#         for i in range(n):
#             s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        
#         for i in range(n):
#             val = p[i]
#             tmp = s_dict.get(val, 0) - 1
#             if tmp == -1:
#                 return False
#             s_dict[val] = tmp

#         return sum(s_dict.values()) == 0
