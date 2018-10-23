class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return self.findLS(s, k, 0, len(s))

    # Version 1, not good
#     def findLS(self, s, k, left, right):
#         # s[left, right)
#         from collections import Counter
#         total = Counter(s[left: right])
#         invalid = set()
#         for i in total:
#             if total[i] < k:
#                 invalid.add(i)
#         start = left
#         ans = 0
#         rem = set()
#         working = Counter()
#         for i in range(left, right):
#             if s[i] in invalid:
#                 ans = max(ans, self.findLS(s, k, start, i))
#                 rem = set()
#                 working = Counter()
#                 start = i+1
#             else:
#                 working[s[i]] += 1
#                 if working[s[i]] >= k:
#                     if s[i] in rem:
#                         rem.remove(s[i])
#                 else:
#                     rem.add(s[i])
            
#                 if len(rem) == 0:
#                     ans = max(ans, i-start+1)
#         return ans
    
# #         # method 1: recursive
        
# #         if len(s) < k:
# #             return 0
# #         # split string if the sum of letters are less than k
# #         for c in set(s):
# #             if s.count(c) < k:
# #                 return max(self.longestSubstring(i, k) for i in s.split(c))
# #         return len(s)
    
#         # method 2: iterative
#         stack = []
#         res = 0
        
#         stack.append(s)
        
#         while stack:
#             sub = stack.pop()
            
#             for c in set(sub):
#                 if sub.count(c) < k:
#                     stack.extend([i for i in sub.split(c)])
#                     break
#             else:
#                 res = max(res, len(sub))
#         return res
        
