""" 
Remove duplicatess in-place
Do not allocate extra spacce for another array.
Must have the result be placedd in the first part of the array nums.
The first part of the array nums should holddd the final result.  
Must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:
The judge will test your solution with the followinig code.

int[] nums = [...];   //input array
int[] expectedNums = [...];   // expected answer with correct length 

int k = removeDuplicates(nums);    // calls your implementation 
assert k == expectedNums.length;
for (int i=0, i<k, i++) {
    assert nums[i] == expectedNums[i];
}
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        left = 1 

        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1     # left only moves when current != prev not same 
            # print(nums[right], left)
        print(nums)
        return left 

    def removeDuplicates_2(self, nums: List[int])-> int:
        if len(nums) == 0: return 0 
        if len(nums) == 1: return 1 

        # nums = [0,0,1,1,1,2,2,3,4]
        j = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1 

        # after above, i=9, j=5
        for delete_index in range(i, j-1, -1):   # delete backwards 
            del nums[delete_index]

        print(nums)

        return j 


nums = [0,0,1,1,1,2,2,3,4]
print(Solution().removeDuplicates(nums))
nums = [0,0,1,1,1,2,2,3,4]
print(Solution().removeDuplicates_2(nums))