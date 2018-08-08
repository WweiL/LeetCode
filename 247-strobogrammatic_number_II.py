class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.l = n
        return self.getAll(n)
    
    def getAll(self, n):
        # BRILLIANT BASE CASE!
        if n == 0:
            return [""]
        if n == 1:
            return ["0", "1", "8"]
        
        previous = self.getAll(n-2)
        pairs = ["00", "11", "88", "69", "96"] if n != self.l else ["11", "88", "69", "96"]
        res = []
        for pair in pairs:
            for item in previous:
                res.append(pair[0] + item + pair[1])
        return res

            
# class Solution(object):
#     def findStrobogrammatic(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         self.every = ["1", "8"]
#         self.zero = ["0"]
#         self.pair = ["6", "9"]
        
#         if n == 0:
#             return []
#         elif n == 1:
#             return self.every + self.zero
#         elif n % 2 == 0:
#             l = int(n/2)
#             half_list = self.getAllListsHalf(l)
#             return self.getAllListsWhole(half_list)
#         else:
#             l = int(n/2)
#             half_list = self.getAllListsHalf(l)
#             whole_list = self.getAllListsWhole(half_list)
#             res = []
#             for num in self.every+self.zero:
#                 for item in whole_list:
#                     res.append(item[:l] + num + item[l:])
#             return res
        
#     def listMul(self, l1, l2):
#         l = []
#         for i in l1:
#             for j in l2:
#                 l.append(i+j)
#         return l
    
#     def getAllListsHalf(self, l):
#         end = self.every + self.pair
#         middle = self.every + self.pair + self.zero
#         tmp = end
#         for i in range(l-1):
#             tmp = self.listMul(middle, tmp)
#         return tmp
    
#     def getAllListsWhole(self, l):
#         for i, last_half in enumerate(l):
#             first_half = ""
#             for j in range(len(last_half)-1, -1, -1):
#                 if last_half[j] == "6":
#                     first_half += "9"
#                 elif last_half[j] == "9":
#                     first_half += "6"
#                 else:
#                     first_half += last_half[j]
#                 l[i] = first_half + last_half
#         return l
                    
