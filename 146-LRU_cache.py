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

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lru = {}

    def get(self, key: int) -> int:
        node = self.lru.get(key, None)
        if not node:
            return -1
        self._remove(key)
        self._add(key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        # update existing key
        if self.lru.get(key, None):
            self._remove(key)
        # remove LRU
        if len(self.lru) == self.capacity:
            self._remove(self.head.next.key)
        self._add(key, value)
            
    def _add(self, key: int, value: int) -> None:
        node = Node(key, value)
        node.next = self.tail
        node.prev = self.tail.prev
        node.prev.next = node
        node.next.prev = node
        self.lru[key] = node

    def _remove(self, key: int) -> None:
        node = self.lru[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        del self.lru[key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
