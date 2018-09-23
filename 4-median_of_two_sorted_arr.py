class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def findNumPicked(nums1, nums2, left, right, k):
            mid1 = (left + right) // 2
            mid2 = k - mid1
            if left == right:
                return mid1
            elif(nums1[mid1] > nums2[mid2-1]):
                return findNumPicked(nums1, nums2, left, mid1, k)
            else:
                return findNumPicked(nums1, nums2, mid1+1, right, k)
                
        m = len(nums1)
        n = len(nums2)
        if(n < m): return self.findMedianSortedArrays(nums2, nums1)
        left = 0
        right = m
        # k is the number of items is the first half of the combined array(including the middle if array length is odd)
        k = (m+n+1) // 2
        # m1 be the number of elements chosen in nums1, n1 be the number of elements chosen in nums2
        m1 = findNumPicked(nums1, nums2, left, right, k)
        n1 = k - m1
        num1 = nums1[m1-1] if m1 > 0 else -float('inf')
        num2 = nums2[n1-1] if n1 > 0 else -float('inf')
        num1a = nums1[m1] if m1 < m else float('inf')
        num2a = nums2[n1] if n1 < n else float('inf')
        if((m+n) % 2 == 1):
            return max(num1, num2)
        else:
            first = max(num1, num2)
            second = min(num1a, num2a)
            return (first+second) / 2
