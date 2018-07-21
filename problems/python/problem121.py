"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
#         find_min
#         find_max to right of find_min
#         calc profit
#         if profit > max_profit: profit = max_profit
#         rinse/repeat for items to the left of the min
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        
        while prices:
            min_price = min(prices)
            min_price_ind = prices.index(min_price)
            max_sell_price = max(prices[min_price_ind:])
            profit = max_sell_price - min_price
            max_profit = max(max_profit, profit)
            prices = prices[:min_price_ind]
        return max_profit

if __name__ == "__main__":
    sol = Solution()
    input = [7,1,5,3,6,4]
    result = sol.maxProfit(input)
    assert result == 5
