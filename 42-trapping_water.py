# # more easy to be thought of stack:
import collections
class Solution:
    def trap(self, height):
        stack = collections.deque()
        index = 0
        water = 0
        while index < len(height):
            # decreasing order, find bottom
            if len(stack) == 0 or height[index] <= height[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                bottom = stack.pop()
                if len(stack) != 0:
                    # add horizontally, one row
                    water += (min(height[stack[-1]], height[index]) - height[bottom]) * (index - stack[-1] - 1)
        return water
# fancy two pointer
# class Solution:
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         if len(height) in [0, 1]:
#             return 0
#         left = 0
#         right = len(height) - 1
#         maxLeft = 0
#         maxRight = 0
#         volume = 0
#         # accumulate water one bar by one bar
#         while left < right:
#             if height[left] <= height[right]:
#                 if height[left] >= maxLeft: maxLeft = height[left]
#                 # since height[left] <= height[right], volume of maxLeft - height[left] will certainly be held by the wall on position right, even if this may not be the real case(the wall could be closer to left)
#                 else: volume += maxLeft - height[left]
#                 left += 1
#             else:
#                 if height[right] >= maxRight: maxRight = height[right]
#                 else: volume += maxRight - height[right]
#                 right -= 1
#         return volume
                    
# TOO CUMBERSOME!
# class Solution:
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         if len(height) in [0, 1]:
#             return 0
#         # Get interval
#         max_h_pair = [0, 0] # float('inf')
#         i = 0
#         stack = []
#         while i < len(height) - 1:
#             if height[i] < height[i+1]:
#                 i += 1
#                 continue
#             else: # height[i] >= height[i+1]
#                 # if i >= len(height)-1:
#                 #     break
#                 # j = i+1
#                 # print("a")
#                 # while j < len(height)-1 and height[j] < height[j+1]:
#                 #     j += 1
#                 j = self.findNextWall(height, i)
#                 # i is the left hightest and j is the right highest in interval [i, j]
#                 print(i, j)
#                 print(stack)
#                 h_tmp = max(height[i], height[j])
#                 idx = j if h_tmp == height[j] else height[i]
#                 k = i
#                 if h_tmp > min(max_h_pair):
#                     while stack != [] and max(height[stack[-1][1]], height[stack[-1][0]]) < h_tmp:
#                         if height[stack[-1][0]] >= height[stack[-1][1]]:
#                             k = stack[-1][0]
#                         else:
#                             k = stack[-1][1]
#                         stack.pop()
#                 max_h_pair = [height[k], h_tmp]
#                 stack.append((k, idx))
#                 max_h = h_tmp
#                 i = j
        
        
#     def findNextWall(self, height, i):
#         j = i+1
#         while j < len(height)-1 and height[j] >= height[j+1]:
#             j += 1
#         while j < len(height)-1 and height[j] <= height[j+1]:
#             j += 1
#         return j
