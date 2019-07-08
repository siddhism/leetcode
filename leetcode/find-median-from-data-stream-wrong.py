class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        from collections import defaultdict
        self.count = 0
        self.median = 0
        self.nums = []
        self.counts = defaultdict(int)
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.nums.append(num)
        self.count += 1
        if num in self.counts:
            self.counts[num] += 1
        else:
            self.counts[num] = 1

    def update_median(self):
        mid = self.count / 2
        # sort by key
        counts = sorted(self.counts.items())
        total = 0
        # print 'counts ', counts, ' mid ', mid
        if self.count % 2 == 1:
            for key, count in counts:
                total += count
                if mid <= total - 1:
                    # total just became greater than mid
                    self.median = float(key)
                    break
        else:
            for key, count in counts:
                total += count
                # print 'mid ', mid, 'key ', key, ' count ', count, ' total ', total
                if mid - 1 <= total - 1:
                    # total just became greater than mid
                    a = key
                    break
            total = 0
            for key, count in counts:
                total += count
                # print 'mid ', mid, 'key ', key, ' count ', count, ' total ', total
                if mid <= total - 1:
                    # total just became greater than mid
                    b = key
                    break
            # print 'a ', a, ' b ', b
            self.median = (a + b)/2.0

    def findMedian(self):
        """
        :rtype: float
        """
        self.update_median()
        return self.median
        
# obj = MedianFinder()
# obj.addNum(6)
# print obj.findMedian()
# obj.addNum(10)
# print obj.findMedian()
# obj.addNum(2)
# print obj.findMedian()
# obj.addNum(6)
# print obj.findMedian()
# obj.addNum(5)
# print obj.findMedian()
# obj.addNum(0)
# print obj.findMedian()
# obj.addNum(6)
# print obj.findMedian()
# obj.addNum(3)
# print obj.findMedian()

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()