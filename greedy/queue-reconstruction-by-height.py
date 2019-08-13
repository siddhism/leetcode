class Solution(object):
    def reconstructQueue(self, people):
        people.sort(key=lambda (h, k): (-h, k))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue


print Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])