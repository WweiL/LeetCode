class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map1 = {}
        for i in nums1+nums2:
            map1[i] = 0
            
        for i in nums1:
            map1[i] += 1
            
        ans_tmp = []
        ans = []
        ans_map = {}
        
        for i in nums2:
            if not map1[i] == 0:
                ans_tmp.append(i)
        
        # eliminate duplication
        # built-in fcn, faster
        return list(set(ans_tmp))
        
        # implement by hand
#         for i in ans_tmp:
#             ans_map[i] = ans_map.get(i, 0) + 1
        
#         for i in ans_map.keys():
#             ans.append(i)
        
#         return ans
