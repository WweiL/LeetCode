class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        edge = defaultdict(set)
        for v1, v2 in dislikes:
            edge[v1].add(v2)
            edge[v2].add(v1)
        
        marks = [2] * (N+1)
        for i in range(1, N+1):
            if marks[i] == 2:
                if not self.can_bipartite(i, edge, 0, marks):
                    return False
        return True
        
    
    def can_bipartite(self, s, edge, curr_mark, marks):
        if marks[s] == 2:
            marks[s] = curr_mark
            for neighbor in edge[s]:
                if not self.can_bipartite(neighbor, edge, 1-curr_mark, marks):
                    return False
            return True
        elif marks[s] == curr_mark:
            return True
        else:
            return False
            
