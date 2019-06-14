class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        area = 0
        while start < end:
            print ('start ', height[start], ' end ', height[end], ' area ', area)
            new_area = min(height[start], height[end]) * (end-start)
            area = max(area, new_area)
            if height[start] < height[end]:
                start = start + 1
            else:
                end = end - 1
        return area

print Solution().maxArea([2,3,4,5,18,17,6])