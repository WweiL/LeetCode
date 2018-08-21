# Marvelous
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        char_hash = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37,    'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u':73, 'v':79, 'w':83, 'x':89, 'y': 97, 'z': 101}
        dic = defaultdict(list)
        for s in strs:
            hash_val = 1
            for c in s:
                hash_val *= char_hash[c]
            dic[hash_val].append(s)
        return [values for values in dic.values()]

# common and not interesting
# class Solution:
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         from collections import defaultdict
#         dic = defaultdict(list)
#         for s in strs:
#             _s = "".join(sorted(s))
#             dic[_s].append(s)
                
#         return [values for values in dic.values()]
            
        
