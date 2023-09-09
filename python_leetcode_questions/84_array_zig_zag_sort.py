"""
Given an array A (distinct elements) of size N.
Rearrange the elements of array in zig-zag fashion.
The converted array should be in form a < b > c < d > e < f.
The relative order of elements is same in the output 
i.e you have to iterate on the original array only.
"""

from typing import List 

class Solution:

    def sortZigZag(self, nums: List[int]) -> List: 
        if not nums: return []
        N = len(nums)
        for i in range(0, N-1):
            # first val, 1, 2, 3, (1 > 2 False, keep)
            if i % 2 == 0 and nums[i] > nums[i + 1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            # next val, 1, 2, 3 , (2 < 3 True, change)
            elif i % 2 != 0 and nums[i] < nums[i + 1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums 

nums = [1,2,3,4,5]
print(Solution().sortZigZag(nums))   # -> [1, 3, 2, 5, 4]
        