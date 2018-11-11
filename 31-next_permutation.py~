class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        p = n+1
        for i in range(n, 0, -1):
            if nums[i-1] < nums[i]:
                p = i-1
                break
        
        if p == n+1:
            nums.reverse()
        else:
            to_swap = 2**32-1
            to_swap_idx = n
            for i in range(n, p, -1):
                if nums[i] > nums[p] and nums[i] < to_swap:
                    to_swap = nums[i]
                    to_swap_idx = i
            
            nums[to_swap_idx], nums[p] = nums[p], nums[to_swap_idx]

            for i in range(n, int((n+p)/2), -1):
                nums[i], nums[n+p+1-i] = nums[n+p+1-i], nums[i]

    
