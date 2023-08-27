"""
Given an integer array nums, find the contiguous subarray  within an array 
(containing at least one number) which has the largest product.

Example: 
Input: [2,3,-2,4]
Output: 6 

[2,3]sAt least has the largest product 6
"""

import numpy as np 
from typing import List 

class Solution():
    def max_prod_subarray(self, nums: List[int]) -> List[int]:
        res = [] 
        # # create a list of all subarrays
        # for i in range(len(nums) + 1):
        #     for j in range(i, len(nums)+1):
        #         if i != j:
        #             res.append(nums[i:j])

        res = [nums[i:i+j] for i in range(0, len(nums)) for j in range(1, len(nums)-i+1)]
        print(res)
        # use map to get list of prod of list items 
        # get the max value, [0]: max values, [1]: list item
        return max(list(map(lambda x: (np.prod(x), x), res)))[1]


nums = [2,3,-2,4]
s = Solution()
print(s.max_prod_subarray(nums))
