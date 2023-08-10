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
            print(nums[right], left)
        print(nums)
        return left 

nums = [2,2,3,5,8,8,8,9,10]
print(Solution().removeDuplicates(nums))