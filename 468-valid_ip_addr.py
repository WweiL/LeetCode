class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        
        def isValid(s):
            return 'a' <= s <= 'f' or 'A' <= s <= 'F' or '0' <= s <= '9'
        
        def hasLeadingZero(num):
            # len(num) must in [1, 2, 3]
            if num[0] != '0':
                return False
            elif num == '0':
                return False
            else: # # num[0] is '0' and len(num) > 1
                return True

        def isIPv4(s):
            for i in s:
                if (not i.isdigit()) and i != '.':
                    return False
            
            _s = s.split('.')
            if len(_s) != 4:
                return False
            
            for num in s.split("."):
                n = len(num)
                if n == 0 or n > 3:
                    return False
                v = int(num)
                if v > 255 or v < 0:
                    return False
                elif hasLeadingZero(num):
                    return False
            return True
            
        def isIPv6(s):
            _s = s.split(':')
            if len(_s) != 8:
                return False

            for i in _s:
                if len(i) > 4 or len(i) == 0:
                    return False
                for j in i:
                    if not isValid(j):
                        return False
            return True
        
        if isIPv4(IP):
            return 'IPv4'
        elif isIPv6(IP):
            return 'IPv6'
        else:
            return 'Neither'
