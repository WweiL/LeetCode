def search(arr, target):
    # binary search with duplicated values and non-existing target, find the first value smaller than or equal to target
    # return index and value
    # [1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10] 2.5
    # [2, 2, 2, 2,2,2 ] 2.5
    # [1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10] 12.5
    l = 0
    r = len(arr)-1
    while l < r:
        m = l + (r-l) // 2
        if arr[m] < target:
            l = m + 1
        elif arr[m] >= target:
            r = m
    #print(arr[l])
    return arr[l]
#     n = len(arr)
#     if target > arr[-1]:
#         return n-1, arr[n-1]
#     if target < arr[0]:
#         return 0, arr[0]
#     return helper(arr, target, 0, len(arr)-1)
#
# def helper(arr, target, lo, hi):
#     mid = (lo+hi) // 2
#     # [low, mid, hi] -> [lo, mid], [mid, hi]  b => lo == hi - 1 (or mid == lo) base case! => choose in [a, b] => can choose the nearst value(bigger or smaller), not necessatily the smaller
#     #                -> [lo, mid], [mid+1, hi] => lo == hi base case!
#     if mid == lo:
#         if target >= arr[mid]:
#             ret = mid
#             val = arr[mid]
#         else: #less than arr[mid]
#             ret = lo
#             val = arr[lo]
#         while ret > 0 and arr[ret-1] == val:
#             ret -= 1
#         return ret, arr[ret]
#     else:
#         if target <= arr[mid]:
#             return helper(arr, target, lo, mid)
#         else:
#             return helper(arr, target, mid, hi)
if __name__ == '__main__':
    search([1, 2, 3, 4, 5, 10], 9)
