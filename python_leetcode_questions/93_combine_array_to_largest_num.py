""" 
Given an array of numbers, combine them into one largest number, 
return in string format.

Example
nums: [3, 30, 34, 5, 9]
outpu: '9534330'

Thoughts: For two numbers, it should AB>BA, A is in front of B.
"""
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):
        # sort array based on the rule
        sorted_nums = sorted(
            map(str, nums), key=cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        )
        result = "".join(sorted_nums).lstrip("0")
        return result or 0


nums = [3, 30, 34, 5, 9]
print(Solution().largestNumber(nums))  # -> 9534330
