class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        ret = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ret += self.perimeter(grid, i, j)
        return ret
        
    def perimeter(self, grid, i, j):
        ans = 4
        updown = [-1, 0, 1, 0]
        leftright = [0, -1, 0, 1]
        m = len(grid)
        n = len(grid[0])
        for k in range(4):
            x, y = i+updown[k], j+leftright[k]
            if x < 0 or x == m or y < 0 or y == n:
                continue
            elif grid[x][y] == 1:
                ans -= 1
        return ans
