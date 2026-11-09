class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        max_profit = 0
        for i in range(length):
            for j in range(i+1,length):
                max_profit = max(prices[j]-prices[i],max_profit)



        return max_profit
