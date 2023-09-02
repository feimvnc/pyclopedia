""" 
Given an array of numbers, find a continuous subarray of the list
which adds up to a given sum.

Example:
Input: [1,7,4,2,1,3,11,5], k = 10 
Output: 2 5  , because sum of input[2:5] == 10

Approach: 
-Use two pointer, i, j
-Calculate the sum of the slice of nums[i:j]
-If sum found, return (i, j-1), need to use list indices length - 1
-If sum big, move left i +=1
-If sum small, move right j+=1
"""

from typing import List 

class Solution:
    def subarray_sum(self, nums: List[int], k: int) -> List[int]:
        
        i, j = 0, 1
        cur_total = nums[0]
        length = len(nums)
        result = [] 

        while i < length - 1 and j < length - 1:
            cur_total = sum(nums[i:j])
            if cur_total == k:
                result = [i,j-1]   # j-1 because j index is exclusive 
                break
            elif cur_total > k:
                i += 1
            elif cur_total < k:
                j += 1
        return result if result else []

    def subarray_sum_optimized_2(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        i, j, s = 0, 0, 0
        while i < n and j < n + 1:
            if s == k:
                return i, j-1 
            elif s < k:
                if j < n: 
                    s += nums[j]
                j += 1 
            elif s > k:
                s -= nums[i]
                i += 1 
        return []



    def subarray_sum_brute_force(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        for i in range(0, n):
            for j in range(i, n+1):
                if sum(nums[i:j]) == k:
                    return [i, j-1]
        return []


nums = [1,7,4,2,1,3,11,5]
k = 10  

print(Solution().subarray_sum(nums, k))
# [2, 5]

print(Solution().subarray_sum_optimized_2(nums, k))
# (2, 5)

print(Solution().subarray_sum_brute_force(nums, k))
# [2, 5]


