""" 
Suppose an array of length n sorted in ascending order is rotated between 1 and
n times. For example, the array nums = [0,1,2,3,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times 
[0,1,2,4,5,6,7] if it was rotated 7 times

Notice that rotatng an array [a[0], a[1], a[2],...,a[n-1]] 1  times results
in the array [a[n-1], a[0], a[1], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
"""

# O(log n) means as the input size gorws, the number of operations grows very slowly
# Example: binary search 
 
from typing import List 

class Solution:
    def min_rotated_array(self, nums: List[int]) -> int:
        # use binary search method, left and right pointer
        l, r = 0, len(nums)
        print(nums, len(nums))

        while l<r:
            
            mid = len(nums)//2
            # divide list at middle 
            # first mid is exclusive, second mid is inclusive
            if (min(nums[0:mid])<min(nums[mid:])):
                temp = nums[0:mid]
                r = mid-1 
            else:
                temp = nums[mid:]
                l = mid+1
            nums = temp 
            print(nums, len(nums), f'{l=}, {r=}')

        # just be safe, return min
        return min(nums)



nums = [3,4,5,1,2]
s = Solution()
print(s.min_rotated_array(nums))


"""  

$ python 07_min_rotated_array 
[3, 4, 5, 1, 2] 5
[5, 1, 2] 3 l=3, r=5
[1, 2] 2 l=2, r=5
[1] 1 l=2, r=0
1

"""