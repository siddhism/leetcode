#
# @lc app=leetcode id=939 lang=python
#
# [939] Minimum Area Rectangle
#
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        seen = set()
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area < res:
                        res = area
            seen.add((x1, y1))
        return res if res < float('inf') else 0

# print Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]])



