class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        count = 0
        marked = [[False] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and marked[i][j] == False:
                    count += 1
                    self.dfs((i, j), grid, marked)
        return count
                        
    def dfs(self, node, grid, marked):
        h = len(grid)
        l = len(grid[0])
        i = node[0]
        j = node[1]
        neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        for neighbor in neighbors:
            x = neighbor[0]
            y = neighbor[1]
            if 0 <= x < h and 0 <= y < l and grid[x][y] == "1" and not marked[x][y]:
                marked[x][y] = True
                self.dfs(neighbor, grid, marked)
        
