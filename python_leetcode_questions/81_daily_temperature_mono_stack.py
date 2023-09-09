"""  
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you 
have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73] 
Output: [1,1,4,2,1,1,0,0]

"""

from typing import List 

class Solution:

    # brute force 
    def daily_temperature_bf(self, t: List[int]) -> List[int]:
        N = len(t)
        res = [0] * N 
        for i in range(N):
            for j in range(i+1, N):
                if t[j] > t[i]:
                    res[i] = j - i 
                    break 

        return res 

    def daily_temperature_mono_stack(self, t: List[int]) -> List[int]:
        if not t: 
            return [0]

        N = len(t)
        st = []    # mono stack 
        res = [0] * N 
        for i in range(N):
            while st and t[st[-1]] < t[i]:
                res[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        
        return res 


t = [73,74,75,71,69,72,76,73] 
print(Solution().daily_temperature_bf(t))  # -> [1, 1, 4, 2, 1, 1, 0, 0]

print(Solution().daily_temperature_mono_stack(t))  # -> [1, 1, 4, 2, 1, 1, 0, 0]

