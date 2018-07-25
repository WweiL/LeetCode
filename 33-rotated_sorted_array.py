class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return -1 if nums[0] != target else 0
        else:
            pivot = self.find_pivot(0, len(nums)-1, nums)
            if pivot == -1:
                return self.bin_search(0, len(nums)-1, nums, target)
            else:
                if nums[0] == target:
                    return 0
                elif nums[0] < target:
                    return self.bin_search(0, pivot, nums, target)
                else:
                    return self.bin_search(pivot+1, len(nums)-1, nums, target)

    def find_pivot(self, low, high, nums):
        half = int((low + high)/2)
        if nums[half] > nums[half+1]:
            return half
        else: # nums[half] < nums[half+1], no duplicates
            if nums[half] > nums[high]:
                return self.find_pivot(half, high, nums)
            elif nums[half] < nums[low]:
                return self.find_pivot(low, half, nums)
            else: # in ascending order
                return -1
    
    def bin_search(self, low, high, nums, target):
        half = int((low + high)/2)
        if half == low:
            return -1 if nums[low] != target and nums[high] != target else (low if nums[low] == target else high)
        else:
            if nums[half] == target:
                return half
            elif nums[half] > target:
                return self.bin_search(low, half, nums, target)
            else:
                return self.bin_search(half, high, nums, target)
