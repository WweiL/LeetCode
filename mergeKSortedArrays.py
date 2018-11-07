class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        # (val, index)
        import heapq
        n = len(arrays)
        heap = [(v[0], i) for i, v in enumerate(arrays) if v]
        heapq.heapify(heap)
        indicies = [0] * n
        lens = [len(i) for i in arrays]
        ans = []
        while heap:
            minVal, idx = heapq.heappop(heap)
            ans.append(minVal)
            if indicies[idx]+1 < lens[idx]:
                indicies[idx] += 1
                heapq.heappush(heap, (arrays[idx][indicies[idx]], idx))
        return ans
            
