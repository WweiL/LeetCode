class BinaryIndexTree():
    def __init__(self, array):
        self.sums = [0] * (len(array) + 1)
        for i in range(1, len(array) + 1):
            self.update(i, array[i-1])

    @classmethod
    def zeroInit(cls, n):
        return cls([0] * n)

    def lowbit(self, x):
        return x & -x

    def update(self, idx, val):
        while idx < len(self.sums):
            self.sums[idx] += val
            idx += self.lowbit(idx)

    def query(self, idx):
        ret = 0
        while idx > 0:
            ret += self.sums[idx]
            idx -= self.lowbit(idx)
        return ret
