"""
Given an array of integerss, return indices of the two numbers 
such that they add up to a specific target.

Example: Given nums = [2, 7, 11, 15], target = 9

Because nums[0] + nums[1] = 2 + 7 = 9
return [0, 1]
"""

from typing import List 
from itertools import combinations
import numpy as np

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List:
        print(nums)
        print(list(combinations(nums, 2)))
        print(list(sum(x) for x in list(combinations(nums, 2))))
        l = list(set(x for x in list(combinations(nums, 2))))
        print(list(filter(lambda x: sum(x) == target, l)))
        res = list(filter(lambda x: sum(x) == target, l))
        return list([nums.index(res[0][0]), nums.index(res[0][1])])

    def two_sum_np(self, nums: List[int], target: int) -> List:
        na = np.array(nums)
        nb = np.array([2,7])
        sorter = np.argsort(na)
        print(sorter[np.searchsorted(na, nb, sorter=sorter)])
        res = sorter[np.searchsorted(na, nb, sorter=sorter)]
        return  res 

    # below can be a optimized version
    def two_sum_np_2(self, nums: List[int], target: int) -> List:
        # list comprehension to loop through list of 2 items 
        # use combination to extract list of all 2 items array
        # add sum conditon
        l =  list(x for x in list(combinations(nums, 2)) if sum(x) == target)

        # where returns indicces 
        # isin returns ndarray
        print(type(np.isin(nums, l)))
        res = np.where(np.isin(nums, l))

        return  res 

    def two_sum4(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target = n 
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i 
        return [] 


    # use two pointers
    def two_sum_5(self, ns: List[int], target: int) -> List[int]:
        l, r = 0, len(ns)-1
        while l<r:
            total = ns[l]+ns[r]
            if total == target:
                return [l+1, r+1]
            elif total < target:
                l += 1
            else:
                r -= 1
        return [-1,-1]

nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.two_sum(nums, target))
print(s.two_sum_np(nums, target))
print(s.two_sum_np_2(nums, target))
print(s.two_sum_5(nums, target))


""" output 

$ python 01_two_sum.py 
[2, 7, 11, 15]
[(2, 7), (2, 11), (2, 15), (7, 11), (7, 15), (11, 15)]
[9, 13, 17, 18, 22, 26]
[(2, 7)]
[0, 1]
[0 1]
[0 1]
<class 'numpy.ndarray'>
(array([0, 1]),)
[1, 2]
""" 