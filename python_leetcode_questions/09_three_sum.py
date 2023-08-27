""" 
Given an array nums of n integers, are there elements a, b, c in nums, 
such that a+b+c = 0?  Find all unique triplets in the array 
which gives the sum of zero.

Note: 
The solution set must not contain duplicate triplets.

Example:

nums = [-1, 0, 1, 2, -1, 4]
A solution set is:
[
    [-1, 0. 1],
    [-1, -1, 2]
]
"""
from typing import List 
from itertools import combinations
import numpy as np  

class Solution:

    def zero_sum_list(self, l: List[int]) ->List[int]:
        if sum(l) ==0:
            return l

    def three_sum(self, nums: List[int]) -> List[int]:
        # create 3 item list 
        temp = combinations(nums, 3)
        
        # use map to remove duplicate list item 
        temp = set(map(lambda x: tuple(sorted(x)), temp))

        # filter list with condition of sum() == 0
        return (list(filter(self.zero_sum_list, temp)))


nums = [-1, 0, 1, 2, -1, 4]
s = Solution()
print(s.three_sum(nums))


""" 
# without duplicate removal, 1st and 3rd item are same
$ python 09_three_sum.py 
[(-1, 0, 1), (-1, 2, -1), (0, 1, -1)]


# after duplicate removed 
$ python 09_three_sum.py 
[(-1, 0, 1), (-1, -1, 2)]

"""
