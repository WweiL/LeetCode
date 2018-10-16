class Solution:
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        # BFS
        height, length = len(maze), len(maze[0])
        marked = [[False] * length for _ in range(height)]
        marked[start[0]][start[1]] = True
        queue = [start]
        while queue:
            pos = queue.pop(0)
            neighbors = self.nextPos(maze, pos)
            for n in neighbors:
                if n == destination:
                    return True
                if n != pos and not marked[n[0]][n[1]]:
                    marked[n[0]][n[1]] = True
                    queue.append(n)
        return False

    def nextPos(self, maze, pos):
        height, length = len(maze), len(maze[0])
        i, j = pos[0], pos[1]
        up, down = i, i
        left, right = j, j
        while up >= 0 and maze[up][j] == 0:
            up -= 1
        while down < height and maze[down][j] == 0:
            down += 1
        while left >= 0 and maze[i][left] == 0:
            left -=1
        while right < length and maze[i][right] == 0:
            right += 1
        return [[up+1, j], [down-1, j], [i, left+1], [i, right-1]]
