class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.count = 0
        self.capacity = capacity
        self.cache = {}
        self.lru = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        data = self.cache.get(key)
        if not data:
            return -1
        self.update_lru(key)
        return data
    
    def update_lru(self, key):
        # remove it if it already exists
        self.lru.remove(key)
        self.lru.append(key)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if not key or not value:
            return None

        if key in cache:
            # case when we don't need to readjust capacity
            # just use the same key to update value
            self.lru.remove(key)
        elif len(self.cache) == self.capacity:
            # need to pop least recently used item
            item = self.lru.pop(0)
            self.cache.pop(item)
        # put the item in cache
        self.cache[key] = value
        # update it in lru
        self.lru.append(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)