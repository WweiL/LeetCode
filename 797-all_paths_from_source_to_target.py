class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        from copy import copy
        def tra(graph, i, path, ans):
            path.append(i)
            if not graph[i]:
                if i == len(graph) - 1:
                    ans.append(path)
            else:
                for j in graph[i]:
                    tra(graph, j, copy(path), ans)
        
        ans = []
        tra(graph, 0, [], ans)
        return ans
