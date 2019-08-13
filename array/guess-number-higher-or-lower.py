# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num, target=1702766719):
    if num == target:
        return 0
    if num < target:
        return -1
    else:
        return 1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            print 'left ', left, ' right ', right, ' mid ', mid
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid + 1
            else:
                right = mid - 1
        return -1

print Solution().guessNumber(2126753390)