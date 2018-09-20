class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if(len(chars) == 1): return 1
        pos = 0
        runner = 0
        while(runner < len(chars)):
            count = 1
            while(runner < len(chars)-1 and chars[runner] == chars[runner+1]):
                count += 1
                runner += 1
            # print(pos, runner)
            # print(chars)
            chars[pos] = chars[runner]
            runner += 1
            if count > 1 and count < 10:
                chars[pos+1] = str(count)
                pos += 2
            elif count >= 10 and count < 100:
                c = str(count)
                chars[pos+1] = c[0]
                chars[pos+2] = c[1]
                pos += 3
            elif count >= 100:
                c = str(count)
                chars[pos+1] = c[0]
                chars[pos+2] = c[1]
                chars[pos+3] = c[2]
                pos += 4
            else: # count == 1
                pos += 1
        return pos
