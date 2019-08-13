class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        output = 0
        n = len(prices)
        if n == 0:
            return 0
        buy = prices[0]
        sell = 0
        profit = 0
        for i in range(1, n-1):
            print 'buy ', buy ,  ' sell ', sell, ' profit ', profit
            if prices[i] >= prices[i-1] and prices[i] > prices[i+1]:
                sell = prices[i]
                profit += sell - buy
            if prices[i] < prices[i-1]:
                buy = prices[i]
        # after completion check for last element
        if prices[n-1] >= prices[n-2]:
            sell = prices[n-1]
            profit += sell - buy
        return profit

# print Solution().maxProfit([5,2,3,2,6,6,2,9,1,0,7,4,5,0])
print Solution().maxProfit([1,9,6,9,1,7,1,1,5,9,9,9])
