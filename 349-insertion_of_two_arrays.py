class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)
        count1 = collections.Counter(nums1)
        ans = []
        for i in nums2:
            if count1[i] > 0:
                ans.append(i)
                count1[i] = 0
        return ans
