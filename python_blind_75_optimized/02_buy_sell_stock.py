"""
You have an array for which the ith element is the price 
of a given stock on day i.
If you were only permitted to complete at most one tranaction (i.e., 
buy one and sell one share of the stock), 
design an algorithm to find the maximum profit
Note that you cannot sell a stock before you buy one.\

Example: 
Input: [7,1,5,3,6,4]
output: 5
Explanation: Buy on dday 2 (price = 1) and sell on day 5 (price =6),
profit = 6-1 =5, not 7-1=6, as selling price needs to be larger than buying price.
"""

from typing import List
from itertools import combinations


class Solution:  
    def buy_sell(self, prices: List[int]) -> int:
        print(prices)
        print(list(combinations(prices, 2)))

        # create a list of 2 items
        l = list(combinations(prices, 2))

        # find the item which has max values
        print(np.max(list(combinations(prices, 2))))
        m = np.max(list(combinations(prices, 2)))
        v = l[m][1]    # the 2nd value of the pair

        print(prices.index(v) + 1, "day to sell")      # add 1, index starts att 0
        day = prices.index(v) + 1
        return day 
        

prices = [7,1,5,3,6,4]
s = Solution()
s.buy_sell(prices)


"""
$ python 02_buy_sell_stock.py 
[7, 1, 5, 3, 6, 4]
[(7, 1), (7, 5), (7, 3), (7, 6), (7, 4), (1, 5), (1, 3), (1, 6), (1, 4), (5, 3), (5, 6), (5, 4), (3, 6), (3, 4), (6, 4)]
7
5

"""