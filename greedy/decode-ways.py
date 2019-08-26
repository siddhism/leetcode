class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if not s:
            return 0
        truth = [False for _ in range(n)]
        dp = [0 for _ in range(n+1)]
        x = map(str, range(1, 27))
        dp[0] = 1
        # if len(s) > 1:
        #     last_two = s[0:2]
        #     if dp[0]:
        #         if s[1] in x:
        #             if last_two in x:
        #                 dp[1] = 2
        #             else:
        #                 dp[1] = 1
        #         else:
        #             dp[1] = 0
        #     else:
        #         if s[1] in x:
        #             dp[1] = 1
        #         else:
        #             dp[1] = 0
        # DP array has first index as dummpy, dp[1] represents first char
        if s[0] != '0':
            dp[1] = 1
        else:
            dp[1] = 0

        for i in range(2, n+1):
            c = s[i-1:i]
            two_char = s[i-2:i]
            if c in x:
                dp[i] += dp[i-1]
            if two_char in x:
                dp[i] += dp[i-2]
        print dp
        return dp[n]

print Solution().numDecodings("10")
print Solution().numDecodings("10") == 1
print Solution().numDecodings("01")
print Solution().numDecodings("01") == 0
print Solution().numDecodings("00") == 0
print Solution().numDecodings("301") == 0
print Solution().numDecodings("226") == 3
print Solution().numDecodings("1226") == 5
