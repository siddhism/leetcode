class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        sum = 0
        l = 0
        r = n - 1
        left_max = 0
        right_max = 0
        while l <= r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            if left_max < right_max:
                sum += left_max - height[l]
                l = l + 1
            else:
                sum += right_max - height[r]
                r = r - 1
        return sum

print Solution().trap([5,4,1,2])
