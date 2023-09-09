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

    def three_sum_two_ptrs(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)   # -> [-1, -1, 0, 1, 2, 4]
        if not nums: 
            return []
        N = len(nums)
        res = [] 
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            head = i + 1
            end = N - 1  
            while head < end: 
                h, m, e = nums[head], nums[i], nums[end]
                if h + m + e == 0:
                    res.append([m, h, e])
                    head += 1
                    while head < end and nums[head] == nums[head-1]:
                        head += 1
                    end -= 1
                    while head < end and nums[end] == nums[end+1]:
                        end -= 1
                elif h + m + e < 0:
                    head += 1 
                    while head < end and nums[head] == nums[head - 1]:
                        head += 1 
                else: #  h + m + e > 0
                    end -= 1 
                    while head < end and nums[end] == nums[end + 1]:
                        end -= 1  

        return res 


nums = [-1, 0, 1, 2, -1, 4]
s = Solution()
print(s.three_sum(nums))   # -> [(-1, 0, 1), (-1, -1, 2)]

print(s.three_sum_two_ptrs(nums))   # -> [[-1, -1, 2], [-1, 0, 1]]

""" 
# without duplicate removal, 1st and 3rd item are same
$ python 09_three_sum.py 
[(-1, 0, 1), (-1, 2, -1), (0, 1, -1)]


# after duplicate removed 
$ python 09_three_sum.py 
[(-1, 0, 1), (-1, -1, 2)]
"""
