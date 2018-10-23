class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        from bisect import bisect_left
        from collections import deque
        first_idx = bisect_left(arr, x) - 1
        if first_idx < 0:
            first_idx = 0
        l, r = first_idx-1, first_idx+1
        ans = deque([arr[first_idx]])
        while len(ans) < k:
            left = arr[l] if l >= 0 else float('inf')
            right = arr[r] if r < len(arr) else float('inf')
            if abs(left - x) <= abs(right - x):
                ans.appendleft(left)
                l -= 1
            else:
                ans.append(right)
                r += 1
        return list(ans)
