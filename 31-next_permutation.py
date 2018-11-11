cccclass Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p = n
        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                p = i-1
                break

        if p == n:
            nums.reverse()
        else:
            to_swap = float('inf')
            to_swap_idx = n-1
            for i in range(n-1, p, -1):
                if nums[i] > nums[p] and nums[i] < to_swap:
                    to_swap = nums[i]
                    to_swap_idx = i
            
            nums[to_swap_idx], nums[p] = nums[p], nums[to_swap_idx]

            # for i in range(n-1, (n+p)//2, -1):
                # nums[i], nums[n+p-i] = nums[n+p-i], nums[i]
            nums[p+1:] = reversed(nums[p+1:])

    
