class Solution:
    def __init__(self):
        self.unit = ['', ' Thousand', ' Million', ' Billion']
        self.ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        self.tys  = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        self.teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return 'Zero'
        ret = ''
        for i, v in enumerate([(num // (1000**n)) % 1000 for n in range(4)]):
            # separate the number evey three digit
            if v: # crucial here! list is [0, 1, 0, 0] if num is 1000
                ret = self.parseThree(v, self.unit[i]) + ret
        return ret[1:]

    def parseThree(self, s, unit):
        # return eng exp of every three digits, a space is reserved at the beginning. e.g. ' Two Hundred Fourteen Thousand'
        ret = ''
        first = s // 100
        second = (s % 100) // 10
        third = (s % 10)
        if first != 0:
            ret += ' ' + self.ones[first] + ' Hundred'
        if second != 0:
            if second == 1:
                ret += ' ' + self.teens[third]
                third = 0
            else:
                ret += ' ' + self.tys[second]
        if third != 0:
            ret += ' ' + self.ones[third]
        return ret + unit    
