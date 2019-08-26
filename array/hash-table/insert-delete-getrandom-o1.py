# import time

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos = {} # store index of each value
        self.nums = []
        self.idx = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False
        self.pos[val] = idx
        self.nums.append(val)
        self.idx += 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False
        # here we want to do remove in O(1). so we need to swap last index and current index
        idx, last = self.pos[val], len(self.nums) - 1
        self.nums[idx], self.nums[last] = self.nums[last], self.nums[idx]
        # now we can pop last element from self.nums
        self.nums.pop()
        # update index in pos for the swapped element
        self.pos[self.nums[idx]] = idx
        self.pos.pop(val)
        return True        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()