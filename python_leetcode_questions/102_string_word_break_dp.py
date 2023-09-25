""" 
Given a string, check if it can be broke into given word list.

Input: 
s = "leetcode", wordDict = {"leet", "code"} 
Output: 
True
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i, -1, -1):
                print(dp, dp[j], s[j : i + 1])
                # j <- i, decreasing
                # s[j:i+1] -> from j to i + 1
                # leetcode
                # 01234567  i = 3
                # 0<-j
                # dp[4] = True , i = 1 = 3
                if dp[j] and s[j : i + 1] in wordDict:  # j = 0, i = 3
                    dp[i + 1] = True
                    break
        return dp[n]


s = "leetcode"
wordDict = {"leet", "code"}


print(Solution().wordBreak(s, wordDict))
