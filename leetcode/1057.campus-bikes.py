#
# @lc app=leetcode id=1057 lang=python
#
# [1057] Campus bikes
#
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        # worker sorted by x, y, index
        # bikes sorted by x, y, index
        n_workers = len(workers)
        n_bikes = len(bikes)
        distances = {}
        # It's a matrix for each worker having (d, windex, bindex)
        for n_worker, (x, y) in enumerate(workers):
            cur_worker_bike_dist = []
            for n_bike, (bx, by) in enumerate(bikes):
                d = abs(bx-x) + abs(by-y)
                cur_worker_bike_dist.append((d, n_worker, n_bike))
            # reversed in order of shortest distance first
            cur_worker_bike_dist = sorted(cur_worker_bike_dist, reverse=True)
            distances[n_worker] = cur_worker_bike_dist

        # now for each worker pick first bike
        used_bikes = set()
        # push all distances into a heap
        from heapq import heapify, heappush, heappop
        queue = [distances[i].pop() for i in range(len(workers))]
        heapify(queue)
        print queue
        res = [None]* n_workers
        while len(used_bikes) < len(workers):
            d, worker, bike = heappop(queue)
            if bike not in used_bikes:
                res[worker] = bike
                used_bikes.add(bike)
            else:
                # pick next pair of d, worker, bike for this worker and push into heap
                temp = distances[worker].pop()
                heappush(queue, temp)
        return res






        workers = [(val[0], val[1], idx) for idx, val in enumerate(workers)]
        bikes = [(val[0], val[1], idx) for idx, val in enumerate(bikes)]
        workers = sorted(workers)
        bikes = sorted(bikes)
        dists = []
        for worker in workers:
            for bike in bikes:
                dist = abs(bike[0] - worker[0]) + abs(bike[1] - worker[1])
                worker_idx = worker[2]
                bike_idx = bike[2]
                data = (dist, worker_idx, bike_idx)
                dists.append(data)
        dists = sorted(dists)
        # pick unique worker_bike pairs from dists
        assigned_bikes = []
        assigned_workers = []
        result = []
        for dist in dists:
            if len(result) == n_workers:
                break
            worker = dist[1]
            bike = dist[2]
            if worker in assigned_workers or bike in assigned_bikes:
                continue
            assigned_bikes.append(bike)
            assigned_workers.append(worker)
            result.append((worker, bike))
        values = [item[1] for item in sorted(result)]
        return values
    
# Solution().assignBikes([[0,0],[2,1]], [[1,2],[3,3]])













    