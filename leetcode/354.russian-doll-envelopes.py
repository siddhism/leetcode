#
# @lc app=leetcode id=354 lang=python
#
# [354] Russian Doll Envelopes
#
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        w_sorted = [(x, -y) for x, y in envelopes]
        w_sorted = sorted(envelopes)
        n = len(envelopes)
        if not n:
            return 0
        dp = [0 for _ in range(n)]
        dp[0] = 1
        w = 0
        h = 1
        print w_sorted, ' initially '
        for i in range(1, n):
            x, y = w_sorted[i]
            # y = -y
            for j in range(i):
                prev_x, prev_y = w_sorted[j]
                # prev_y = -prev_y
                if prev_x < x and prev_y < y:
                    dp[i] = max(dp[i], dp[j] + 1)
                # if w_sorted[j][w] < w_sorted[i][w] and w_sorted[j][h] < w_sorted[i][h]:
                #     dp[i] = max(dp[i], dp[j] + 1)
        print dp
        return max(dp)
        
print Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])

