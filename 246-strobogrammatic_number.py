class Solution():
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        pair = {'6': '9', '1': '1', '8': '8', '9': '6', '0': '0'}
        i = 0
        j = len(num)-1
        while i < j:
            if num[i] == pair.get(num[j], '#'):
                i += 1
                j -= 1
            else:
                return False
        if i == j:
            return num[i] in ['0', '1', '8']
        return True
            
