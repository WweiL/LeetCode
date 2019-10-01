from collections import deque
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # monotonally increasing array
        q = deque() # (num, idx)
        ans = [0] * len(T)
        for i in range(len(T)):
            t = T[i]
            while len(q) > 0 and t > q[-1][0]:
                num, idx = q.pop()
                ans[idx] = i - idx
            q.append((t, i))
        return ans
