# my sol
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        nRows, nCols = len(grid), len(grid[0])
        if nRows*nCols == 0: return 0
        distinct_islands, visited = set(), [[False]*nCols for _ in range(nRows)]
        
        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == 1 and (not visited[r][c]):
                    # no need to sort, relative positions are set since the ways of exploring neighbors are the same
                    island = self.dfs(r, c, visited, grid)
                    #ox, oy = island[0][0], island[0][1]
                    for i in range(len(island)):
                        island[i] = island[i][0] - r, island[i][1] - c
                    distinct_islands.add(tuple(island))
        return len(distinct_islands)
            
    def dfs(self, r: int, c: int, visited: List[List[bool]], grid: List[List[int]]) -> List[tuple]:
        if grid[r][c] != 1: return []
        if visited[r][c]: return []
        visited[r][c] = True
        ans = [(r, c)]
        for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if i >= 0 and j >= 0 and i < len(visited) and j < len(visited[0]):
                ans += self.dfs(i, j, visited, grid)
        #visited[r][c] = False
        return ans

    
# beautiful sol
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(rowNum: int, colNum: int, direction: str):
            if 0 <= rowNum < nRows and 0 <= colNum < nCols and grid[rowNum][colNum] == 1:
                grid[rowNum][colNum] = 0
                self.signature += direction
                dfs(rowNum - 1, colNum, 'u')
                dfs(rowNum, colNum + 1, 'r')
                dfs(rowNum + 1, colNum, 'd')
                dfs(rowNum, colNum - 1, 'l')
                self.signature += 'b'
                
        nRows = len(grid)
        nCols = len(grid[0])
        islandsSet = set()
        for idx in range(nRows):
            for jdx in range(nCols):
                if grid[idx][jdx] == 1:
                    self.signature = ''
                    dfs(idx, jdx, 'o')
                    islandsSet.add(self.signature)
        return len(islandsSet)

