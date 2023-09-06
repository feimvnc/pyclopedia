""" 
Jump Game I
Given an array of non-negative integers nums, you are initially positioned
at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example:
Input: nums = [2,3,1,1,4]
Output: true 
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: false 
"""

from typing import List 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1    # set the goal post at end 
        
        # check from right towards left 
        for i in range(len(nums)-1, -1, -1):   # from last index towards to beginning
            if i+nums[i] >= goal:  # if max jump can reach goal 
                goal = i    # shift goal to left once 

        return True if goal == 0 else False    # if goal is 0 we can reach all goals


# No extra memeroy is required
# Greedy method 

nums1 = [2,3,1,1,4]
nums2 = [3,2,1,0,4]
print(Solution().canJump(nums1))
print(Solution().canJump(nums2))


""" 
Jump Game II
Given an array of non-negative integers nums, you are initially positioned at the 
first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reacch the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Input: nums= [2,3,1,1,4]
Output: 2 
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.

Like minimum BFS search path.
"""

class Solution2:
    def jump(self, nums: List[int]) -> int: 
        res = 0    # set initial jump to 0 
        l = r = 0   # two left and right pointers set to 0, measure window size
        # l=1 
        # r=2    # means the window size is 2
        # below is a simplified bfs in one dimensional array 
        while r < len(nums) - 1:
            farthest = 0 
            for i in range(l, r+1):
                farthest = max(farthest, i+nums[i])   # how far can we jump
            l = r + 1   # update window size of l and r 
            r = farthest
            res += 1
        return res      # increment the steps each time 


nums22= [2,3,1,1,4]
print(Solution2().jump(nums22))

""" 
Jump game using dynamic programming method.
"""

class Solution_DP:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        f = [False] * n 
        f[0] = True 

        for j in range(1, n):
            f[j] = False 
            for i in range(0, n):
                if (f[i] and i + nums[i] >= j):
                    f[j] = True 
                    break 
        return f[n-1]


    def canJump2(self, nums: List[int]) ->bool:
        max_reach = 0   # how far can go 
        for i, num in enumerate(nums):
            if i > max_reach: return False    # if index beyond max_reach
            max_reach = max(max_reach, i + num)   # update s
        return True 


class Solution_DFS:
    def canJump(self, nums: List[int]) -> bool:

        from functools import lru_cache 
        @lru_cache(None)
        def dfs(i):
            # if yes 
            if i + nums[i] >= len(nums) - 1: return True 
            # if no
            if i != len(nums) - 1 and nums[i] == 0: return False 
            # otherewise continue 
            return any(dfs(i + d) for d in range(1, nums[i] + 1))
        return dfs(0)



nums3 = [3,2,1,0,4]
print(Solution_DP().jump(nums3))   # False 
nums33 = [2,3,1,1,4]
print(Solution_DP().jump(nums33))   # True 
print(Solution_DP().canJump2(nums3))   

print(Solution_DFS().canJump(nums3))    # False
print(Solution_DFS().canJump(nums33))   # True 
