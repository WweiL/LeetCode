# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        for i in range(n):
            if knows(c, i):
                c = i
                
        for i in range(c):
            if knows(c, i):
                return -1
        
        # check if c is a single component
        for i in range(0, c):
            if not knows(i, c):
                return -1
        for i in range(c+1, n):
            if not knows(i, c):
                return -1
        return c
        
# # O(n^2), TLE
# class Solution(object):
#     def findCelebrity(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         knows_dict = {}
#         for i in range(n):
#             for j in range(n):
#                 if j == i:
#                     continue
#                 else:
#                     knows_dict[(i, j)] = knows(i, j)
#                     knows_dict[(j, i)] = knows(j, i)

#         for i in range(n):
#             is_celebrity = True
#             for j in range(n):
#                 if j == i:
#                     continue
#                 elif knows_dict[(i, j)] == False and knows_dict[(j, i)] == True:
#                     continue
#                 else:
#                     is_celebrity = False
#                     break
#             if is_celebrity:
#                 return i
            
#         return -1
                    
