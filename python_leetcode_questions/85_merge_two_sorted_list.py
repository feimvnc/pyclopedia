""" 
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 
respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
""" 

from typing import List 

class Solution:
    def  merge(self, nums1: List[int], m: int, nums2:  List[int], n: int) -> None:
        a, b, write_index = m-1, n-1, m + n - 1
        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1 
            else:
                nums1[write_index] = nums2[b]
                b -= 1 
            write_index -= 1 

        print(nums1, nums2)
        # no return 


nums1 = [1,2,3,0,0,0] 
nums2 = [2,5,6]
m = 3, 
n = 2
print(nums1, nums2)   # -> [1, 2, 3, 0, 0, 0] [2, 5, 6]
Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)  # -> [1, 2, 2, 3, 5, 6] [2, 5, 6]
