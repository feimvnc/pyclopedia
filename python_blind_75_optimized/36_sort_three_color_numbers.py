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

nums = [2,1,0,2,1,0,1]
Solution().sortColorNumbers(nums)
