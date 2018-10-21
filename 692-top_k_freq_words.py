class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter
        import heapq
        d = Counter(words)
        ret = [(-count, word) for word, count in d.items()]
        heapq.heapify(ret)
        return [heapq.heappop(ret)[1] for _ in range(k)]
