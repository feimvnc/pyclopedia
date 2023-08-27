from ftplib import all_errors
import itertools
from typing import List 

class Solution:
    def all_sub_arrays(self, nums):
        n = len(nums)
        indices = list(range(n+1))

        # get all sub-array from the list 
        for i,j in itertools.combinations(indices, 2):
            yield nums[i:j]

    def max_sub_array(self, nums: List[int])->int:
        print(list(self.all_sub_arrays(nums)))
        # get all sub-arrays
        # map to sum of sub-arrays
        # return max 
        return max(map(sum, self.all_sub_arrays(nums)))
        

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.max_sub_array(nums))


"""  
$ python 06_max_sum_subarray.py 
[[-2], [-2, 1], [-2, 1, -3], [-2, 1, -3, 4], [-2, 1, -3, 4, -1], [-2, 1, -3, 4, -1, 2], [-2, 1, -3, 4, -1, 2, 1], [-2, 1, -3, 4, -1, 2, 1, -5], [-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [1, -3], [1, -3, 4], [1, -3, 4, -1], [1, -3, 4, -1, 2], [1, -3, 4, -1, 2, 1], [1, -3, 4, -1, 2, 1, -5], [1, -3, 4, -1, 2, 1, -5, 4], [-3], [-3, 4], [-3, 4, -1], [-3, 4, -1, 2], [-3, 4, -1, 2, 1], [-3, 4, -1, 2, 1, -5], [-3, 4, -1, 2, 1, -5, 4], [4], [4, -1], [4, -1, 2], [4, -1, 2, 1], [4, -1, 2, 1, -5], [4, -1, 2, 1, -5, 4], [-1], [-1, 2], [-1, 2, 1], [-1, 2, 1, -5], [-1, 2, 1, -5, 4], [2], [2, 1], [2, 1, -5], [2, 1, -5, 4], [1], [1, -5], [1, -5, 4], [-5], [-5, 4], [4]]
6

"""