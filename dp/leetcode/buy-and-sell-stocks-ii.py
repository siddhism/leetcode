class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits = {}
        n = len(prices)
        if n  == 1:
            return 0
        if n == 2:
            return max(0, prices[1]-prices[0])
        # story buy sell and cooldown value at current index
        buy = [0 for i in range(n)]
        sell = [0 for i in range(n)]
        rest = [0 for i in range(n)]
        for i in range(1, n):
            # profit by buying at this place
            price = prices[i]
            buy[i]  = max(rest[i-1]-price, buy[i-1]) 
            sell[i] = max(buy[i-1]+price, sell[i-1])
            rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
            # buy = max(price, profits[i-1][0])
            # # profit by selling at this price
            # sell = max(profits[i-1][1] - price, profits[i-1][1])
            # # profit by keeping this in cooldown, same as sell of profits[i-1][1]
            # cooldown = profits[i-2][1]
            # profits[i] = [buy, sell, cooldown]
        print buy, sell, rest
        return sell[n-1]

print Solution().maxProfit([1,2,3,0,2])



        
         total_invited_count = self.model.objects\
            .filter(event_id__in=event_id_list)\
            .exclude(invited_count=0)\
            .aggregate(total=Sum('invited_count'))['total']