""" 
Given an integer array nums, return true if any value appears 
at least twice in the array, return false if every element is disttinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true 

Example 2:
Input: nums = c
Output: false
"""

from typing import List 
import numpy as np


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        print(nums)
        return len(nums) != np.unique(nums).size 


nums = [1,2,1,2,3,4]
s = Solution()
print(s.contains_duplicate(nums))

nums2 = [1,2,3,4]
print(s.contains_duplicate(nums2))


""" 

r$ python 03_contains_duplicate.py 
[1, 2, 1, 2, 3, 4]
True
[1, 2, 3, 4]
False

"""