from collections import defaultdict, Counter
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3: return n
        ans = 1
        lines = defaultdict(int)
        for i in range(n):
            lines.clear()
            duplicates = 0
            k = float('inf')
            for j in range(n):
                if j == i: continue
                x1, y1, x2, y2 = points[i][0], points[i][1], points[j][0], points[j][1]
                if x1 == x2:
                    if y1 == y2:
                        duplicates += 1
                    else:
                        k = float('inf')
                        lines[k] = lines.get(k, 1) + 1
                else: # x1 != x2
                    # avoid k's being too close for hash function to distinguish
                    # [[0,0],[94911151,94911150],[94911152,94911151]]
                    k = 100 * (y1 - y2) / (x1 - x2)
                    lines[k] = lines.get(k, 1) + 1
                ans = max(ans, lines.get(k, 1) + duplicates)
                    
        return ans
