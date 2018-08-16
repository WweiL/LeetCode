class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        from collections import defaultdict
        
        d = defaultdict(int)
        for i in wordDict:
            d[i] = 1
        
        n = len(s)
        mark = [False] * n
        possible_spots = []
        for i in range(n-1, -1, -1):
            if d[s[i:]] == 1:
                possible_spots.append(i)
                if i == 0: return True
        
        for i in range(n-1, -1, -1):
            for j in possible_spots:
                if i <= j and d[s[i:j]] == 1:
                    possible_spots.append(i)
                    mark[i] = True
                    break
        return mark[0]
            
