#
# @lc app=leetcode id=475 lang=python
#
# [475] Heaters
#
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        import sys
        import bisect
        heaters = sorted(heaters)
        # heaters.insert(0, float('-inf'))
        # heaters.append(float('inf'))
        res = -sys.maxsize
        for house in houses:
            # find position of this house in heaters. (house itself is index we want to find)
            index = bisect.bisect_right(heaters, house)
            # distance from left heater
            dist_left = sys.maxsize
            dist_right = sys.maxsize
            if index -1 >= 0:
                dist_left = house - heaters[index - 1]
            if index < len(heaters):
                dist_right = heaters[index] - house
            cur_min = min(dist_left, dist_right)
            res = max(cur_min, res)
        return res
        
