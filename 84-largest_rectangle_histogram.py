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
                    
