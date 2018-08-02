import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt = collections.Counter(tasks)
        tmax = cnt.most_common(1)[0][1]
        slots = (tmax - 1) * (n+1)
        tsum = len(tasks)
        return max(tsum, slots + sum(n == tmax for n in cnt.values()))

# class Solution:
#     def leastInterval(self, tasks, n):
#         """
#         :type tasks: List[str]
#         :type n: int
#         :rtype: int
#         """
#         if tasks == []:
#             return 0
        
#         task_feq = {}
#         most_feq = 0
#         for i in tasks:
#             task_feq[i] = task_feq.get(i, 0) + 1
#             most_feq = max(most_feq, task_feq[i])
        
#         ans = (n+1) * (most_feq-1)
#         for i in task_feq:
#             if task_feq[i] == most_feq:
#                 ans += 1
#         return max(ans, len(tasks))
        
        
