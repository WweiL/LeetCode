class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        left = self.getLeft(heights)
        right = self.getRight(heights)
        max_area = 0
        for i in range(len(heights)):
            area = (right[i] - left[i] + 1) * heights[i]
            max_area = max(max_area, area)
        return max_area
    
    def getRight(self, heights):
        n = len(heights)
        s = [n-1]
        right = [n-1] * n
        for i in range(n - 2, -1, -1):
            if heights[i] > heights[s[-1]]:
                right[i] = i
            else:
                while(s and heights[i] <= heights[s[-1]]):
                    right[i] = right[s.pop()]
            s.append(i)
        return right
    
    def getLeft(self, heights):
        s = [0]
        n = len(heights)
        left = [0] * n
        for i in range(1, n):
            if heights[i] > heights[s[-1]]:
                left[i] = i
            else:
                while(s and heights[i] <= heights[s[-1]]):
                    left[i] = left[s.pop()]
            s.append(i)
        return left
                    

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = collections.deque()
        heights.append(-1)
        i, n = 0, len(heights)
        ans = 0
        while i < n:
            if len(stack) == 0 or heights[stack[-1]] < heights[i]: # increasing
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                ans = max(ans, (i-stack[-1]-1) * heights[top]) if stack else max(ans, heights[top] * i) # empty when heights[top] is the minimum so far, so area is i * heights[top]
        # for i in range(n):
            # while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
            #     top = stack.pop()
            #     ans = max(ans, (i-stack[-1]-1) * heights[top]) if stack else max(ans, heights[top] * i)
            # stack.append(i)
        return ans
