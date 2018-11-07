class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = collections.deque()
        # [max -> min]
        if not nums or k == 0:
            return []
        nums.append(-float('inf'))
        l, r, n = 0, 0, len(nums)
        ans = []
        while r < n:
            if r - l < k:
                while q and nums[q[-1]] <= nums[r]:
                    q.pop()
                q.append(r)
                r += 1
            else:
                ans.append(nums[q[0]])
                while q and nums[q[-1]] <= nums[r]:
                    q.pop()
                q.append(r)
                if q[0] == l:
                    q.popleft()
                l, r = l+1, r+1
        return ans
