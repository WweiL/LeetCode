cccclass Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res, self.target = [], target
        for i in range(1,len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
                # self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)
        return res

# dfs() parameters:
# num: remaining num string
# temp: temporally string with operators added
# cur: current result of "temp" string
# last: last multiply-level number in "temp". if next operator is "multiply", "cur" and "last" will be updated
# res: result to return

    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num)+1):
            val = num[:i]
            val_int = int(num[:i])
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], temp + "+" + val, cur+val_int, val_int, res)
                self.dfs(num[i:], temp + "-" + val, cur-val_int, -val_int, res)
                self.dfs(num[i:], temp + "*" + val, cur-last+last*val_int, last*val_int, res)
