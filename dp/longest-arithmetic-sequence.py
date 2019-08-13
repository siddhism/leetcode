class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n == 1:
            return 1
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        for i in range(1, n):
            if A[i] > A[i-1]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i-1]
            print i, A[i], dp[i]
        return dp[n-1]

print Solution().longestArithSeqLength([83,20,17,43,52,78,68,45])
print Solution().longestArithSeqLength([83,20,17,43,52,78,68,45]) == 2
print Solution().longestArithSeqLength([9,4,7,2,10]) == 3
print Solution().longestArithSeqLength([3,5,6,10]) == 4
print Solution().longestArithSeqLength(20,1,15,3,10,5,8) == 4
