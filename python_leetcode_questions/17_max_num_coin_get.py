""" 
Maximum number of coins you can get
There are 3n piles of coins of varying size, here are rules
Alice  always picks the maximum number of coins 
You pick the next maximum coin 
Bob will pick the last pile
"""
from typing import List 

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles)    # sort the list first 
        end_index = len(piles)-1
        our_value = 0 
        for i in range(len(piles)//3):
            our_value += sorted_piles[end_index-(i*2)-1]    # after max taken each time from max end
        return our_value

    def maxCoins2(self, piles: List[int])-> int:
        sorted_piles = sorted(piles, reverse=True)    # sort in reverse order 
        # because we have 3 person, we can remove last person Bob's value 
        temp = sorted_piles[:-3]    # remove value of last person 
        res = sum(temp[1::2])    # add value of you picked, the 2nd max
        print(temp, temp[1::2], res)
        return res

    def maxCoins3(self, piles: List[int])->int:
        return sum(sorted(piles)[len(piles) // 3::2])   # slice, every 3, and 2nd value

print(Solution().maxCoins([2,4,1,2,7,8]))
print(Solution().maxCoins([9,8,7,6,5,4,3,2,1]))

print(Solution().maxCoins2([2,4,1,2,7,8]))
print(Solution().maxCoins2([9,8,7,6,5,4,3,2,1]))

print(Solution().maxCoins3([2,4,1,2,7,8]))
print(Solution().maxCoins3([9,8,7,6,5,4,3,2,1]))
