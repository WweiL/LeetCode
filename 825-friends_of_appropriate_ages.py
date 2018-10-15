class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        # O(n), dp
        # Use a dict to count the number of people in each age => optimized by using an array
        age_dict = [0] * 121
        age_sum = [0] * 121
        ans = 0
        for i in ages:
            age_dict[i] += 1
        for i in range(1, 121):
            age_sum[i] += age_sum[i-1] + age_dict[i] # number of people with age <= i
        #print(age_sum)
        for i in range(15, 121):
            if age_dict[i] == 0:
                continue
            min_age = i // 2 + 7
            count = age_sum[i] - age_sum[min_age]
            ans += (count-1) * age_dict[i]
        return ans

# O(nlogn), not good enough
#     def numFriendRequests(self, ages):
#         """
#         :type ages: List[int]
#         :rtype: int
#         """
#         from bisect import bisect_right
#         ages = sorted(ages)
#         n = len(ages)
#         ans = 0
#         prev = 0
#         for i in range(n-1, -1, -1):
#             if i < n-1 and ages[i] == ages[i+1]:
#                 ans += prev
#                 continue
    
#             if ages[i] < 14:
#                 break
#             else:
#                 min_age = 0.5 * ages[i] + 7
#                 min_idx = bisect_right(ages, min_age, 0, i)
#                 prev = i - min_idx
#                 ans += prev
#         return ans
