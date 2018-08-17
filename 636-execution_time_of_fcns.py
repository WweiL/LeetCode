class Log:
    def __init__(self, log):
        self.id = int(log[0])
        self.status = log[2:-2]
        self.ts = int(log[-1])

class Solution:
    def exclusiveTime(self, n, logs):
        import collections
        ans = [0] * n
        stack = stack = collections.deque()
        prev_time = 0
        _logs = []
        
        for log in logs:
            _logs.append(Log(log))
      
        for log in _logs:
            time = log.ts

            if log.status == 'start':
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(log.id)
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return ans

# class Solution:
#     def exclusiveTime(self, n, logs):
#         """
#         :type n: int
#         :type logs: List[str]
#         :rtype: List[int]
#         """
#         import collections
#         ans = [0] * n
#         _logs = []
#         for log in logs:
#             _logs.append(Log(log))

#         stack = collections.deque()
#         prev_time = 0

#         i = 1
#         n = len(_logs)
#         stack.append(_logs[0])
#         while i < n:
#             log = _logs[i]
#             if stack:
#                 if log.status == 'start':
#                     ans[stack[-1].id] += log.ts - prev_time
#                     prev_time = log.ts
#                     stack.append(log)
#                     i += 1
#                     print([i.id for i in stack], "s")
#                 else:
#                     stack.pop()
#                     _id = log.id
#                     t = log.ts - prev_time + 1
#                     prev_time = log.ts
#                     while i < n-1 and log.status == 'end' and stack[-1].id == _id:
#                         stack.pop()
#                         i += 1
#                         log = _logs[i]
#                         t += log.ts - prev_time
#                         print([i.id for i in stack], "e1")
#                     print([i.id for i in stack], "e2")

#                     ans[_id] += t
#                     prev_time = log.ts + 1
#                     i += 1

#         return ans
