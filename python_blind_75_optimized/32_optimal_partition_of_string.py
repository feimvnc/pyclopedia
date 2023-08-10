""" 
Given a string s, partition one or more substrings such that the characters 
in each substring are unique, return the minimum number of substrings in 
such a partition.

Examples:
Input: s = "abacaba"
Output: 4
Explanation: ("a", "ba", "cab", "a")
"""

class Solution:
    def partition_str(self, s: str) -> int:
        # create set to track unique substring, 
        curSet = set()  
        # res is counter of unique substring
        res = 0 
        # record substring for learning purpose 
        substring_records = []
        for c in s: 
            # if found, reset and start new substring
            if c in curSet:   
                res += 1 
                curSet = set()
                substring_records.append(curSet)

            curSet.add(c)
            # when first char is added to set, increase counter
            if res == 0 and len(curSet):
                res += 1 
                substring_records.append(curSet)
                
        print(substring_records)
        return res 

print(Solution().partition_str("abacaba"))