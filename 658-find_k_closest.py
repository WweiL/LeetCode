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

class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # first, find the greatest element that is smaller than x
        n = len(arr)
        l, r = 0, n-1
        while l < r:
            mid = l + r + 1 >> 1
            if arr[mid] <= x:
                l = mid
            else:
                r = mid-1
        
        r = l + 1 if l + 1 < n else l
        m = r if arr[r] - x < x - arr[l] else l
        k -= 1
        l, r = m-1, m+1
        while k > 0:
            vl = arr[l] if l >= 0 else -float('inf')
            vr = arr[r] if r < n else float('inf')
            if x - vl <= vr - x:
                l -= 1
            else:
                r += 1
            k -= 1
        l = -1 if l < 0 else l
        r = n if r > n else r
        return arr[l+1: r]
