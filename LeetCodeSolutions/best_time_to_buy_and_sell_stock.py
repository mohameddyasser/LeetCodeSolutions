import numpy as np
class Solution(object):
    def maxProfit(self, prices):
        currect = 0
        next = 1
        max_profit = 0
        while next < len(prices):
            currentProfit = prices[next] - prices[currect]
            if prices[currect] < prices[next]:
                max_profit =max(currentProfit,max_profit)
            else:
                currect = next
            next += 1
        return max_profit
        
