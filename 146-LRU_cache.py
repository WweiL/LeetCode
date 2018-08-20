from collections import deque
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.last_time_dic = {}
        self.used_size = 0
        self.last_time = 0
        self.lru = deque()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = self.cache.get(key, -1)
        if value != -1:
            self.lru.append((key, self.last_time))
            self.last_time_dic[key] = self.last_time
            self.last_time += 1
        return value
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        
        if self.cache.get(key, -1) != -1: # updating an existing value
            pass
        else: # inserting into a new value
            if self.used_size < self.capacity:
                self.used_size += 1
            else:
                lru, lru_time = self.lru.popleft()
                while self.last_time_dic[lru] > lru_time:
                    lru, lru_time = self.lru.popleft()
                self.cache[lru] = -1
        self.last_time_dic[key] = self.last_time
        self.lru.append((key, self.last_time))
        self.last_time += 1
        self.cache[key] = value
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
