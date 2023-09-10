""" 
Given an array, only one number appears in odd number of times, 
other numbers appears in even number of times.
Find the one number which appears in odd number of times.

Example: 
Input: [2,2,4,4,6,6,5,5,5]
Output: 5
"""
from typing import List 

class Solution:

    # use just one var 'eor' and one loop, no map 
    def get_num(self, nums: List) -> int:
        N = len(nums) 
        eor = 0
        for i in range(N):
            eor ^= nums[i]

        return eor 

    def find_number_odd_times(self, nums: List[int]) -> int: 
        if not nums:
            return None

        return self.get_num(nums)

nums = [2,2,4,4,6,6,5,5,5]
print(Solution().find_number_odd_times(nums))   # -> 5 

