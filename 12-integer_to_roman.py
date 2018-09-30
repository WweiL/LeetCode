class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #d = {1: I, 5: V, 10: X, 50: L, 100: C, 500: D, 1000: M}
        #l = [1000, 500, 100, 50, 10, 5, 1]
        ans = ""
        while(num != 0):
            if num // 1000 > 0:
                ans += (num//1000) * "M"
                num %= 1000
            elif num // 500 > 0:
                if num >= 900 and num - 900 < 100:
                    ans += "CM"
                    num -= 900
                else:
                    ans += (num//500) * "D"
                    num %= 500
            elif num // 100 > 0:
                if num >= 400 and num - 400 < 100:
                    ans += "CD"
                    num -= 400
                else:
                    ans += (num//100) * "C"
                    num %= 100
            elif num // 50 > 0:
                if num >= 90 and num - 90 < 10:
                    ans += "XC"
                    num -= 90
                else:
                    ans += (num//50) * "L"
                    num %= 50
            elif num // 10 > 0:
                if num >= 40 and num - 40 < 10:
                    ans += "XL"
                    num -= 40
                else:
                    ans += (num//10) * "X"
                    num %= 10
            elif num // 5 > 0:
                if num == 9:
                    ans += "IX"
                    num -= 9
                else:
                    ans += (num//5) * "V"
                    num %= 5
            else:
                if num == 4:
                    ans += "IV"
                    num -= 4
                else:
                    ans += num * "I"
                    num %= 1
        return ans
