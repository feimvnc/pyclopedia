from typing import List 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # for result
        path = []  # current result satisfy requirements
        def backtracking(nums, index):          # start at the index 
            res.append(path[:])                 # add to result 
            if index >= len(nums):              # stop condition, exit
                return

            for i in range(index, len(nums)):   # through the loop
                path.append(nums[i])            # add to path current result 
                backtracking(nums, i + 1)       # back to next item
                path.pop()                      # cancel or remove current result 

        backtracking(nums, 0)      # start at 0  
        return res


nums = [1,2,3]
print(Solution().subsets(nums))
