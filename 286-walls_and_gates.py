class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if len(rooms) == 0:
            return
        inf = 2 ** 31 - 1
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] != 0:
                    continue
                self.bfs([(i, j, 0)], set((i, j)), rooms)

    def bfs(self, q, visited, rooms):
        m = len(rooms)
        n = len(rooms[0])
        while q:
            a, b, dis = q.pop(0)
            for x, y in self.neighbors(a, b, m, n):
                    if rooms[x][y] < 1 or (x, y) in visited:
                        continue
                    rooms[x][y] = min(rooms[x][y], dis+1)
                    q.append((x, y, dis+1))
                    visited.add((x, y))

    def neighbors(self, i, j, m, n):
        up = i-1 if i > 0 else i
        down = i+1 if i+1 < m else i
        left = j-1 if j > 0 else j
        right = j+1 if j+1 < n else j
        res = set()
        for l in [up, down]:
            res.add((l, j))
        for r in [left, right]:
            res.add((i, r))
        if (i, j) in res:
            res.remove((i, j))
        return res
