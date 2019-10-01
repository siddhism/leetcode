#
# @lc app=leetcode id=1066 lang=python
#
# [1066] Campus bikes 2

class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        from heapq import heapify, heappush, heappop
        from collections import defaultdict
        d_workers = defaultdict(list)
        d_bikes = defaultdict(list)
        distances = [[]] * len(workers)
        for iw, (wx, wy) in enumerate(workers):
            # every worker has a min heap of distances stored in it
            h = []
            for ib, (bx, by) in enumerate(bikes):
                d = abs(bx-wx) + abs(by-wy)
                heappush(d_workers[iw], d)
                heappush(d_bikes[ib], d)
                h.append(d)
            distances[iw] = h
        print 'd workers', d_workers
        print 'd bikes ', d_bikes        
        d_bikes[ib].sort()
        used_bikes = set()
        assigned_workers = set()
        target = len(bikes)
        # assign target no of bikes to get min distances
        # input  workers : [[0,0],[2,1]], bikes = [[1,2],[3,3]]
        # (2, 1, 3) (2, 3, 1) (2, 2, 2)
        n_workers = len(workers)
        n_bikes = len(bikes)
        dp = [[float('inf') for _ in range(n_bikes)] for _ in range(n_workers)]
        # for w in workers[0]:
        #     for 
        dp[0] = d_workers[0]
        print dp

        for iw in range(1, len(workers)):
            for ib in range(1, len(bikes)):
                # get min of prev workers and prev bike
                min_without_this_worker = min(d_workers[iw-1])
                min_without_this_bike = min(d_bikes[ib-1])
                # these both shouldn't be of same? or can be
                print ( ' pickking ', d_workers[iw], d_bikes[ib], min_without_this_worker, min_without_this_bike)
                dp[iw][ib] = distances[iw][ib] + min(min_without_this_bike, min_without_this_worker)
                print distances[iw][ib], dp[iw][ib]
        print ' DP Array ', '*' * 20, dp
        return min(dp[n_workers-1])


print Solution().assignBikes(workers= [[0,0],[2,1]], bikes = [[1,2],[3,3]])












