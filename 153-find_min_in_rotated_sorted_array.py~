class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        def binsearch(nums, lo, hi):
            mid = (lo+hi) // 2
            if(mid == 0 or mid == len(nums)-1):
                return min(nums[mid], nums[lo], nums[hi])
            else:
                if(nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]):
                    return nums[mid]
                elif(nums[mid] < nums[hi]):
                    return binsearch(nums, lo, mid)
                else:
                    return binsearch(nums, mid+1, hi)
        return binsearch(nums, 0, len(nums)-1)
