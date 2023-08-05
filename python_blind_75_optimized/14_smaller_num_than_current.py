""" 
Given the array nums, for each nums[i] find out how many numbers in the 
array are smaller than it.
Input: nums = [8,1,2.2.3]
Ouptut: [4,0,1,1,2]    (count of each num in the array < current num)
"""

from cgitb import small
from math import remainder
from typing import List 

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int])-> List[int]:
        output = [] 
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    count += 1
            output.append(count)
        return output 

    def smallerNumbersThanCurrent2(self, nums: List[int])-> List[int]:
        sorted_nums = sorted(nums, reverse=True)
        smaller_count = {}
        for i in range(len(sorted_nums)-1):    # index beging with 0, len woth 1
            curr_num = sorted_nums[i]
            next_num = sorted_nums[i+1]
            if next_num < curr_num:
                remaining_value = len(sorted_nums)-(i+1)
                smaller_count[curr_num] = remaining_value

        smaller_count[sorted_nums[-1]] = 0   # the last element in array has 0 num < it

        output = []
        for num in nums:
            output.append(smaller_count[num])
        return output


print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))
print(Solution().smallerNumbersThanCurrent2([8,1,2,2,3]))