class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nextGt = {}
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            num = nums2[i]
            if len(stack) == 0 or stack[-1] < num:
                while stack and stack[-1] < num:
                    stack.pop()
                nextGt[num] = stack[-1] if len(stack) > 0 else -1
                stack.append(num)
            else:
                nextGt[num] = stack[-1]
                stack.append(num)
        ans = nums1
        for i in range(len(ans)):
            ans[i] = nextGt[ans[i]]
        return ans
