# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        if n == 1:
            return 1 if isBadVersion(n) else -1
        if n == 2:
            if isBadVersion(n) and not isBadVersion(n-1):
                return n
            return 1
        
        while left < right:
            mid = (left+right) / 2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif not isBadVersion(mid):
                # look right
                left = mid + 1
            else:
                # look left, even this is bad, so don't do mid -1
                right = mid
        # end condition
        if isBadVersion(left):
            return left
        return -1