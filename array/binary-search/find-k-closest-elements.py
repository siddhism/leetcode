class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        from collections import defaultdict
        n = len(arr)
        left = 0
        right = n - 1
        index = -1
        while left <= right:
            mid  = (left + right)/ 2
            # print left, right, mid
            if arr[mid] == x:
                index = mid
                break
            elif arr[mid] > x:
                right = mid -1
            else:
                # if not exact index, get the next one
                index = mid + 1
                left = mid + 1
        if index == -1:
            if x < arr[0]:
                # smaller than first elemtn
                return arr[:k]
            elif x > arr[n-1]:
                # bigger than last element
                # print 'here'
                return arr[n-k:]
        # how to get k closest elements
        low = max(index - k-1, 0)
        high = min(index + k-1, n-1)
        # i = 1
        # result = []
        while (high-low) > k-1:
            if low < 0 or (x - arr[low]) <= (arr[high]-x):
                high = high - 1
            elif high > n-1 or (x - arr[low]) > (arr[high]-x):
                low = low + 1

        return arr[low:high+1]

print Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3)
print Solution().findClosestElements([0,0,1,2,3,3,4,7,7,8],3,5)
print Solution().findClosestElements([0,0,0,1,3,5,6,7,8,8],2,2)
print Solution().findClosestElements( [0,1,1,1,2,3,6,7,8,9], 9, 4)
