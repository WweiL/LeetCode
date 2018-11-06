class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # if A[i] <= A[i-1] or B[i] <= B[i-1] ==> must swap
        # else ==> either swap or not
        # swap[i] the min number of swaps we need at pos i if we do make a swap 
        # no_swap[i] the min number of swap we need at pos i if we do not make a swap
        n = len(A)
        swap, no_swap = [float('inf')] * n, [float('inf')] * n 
        swap, no_swap = 1, 0
        for i in range(1, n):
            swap_prev = swap
            no_swap_prev = no_swap
            if (A[i-1] < A[i] and B[i-1] < B[i]) and (A[i-1] < B[i] and B[i-1] < A[i]):
                swap = 1 + min(swap_prev, no_swap_prev)
                no_swap = min(swap_prev, no_swap_prev)
            else:
                if A[i-1] < A[i] and B[i-1] < B[i]:
                    swap = 1 + swap_prev
                    no_swap = no_swap_prev
                else:
                    swap = 1 + no_swap_prev
                    no_swap = swap_prev
        return min(swap, no_swap)
