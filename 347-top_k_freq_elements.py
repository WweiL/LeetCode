class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        num_freq = defaultdict(int)
        freq_num = defaultdict(list)
        for i in nums:
            num_freq[i] += 1
            freq_num[num_freq[i]].append(i)
        
        
        ans = defaultdict(int)
        for i in range(len(nums), -1, -1):
            if k <= 0: break
            if i in freq_num:
                for j in freq_num[i]:
                    ans[j] += 1
                    k -= 1 if ans[j] == 1 else 0
                        
        return [a for a in ans.keys()]
