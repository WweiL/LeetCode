import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.idx_item = {}
        self.item_idx = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.item_idx: return False
        idx = len(self.idx_item)
        self.idx_item[idx] = val
        self.item_idx[val] = idx
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.item_idx: return False
        idx = self.item_idx[val]
        last_idx = len(self.item_idx) - 1
        if idx == last_idx:
            del self.item_idx[val]
            del self.idx_item[idx]
            return True
        # swap the last idx with the deleted one
        last_val = self.idx_item[last_idx]
        del self.item_idx[val]
        del self.item_idx[last_val]
        del self.idx_item[last_idx]
        self.idx_item[idx] = last_val
        self.item_idx[last_val] = idx
        return True
      

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, len(self.idx_item)-1)
        return self.idx_item[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
