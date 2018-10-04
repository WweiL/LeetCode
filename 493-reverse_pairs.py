class Solution:
    # def reversePairs(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     return self.mergeAndCount(nums, 0, len(nums)-1)
    
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        # faster version using built in sort
        def mergesort(lo, hi):
            m = (lo + hi) // 2
            if m == lo: return 0
            count = mergesort(lo, m) + mergesort(m, hi)
            j = m
            for i in range(lo, m):
                while j < hi and nums[i] > 2 * nums[j]: j += 1
                count += j - m
            nums[lo:hi] = sorted(nums[lo:hi])
            return count
        return mergesort(0, len(nums))
        
    # slower version with self implemented merge sort
    def mergeAndCount(self, nums, l, r):
        if l >= r:
            return 0
        mid = (l+r) // 2
        res = self.mergeAndCount(nums, l, mid) + self.mergeAndCount(nums, mid+1, r)
        merged = []
        p = mid+1
        i = l
        j = mid+1
        cnt = 0
        while(i <= mid):
            while(p <= r and nums[i] > 2*nums[p]):
                cnt += 1
                p += 1
            res += cnt

            while(j <= r and nums[i] > nums[j]):
                merged.append(nums[j])
                j += 1
            merged.append(nums[i])
            i += 1
            
        while j <= r:
            merged.append(nums[j])
            j += 1
        
        k = 0
        while l <= r:
            nums[l] = merged[k]
            k += 1
            l += 1
        return res
  
