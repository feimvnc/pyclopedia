""" 
Given an array, rotate k position to right.
Provide a solution of O(1) space complexity.

Input: [1,2,3,4,5,6,7], k=3
Output: [5,6,7,1,2,3,4]
"""
# Thought process
# A solution for in place rotation, a different equivalent idea 
# - reverse nums from 0 to n-k-1 
# - reverse nums from n-k to n-1
# - reverse nums from 0 to n-1

class Solution(object):
    def rotate(self, nums, k):

        # move front
        def reverse(nums, start, end):
            while start < end: 
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -=1  
        
        n = len(nums)
        k %= n    # modulo k when k > len(nums)
        reverse(nums, 0, n-k-1)    # reverse left part
        reverse(nums, n-k, n-1)    # reverse right part
        reverse(nums, 0, n-1)      # reverse whole array to achieve same result
        print(nums)   # print out result 

nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)     # [5, 6, 7, 1, 2, 3, 4]