""" 
Product of array except self 

Given an integer array nums, return an array answer succh aht answer[i] is 
equal to the product of all the elements of nums except nums[i].

You must write an algorithm that runs ini O(n) time and without using 
hte division operation.

Example 1: 
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1, 1, 0, -3 3]
Output: [0, 0, 9, 0, 0]
"""

from typing import List 
import numpy as np 

class Solution: 

    def prod_array_except_self(self, nums: List[int]) -> List[int]:

        # create np array
        nn = np.array(nums)
        # result to be returned 
        res = []
        # use np.prod to have product of all items
        # use division self value to remove from the product
        # use map function for elementwise operation 
        # convert to list 
        # use // to keep int type 
        if 0 in nn:
            res = np.where(nn==0, np.prod(nn[nn!=0]), 0)
            # print(res)
        else:
            res = list(map(lambda x: np.prod(nn)//x, nn))
            # print(res)

        return res


nums = [1,2,3,4]
s = Solution()
print(s.prod_array_except_self(nums))

nums2 = [-1, 1, 0, -3, 3]
print(s.prod_array_except_self(nums2))

