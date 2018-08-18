class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        def str_to_num(num):
            i = 1
            d = {'0': 0,
                 '1': 1,
                 '2': 2,
                 '3': 3,
                 '4': 4,
                 '5': 5,
                 '6': 6,
                 '7': 7,
                 '8': 8,
                 '9': 9,
                }
            ans = 0
            for n in range(len(num)-1, -1, -1):
                ans += d[num[n]]*i
                i *= 10
            return ans
        
        def num_to_str(num):
            d = {0: '0',
                 1: '1',
                 2: '2',
                 3: '3',
                 4: '4',
                 5: '5',
                 6: '6',
                 7: '7',
                 8: '8',
                 9: '9',
                }
            ans = ''
            while num:
                n = num % 10
                ans = d[n] + ans
                num = num // 10
            return ans
        if num1 == '0' and num2 == '0':
            return '0'
        return num_to_str(str_to_num(num1) + str_to_num(num2))
