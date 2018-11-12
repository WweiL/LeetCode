class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        import collections
        edge = collections.defaultdict(set)
        reverse = collections.defaultdict(set)
        nodes = set()
        # build graph
        for i in range(len(words)):
            prev = "" if i == 0 else words[i-1]
            curr = words[i]
            # then build edge between curr and prev
            for c in curr:
                # self.edge[c]
                nodes.add(c)
            if i > 0:
                k = 0
                min_len = min(len(curr), len(prev))
                while(k < min_len and curr[k] == prev[k]):
                    k += 1
                if k < min_len:
                    edge[curr[k]].add(prev[k])
                    reverse[prev[k]].add(curr[k])
                    if not self.isValid(curr[k], prev[k], edge):
                        return ''
        source = [i for i in nodes if i not in reverse]
        ans = []
        while source:
            i = source.pop(0)
            for j in edge[i]:
                reverse[j].remove(i)
                if len(reverse[j])==0:
                    del reverse[j]
                    source.append(j)
            ans.append(i)
        if len(reverse) != 0:
            return ""
        return "".join(reversed(ans))
    
    def isValid(self, w1, w2, edge):
        if w1 in edge[w2] and w2 in edge[w1]:
            print(w1, edge[w1], w2, edge[w2])
            return False
        return True
