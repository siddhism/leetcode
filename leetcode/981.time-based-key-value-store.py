#
# @lc app=leetcode id=981 lang=python
#
# [981] Time Based Key-Value Store
#



class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.cache = defaultdict(list)
        self.cache_values = defaultdict(list)
        self.cache_timestamps = defaultdict(list)
        
    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1
        if arr and target < arr[0]:
            return -1
        # print (arr, low, high, target)
        while low <= high:
            mid = (low + high) / 2
            if arr[mid] == target:
                return mid
            if arr[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        # if element is not matched, we are just + 1 index ahead of it
        return high


    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.cache[key].append((value, timestamp))
        self.cache_values[key].append(value)
        self.cache_timestamps[key].append(timestamp)
        
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if not self.cache.get(key):
            return ""
        timestamps = self.cache_timestamps[key]
        index = self.binary_search(timestamps, timestamp)
        # print 'key ', timestamp, ' ts ', timestamps, ' index returned ', index
        if index  == -1:
            return ""
        # otherwise value is found
        return self.cache_values[key][index]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

