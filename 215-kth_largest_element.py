class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.findKthSmallest(nums, len(nums) - k + 1)
    
    def findKthSmallest(self, nums, k):
        n = len(nums)
        p = int(n/2)
        left = [x for x in nums if x < nums[p]]
        middle = [x for x in nums if x == nums[p]]
        p_idx_min = len(left) + 1
        p_idx_max = len(left) + len(middle)
        if p_idx_min <= k <= p_idx_max:
            return nums[p]
        elif p_idx_max < k:
            right = [x for x in nums if x > nums[p]]
            k = k-p_idx_max
            return self.findKthSmallest(right, k)
        else: # p_idx > k
            return self.findKthSmallest(left, k)
