class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # three pointers
        zero, one = 0, 0
        for two in range(len(nums)):
            n = nums[two]
            nums[two] = 2
            if n <= 1:
                nums[one] = 1
                one += 1
            if n == 0:
                nums[zero] = 0
                zero += 1
# void sortColors(int A[], int n) {
#     int j = 0, k = n-1;
#     for (int i=0; i <= k; i++) {
#         if (A[i] == 0)
#             swap(A[i], A[j++]);
#         else if (A[i] == 2)
#             swap(A[i--], A[k--]);
#     }
# }
