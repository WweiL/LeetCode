class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        shorter = nums1 if len(nums1) < len(nums2) else nums2
        longer = nums2 if len(nums1) < len(nums2) else nums1
        d_s = {}
        for i in shorter+longer:
            d_s[i] = 0
        for i in shorter:
            d_s[i] += 1
            
        ans = []
        for i in longer:
            if d_s[i] > 0:
                ans.append(i)
                d_s[i] -= 1
        return ans
