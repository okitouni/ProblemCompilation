# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
from typing import List

def max_profit(prices:List[int])->int:
    lowest = prices[0]
    profit = 0
    for price in prices[1:]:
        if price < lowest:
            lowest = price
        else:
            profit = max(profit, price - lowest)
    return profit



