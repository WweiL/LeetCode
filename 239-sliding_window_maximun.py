class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        if not nums:
            return []
        if k == 0:
            return nums
        ans = []
        q = deque()
        
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            
        ans.append(nums[q[0]])
        start = 0
        end = k
        while end < len(nums):
            if start == q[0]:
                q.popleft()
            while q and nums[end] >= nums[q[-1]]:
                q.pop()
            q.append(end)
            ans.append(nums[q[0]])
            end += 1
            start += 1
        return ans
