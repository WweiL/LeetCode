class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        edge = self.build_graph(equations, values)
            
        ans = []
        for query in queries:
            divident = query[0]
            divisor = query[1]
            if divident not in edge or divisor not in edge:
                ans.append(-1.0)
            else:
                ans.append(self.divide(divident, divisor, edge))
        return ans
    
    # def dfs(self, i, edge, quotient, vals):
    #     for j in edge[i]:
    #         v = quotient[j][i]
    #         unit = vals[i][1]
    #         factor = vals[i][0]
    #         vals[j] = (v*factor, unit)
    #         self.dfs(j, edge, quotient, vals)
    
    def divide(self, divident, divisor, edge):
        from collections import deque
        queue = deque()
        queue.append((divident, 1.0))
        marked = set()
        while queue:
            d, val = queue.popleft()
            if d == divisor:
                return val
            for div in edge[d].keys():
                if div not in marked:
                    factor = edge[d][div]
                    marked.add(div)
                    queue.append((div, factor*val))
        return -1
                
            

    def build_graph(self, equations, values):
        from collections import defaultdict
        edge = defaultdict(dict)
        for i in range(len(equations)):
            divident = equations[i][0]
            divisor = equations[i][1]
            edge[divisor][divident] = 1/values[i]
            edge[divident][divisor] = values[i]
        return edge
    
#     def build_graph(self, equations, values):
#         from collections import defaultdict
#         n = len(equations)
#         edge = defaultdict(set)
#         tmp = defaultdict(set)
#         quotient = defaultdict(dict)
#         sink = set()
#         for i in range(n):
#             divident = equations[i][0]
#             divisor = equations[i][1]
#             edge[divisor].add(divident)
#             tmp[divident].add(divisor)
#             quotient[divident][divisor] = values[i]
#             quotient[divisor][divident] = 1 / values[i]
#             sink.add(divisor)
#         s = set()
#         for i in sink:
#             if len(tmp[i]) == 0:
#                 s.add(i)
#         return edge, quotient, s
        
