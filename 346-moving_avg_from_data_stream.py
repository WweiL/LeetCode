from collections import deque
class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.vals = deque()
        self.size = size
        self.curr_size = 0
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.size == 0:
            return None
        
        self.curr_size += 1
        self.sum += val
        self.vals.append(val)
        if self.curr_size > self.size:
            self.sum -= self.vals.popleft()
            self.curr_size -= 1
        return self.sum / self.curr_size
            

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
