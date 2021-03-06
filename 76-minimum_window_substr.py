# class Solution:
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         dt = collections.Counter(t)
#         ds = collections.defaultdict(int)
#         rem = len(dt)
#         start = 0
        
#         res = ''
#         for end in range(len(s)):
#             ds[s[end]] += 1
#             if ds[s[end]] == dt[s[end]]:
#                 rem -= 1
#             while start <= end and ds[s[start]] > dt[s[start]]:
#                 ds[s[start]] -= 1
#                 start += 1
#             if rem == 0 and (res == '' or end - start < len(res)):
#                 res = s[start: end+1]
#         return res
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        start = end = 0
        counter = len(t)
        begin = 0
        l = float('inf')
        dt = collections.Counter(t)
        
        # "ADOBECODEBANC"
        while end < len(s):
            # move forward the end pointer, set dt[s[end]] -= 1 to mark the visit
            if dt[s[end]] > 0:
                counter -= 1
            dt[s[end]] -= 1
            end += 1
            
            while counter == 0:
                # move forward the start pointer, set dt[s[start]] += 1 to erase the mark
                if end-start < l:
                    l = end-start
                    begin = start
                if dt[s[start]] == 0:
                    counter += 1
                dt[s[start]] += 1
                start += 1

        return "" if l == float('inf') else s[begin:begin+l]
        
