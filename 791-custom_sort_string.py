# class Solution:
#     def customSortString(self, S, T):
#         """
#         :type S: str
#         :type T: str
#         :rtype: str
#         """
#         retStr = ""
#         for letter in S:
#             if letter in T:
#                 count = T.count(letter)
#                 T = T.replace(letter, "")
#                 retStr += count*letter
        
#         return retStr + T
# quick sort with custom > function, VERY SLOW!
class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        g = {}
        for i in range(len(S)):
            g[S[i]] = i
        return self.qsort(g, T)

    def qsort(self, g, T):
        if T == "":
            return ""
        pivot = T[0]
        pivot_count = len([t for t in T if t == pivot])

        right = "".join([t for t in T if self.greater(g, t, pivot)])
        left = "".join([t for t in T if self.greater(g, pivot, t)])
        # print("pivot: ", pivot)
        # print("left: ", left)
        # print("right: ", right)
        return self.qsort(g, left) + pivot * pivot_count + self.qsort(g, right)
    
    def greater(self, g, i, j):
        a = g.get(i, 0)
        b = g.get(j, 0)
        if a != b:
            return a > b
        else: # i != j or i == j:
            return i > j
        
        
        
