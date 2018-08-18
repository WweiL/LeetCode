class Solution(object):
    def canCross(self, stones):
        self.memo = set()
        target = stones[-1]
        stones = set(stones)

        res = self.bt(stones, 1, 1, target)
        return res

    def bt(self, stones, cur, speed, target):
        # check memo
        if (cur, speed) in self.memo:
            return False

        if cur==target:
            return True
        
        if cur>target or cur<0 or speed<=0 or cur not in stones:
            return False
        # dfs
        candidate = [speed-1, speed, speed+1]
        for c in candidate:
            if (cur + c) in stones:
                if self.bt(stones, cur+c, c, target):
                    return True

        self.memo.add((cur,speed))
        return False
# # my dfs, TLE
# class Solution:
#     def canCross(self, stones):
#         """
#         :type stones: List[int]
#         :rtype: bool
#         """
#         # DFS
#         n = len(stones)
#         edges = {}
#         for i in range(n):
#             for j in range(i+1, n):
#                 edges[(i, stones[j] - stones[i])] = j

#         def dfs(start, step):
#             if start == n-1:
#                 return True
#             neighbors = []
#             for s in [step-1, step, step+1]:
#                 j = edges.get((start, s), -1)
#                 if j != -1:
#                     neighbors.append((j, s))
#             if not neighbors:
#                 return False
                
#             for neighbor in neighbors:
#                 if dfs(neighbor[0], neighbor[1]):
#                     return True
#             return False
        
#         if stones[1] - stones[0] != 1:
#             return False
#         else:
#             return dfs(1, 1)
            
