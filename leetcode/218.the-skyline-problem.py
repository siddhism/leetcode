#
# @lc app=leetcode id=218 lang=python
#
# [218] The Skyline Problem
#
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # https://leetcode.com/problems/the-skyline-problem/discuss/61261/10-line-Python-solution-104-ms
        #  https://www.youtube.com/watch?v=GSBLe8cKu0s
        from heapq import heapify, heappush, heappop
        heights = sorted([(l, -h, r) for l, r, h in buildings] + list(set([(r, 0, None) for l,r,h in buildings])))
        res = [[0,0]]
        heap = [(0, float('inf'))]
        for (x, neg_h, r) in heights:
            while x >= heap[0][1]:
                # if left is greater than existing building's right
                heappop(heap)
            if neg_h:
                heappush(heap, (neg_h, r))
            max_val = heap[0][0]
            if res[-1][1] + max_val:
                res.append((x, -max_val))
        return res[1:]















        

