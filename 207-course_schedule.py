class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def hasCycle(s):
            if path[s] == 2:
                return True
            elif path[s] == 1:
                return False 
            path[s] = 2 # visiting
            for neighbour in forward[s]:
                if hasCycle(neighbour):
                    return True
            path[s] = 1 # visited
            return False
        
        if not prerequisites:
            return True
        forward = [[] for _ in range(numCourses)] 
        for p in prerequisites:
            forward[p[0]].append(p[1])
            
        path = [0] * numCourses
        for s in range(numCourses):
            if hasCycle(s):
                return False
        return True
