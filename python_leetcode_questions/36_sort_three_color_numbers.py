""" 
Sort color number in place efficiently, don't use built-in sort() function.
"""
from typing import List 

class Solution:
    def sortColorNumbers(self, nums: List[int]) -> None:
        n = len(nums)
        r = n-1 
        l=0
        r=n-1
        ptr=0 
        while l<=r and ptr<=r:
            if nums[ptr] == 0:
                nums[ptr], nums[l] = nums[l], nums[ptr]
                ptr+=1
                l+=1 
            elif nums[ptr]==2:
                nums[ptr], nums[r] = nums[r], nums[ptr]
                r-=1 
            else:
                ptr += 1 
        print(nums)

    def sortColorNumbers_2(self, nums: List[int]) -> None:
        """ Do not return anything, modify nums in-place """
        l, r = 0, len(nums) - 1 
        i = 0 

        def swap(i,j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp 
        
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1 
            elif nums[i] == 2:
                swap(i, r)
                r -= 1 
                i -= 1 
            i += 1 
        print(nums)


nums = [2,1,0,2,1,0,1]
Solution().sortColorNumbers(nums) 
Solution().sortColorNumbers_2(nums) 

