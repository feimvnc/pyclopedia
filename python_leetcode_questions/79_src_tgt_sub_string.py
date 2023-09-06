""" 
source: a string 
target: a string 
output: minimun string in source which includes target, return "" if no result.

Example:
source: "abc"
targe: "ac"
output: "abc"
"""

import collections 

class Solution:
    def minWindow(self, source, target):
        if source == None or target == None or len(source) == 0 or len(target) == 0:
            return "" 
        targetMap = collections.defaultdict(int)
        sourceMap = collections.defaultdict(int)  
        for i in range(len(target)):
            targetMap[target[i]] += 1 
        answer = "" 
        minLength = float("inf")
        end = 0 
        matched = 0 
        n = len(source)
        for start in range(n):
            while end < n and matched < len(targetMap):
                ch = source[end]
                sourceMap[ch] += 1 
                # if sourceMap[ch] == targetMap[ch]:   # error, add default if not found
                if sourceMap[ch] == targetMap.get(ch, 0):
                    matched += 1 
                end += 1
            if matched == len(targetMap):
                if end - start < minLength:
                    minLength = end - start 
                    answer = source[start : end ]
            ch = source[start]
            sourceMap[ch] -= 1 
            if sourceMap[ch] == targetMap.get(ch, 0) - 1:
                matched -= 1 
        return answer


source = "abc"
target = "ac"
print(Solution().minWindow(source, target))  # -> abc

