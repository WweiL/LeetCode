class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dt = {}
        start = end = 0
        counter = len(t)
        begin = 0
        l = float('inf')
        for i in s+t:
            dt[i] = 0
        
        for i in t:
            dt[i] += 1
        
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
        
