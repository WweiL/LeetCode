class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import defaultdict
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        
        num_odd = 0
        for k, v in d.items():
            if v % 2 == 1:
                num_odd += 1
                
        return num_odd <= 1
