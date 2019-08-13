class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        buy = prices[0]
        sell = prices[0]
        profit = sell - buy
        n = len(prices)
        for i in range(1, n):
            cur = prices[i]
            prev = prices[i-1]
            if cur < buy:
                buy = cur
                sell = cur # reset sell to curr
            if cur > sell:
                sell = cur
            profit = max(profit, sell-buy)
        return profit
            