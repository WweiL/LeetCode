class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = a if len(a) < len(b) else b
        l = b if s == a else a
        
        while (len(s) < len(l)):
            s = "0" + s

        res = ""
        carry_in = "0"
        for i in range(len(l)-1, -1, -1):
            (temp, carry_out) = self.add(i, carry_in, s, l)
            res = temp + res
            carry_in = carry_out
        
        if carry_in == "1":
            res = "1" + res
        return res
            
    def add(self, i, carry_in, s, l):
        res = int(s[i]) + int(l[i]) + int(carry_in)
        if res >= 2:
            res = res % 2
            carry_out = 1
        else:
            carry_out = 0
        return (str(res), str(carry_out))
        
