from typing import List 

class Solution:
    def moveZeros(self, nums: List[int]) -> List[int]:
        l = 0 
        for r in range(len(nums)):
            if nums[r]:   # if non zero, swap nums[r] with nums[l]
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums 


nums = [0,1,0,3,12]
print(Solution().moveZeros(nums))