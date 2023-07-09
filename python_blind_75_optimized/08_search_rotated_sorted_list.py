""" 
Suppose an array sorted in ascending order is rotated at some pivoot unknown to you beforehand.
(i.e. [0,1,2,3,4,5,6,7] might become [4,5,6,7,0,1,2])

You are given a target value to search, if found in the array return its index, 
otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n)

Example 1:
Input: nums = [4,5,6,7,0,1,2,],  target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2,],  target = 3
Output: -1
"""

from re import A
from typing import List 
import numpy as np 

class Solution:
    def search_rotated_sorted_list(self, nums: List[int], target) -> int:
        nums_np =np.array(nums)
        a = np.where(nums_np==target)
        # print(a)
        # a[0][0], get value from tuple list
        a = a[0][0] if np.size(a[0]) else -1
        print(nums, target, a)
        
        return a


nums = [4,5,6,7,0,1,2]
target1 = 6
target2 = 9
s = Solution()
s.search_rotated_sorted_list(nums, target1)
s.search_rotated_sorted_list(nums, target2)


""" 
$ python 08_search_rotated_sorted_list.py 
[4, 5, 6, 7, 0, 1, 2] 6 2
[4, 5, 6, 7, 0, 1, 2] 9 -1

"""