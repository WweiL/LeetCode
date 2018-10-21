class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        prereq = defaultdict(set)
        reverse = defaultdict(set)
        # if a is a prereq for b, then reverse[a] = b, prereq[b] = a
        # a -> b
        source = []
        courses = set([i for i in range(numCourses)])
        res = []
        for i in prerequisites:
            prereq[i[0]].add(i[1])
            reverse[i[1]].add(i[0])
        source = [i for i in courses if i not in prereq]
        
        while source:
            s = source.pop(0)
            for i in reverse[s]:
                prereq[i].remove(s)
                if len(prereq[i]) == 0:
                    del prereq[i]
                    source.append(i)
            res.append(s)
        if len(prereq) != 0:
            return []
        return res
            
