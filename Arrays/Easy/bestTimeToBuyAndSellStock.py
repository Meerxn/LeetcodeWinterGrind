import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #find minima and stop
        buy = 0
        sell = 1
        currMax = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                currMax = max(currMax,profit)
            else:
                buy = sell
            sell +=1
        return currMax
                
                
                        
        
        