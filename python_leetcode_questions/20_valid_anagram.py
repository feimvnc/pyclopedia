from typing import Counter


class Solution: 
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)== Counter(t)

    def isAnagram2(self, s: str,  t: str) -> bool:
        if len(s) != len(t):
            return False 

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1 
            countT[t[i]] = countT.get(t[i], 0) + 1 
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False 
        return True 

    def isAnagram3(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


s = 'anagram'
t = 'nagaram'
print(Solution().isAnagram(s, t))
print(Solution().isAnagram2(s, t))