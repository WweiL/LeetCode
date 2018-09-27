class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]
        ans = [0] * (num+1)
        ans[1] = 1
        mul = 2
        tmp = 0
        for i in range(2, num+1):
            ans[i] = ans[i-mul] + 1
            tmp += 1
            if(tmp == mul):
                tmp = 0
                mul *= 2
        return ans
