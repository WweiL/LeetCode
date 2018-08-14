class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low = 0
        hi = len(height) - 1
        area = 0
        while low < hi:
            h = min(height[low], height[hi])
            area = max(area, (hi-low)*h)
            while height[low] <= h and low < hi:
                low += 1
            while height[hi] <= h and low < hi:
                hi -= 1
        return area
