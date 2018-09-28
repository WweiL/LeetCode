class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        line = defaultdict(int)
        max_blank = 0
        for l in wall:
            length = 0
            for i in l[:-1]:
                length += i
                line[length] += 1
                max_blank = max(max_blank, line[length])
                
        return len(wall) - max_blank
