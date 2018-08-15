class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        marked = [2 for i in range(len(graph))]
        for i in range(len(graph)):
            if marked[i] == 2:
                if not self.mark_dfs(graph, marked, 0, i):
                    return False
        return True
    
    def mark_dfs(self, graph, marked, mark, i):
        if marked[i] == 2:
            marked[i] = mark
            for neighbor in graph[i]:
                if not self.mark_dfs(graph, marked, 1-mark, neighbor):
                    return False
            return True
        elif marked[i] != mark:
            return False
        else:
            return True
