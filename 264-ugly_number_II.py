# Fancier
class Solution:
    ugly = sorted([2**a * 3**b * 5**c for a in range(32) for b in range(20) for c in range(14)])
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return Solution.ugly[n - 1] if n > 0 else None

# using min-heap
class Solution:
    import heapq
    book=[1]
    i2,i3,i5=0,0,0
    while len(book)<1961:
        tmp=min(2*book[i2],3*book[i3],5*book[i5])
        if tmp==2*book[i2]:
            i2+=1
        if tmp==3*book[i3]:
            i3+=1
        if tmp==5*book[i5]:
            i5+=1
        book.append(tmp)
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.book[n-1]
                    
                

# Faster && saves more space, using pointer
class Solution:
    def nthUglyNumber(self, n):
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]

# Most easy to be thought of
class Solution:
    ugly = [1]
    u2 = [2]
    u3 = [3]
    u5 = [5]
    for i in range(1, 1961):
        chosen_one = min(u2[0], u3[0], u5[0])
        if chosen_one == u2[0]:
            u2.pop(0)
        if chosen_one == u3[0]:
            u3.pop(0)
        if chosen_one == u5[0]:
            u5.pop(0)
        u2.append(chosen_one * 2)
        u3.append(chosen_one * 3)
        u5.append(chosen_one * 5)
        ugly.append(chosen_one)
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
            
        return self.ugly[n-1]
