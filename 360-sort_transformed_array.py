class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def fcn(x):
            return a * x**2 + b * x + c
        
        if a == 0:
            ans = [fcn(x) for x in nums]
            if b < 0: ans.reverse()
            return ans
        
        mid = - b / (2*a)
        
        # two pointer
        n = len(nums)
        idx = 0
        dis = float('inf')
        # find the position of the element nearest to mid, which should be the max/min value
        for i in range(n):
            d = abs(nums[i] - mid)
            if d < dis:
                idx = i
                dis = d

        ans = []
        left = right = idx
        while left >= 0 or right < n:
            if a > 0:
                leftVal = rightVal = float('inf')
            else:
                leftVal = rightVal = -float('inf')
            
            if left >= 0:
                leftVal = fcn(nums[left])
            if right < n:
                rightVal = fcn(nums[right])
            
            if a > 0:
                if leftVal < rightVal:
                    ans.append(leftVal)
                    left -= 1
                else:
                    ans.append(rightVal)
                    right += 1

            if a < 0:
                if leftVal > rightVal:
                    ans.append(leftVal)
                    left -= 1
                else:
                    ans.append(rightVal)
                    right += 1
        
        ans = ans[1:]
        if a < 0: ans.reverse()
        return ans
