class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        s_dic = {}
        t_dic = {}
        for i in range(n):
            if s[i] not in s_dic:
                s_dic[s[i]] = t[i]
            else:
                if s_dic[s[i]] != t[i]:
                    return False
            if t[i] not in t_dic:
                t_dic[t[i]] = s[i]
            else:
                if t_dic[t[i]] != s[i]:
                    return False
        return True
        # Allow change order, wrong
#         from collections import defaultdict
#         def parse(s):
#             ret = defaultdict(int)
#             tmp = defaultdict(int)
#             for i in s:
#                 tmp[i] += 1
#             for _, i in tmp.items():
#                 ret[i] += 1
#             return ret
        
#         return parse(s) == parse(t)
        # do not allow order changing
            
