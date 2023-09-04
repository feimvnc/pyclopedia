""" 
Given a list of non negative integers, arrange them 
such that they form the largest number.

Example:
Input: [10, 2]
Outupt: "210"

Input: [3,30,34,5,9]
Output: "9539343"
"""

from typing import List  
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 0:
            return ""

        # conver int array to str array 
        nums_s = []
        for element in nums:
            nums_s.append(str(element))

        # x,y =str(2), str(20)
        # x+y, y+x, x+y>y+x  # -> ('220', '202', True)
        sort_key = lambda x, y: int(y+x) - int(x+y)   # '20'+'2 - '2'+'20'
        sorted_nums = sorted(nums_s, key=cmp_to_key(sort_key))  # ['9', '5', '39', '34', '3']
        result = ''.join(sorted_nums).lstrip('0')   # remove left '0' if appears 

        return result 


print(Solution().largestNumber([3,30,34,5,9]))   # -> 9534330

 