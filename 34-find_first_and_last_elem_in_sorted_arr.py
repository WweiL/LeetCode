# class Solution:
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         if not nums:
#             return [-1, -1]
#         return self.binSearch(0, len(nums)-1, nums, target)

#     def binSearch(self, low, hi, nums, target):
#         if low == hi:
#             if nums[low] == target:
#                 return [low, hi]
#             else:
#                 return [-1, -1]
#         else:
#             mid = (low+hi) // 2
#             if nums[mid] == target:
#                 # print(low, hi)
#                 l, mid1 = self.binSearch(low, mid, nums, target)
#                 mid2, h = self.binSearch(mid+1, hi, nums, target)
#                 ans = [-1, -1]
#                 for i in sorted([l, mid1, mid2, h]):
#                     if i != -1:
#                         ans[0] = i
#                         break
#                 for i in sorted([l, mid1, mid2, h], reverse = True):
#                     if i != -1:
#                         ans[1] = i
#                         break
#                 return ans
#             elif nums[mid] < target:
#                 return self.binSearch(mid+1, hi, nums, target)
#             else:
#                 return self.binSearch(low, mid, nums, target)

# Should be a TLE
# WHY NOT!!! EVEN FASTER?????
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        return self.binSearch(0, len(nums)-1, nums, target)

    def binSearch(self, low, hi, nums, target):
        if low == hi:
            if nums[low] == target:
                return [low, hi]
            else:
                return [-1, -1]
        else:
            mid = (low+hi) // 2
            if nums[mid] == target:
                ans = []
                curr = mid
                while curr >= 0 and nums[curr] == target:
                    curr -= 1
                ans.append(curr+1)
                curr = mid
                while curr < len(nums) and nums[curr] == target:
                    curr += 1
                ans.append(curr-1)
                return ans
            elif nums[mid] < target:
                return self.binSearch(mid+1, hi, nums, target)
            else:
                return self.binSearch(low, mid, nums, target)
