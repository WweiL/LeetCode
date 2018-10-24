class Solution:
    def __init__(self):
        self.max = 2**31
        
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        from bisect import bisect_left
        s = [i for i in str(n)]
        swapped = False
        for i in range(len(s)-1, 0, -1):
            if s[i] > s[i-1]:
                s[i:] = reversed(s[i:])
                smallest_greater = bisect_left(s[i:], chr(ord(s[i-1])+1))
                # print(smallest_greater, s[i+smallest_greater])
                s[i-1], s[i+smallest_greater] = s[i+smallest_greater], s[i-1]
                swapped = True
                break
        if not swapped:
            return -1
        ans = int("".join([i for i in s]))
        return ans if ans < self.max else -1
