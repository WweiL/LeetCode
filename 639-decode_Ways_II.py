class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # decode[i] = decode[i+1]
        #             + decode[i+2] if s[i] in [1, 2] and s[i+1] in [1..6]
        n = len(s)
        if n == 0:
            return 0
        s = s + "@@"
        decode_i, decode_i1, decode_i2 = 1, 1, 1
        for i in range(n-1, -1, -1):
            if s[i] != '*':
                decode_i = 0 if s[i] == "0" else decode_i1
                if (s[i] == '1' and s[i+1] != "@"):
                    multiplier = 9 if s[i+1] == '*' else 1
                    decode_i += multiplier * decode_i2
                if  (s[i] == '2' and s[i+1] in ["*", "0", "1", "2", "3", "4", "5", "6"]):
                    multiplier = 6 if s[i+1] == '*' else 1
                    decode_i += decode_i2 * multiplier
            else:
                decode_i = 9 * decode_i1
                if s[i+1] == '*':
                    decode_i += 15 * decode_i2
                else:
                    if s[i+1] in ['7', '8', '9']:
                        decode_i += decode_i2
                    elif s[i+1] != '@':
                        decode_i += 2 * decode_i2
            decode_i, decode_i1, decode_i2 = 0, decode_i, decode_i1
        return decode_i1 % (10 ** 9 + 7)
