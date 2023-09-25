""" 
Break string into words, separated by space, find all combinations.

Input: 
s = "catsanddog", 
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
["cats and dog", "cat sand dog"]

Method:
Use dfs to query and compare.
Use hashtable to save query results and keep lookup table.
"""

import collections


class Solution(object):
    def workBreak(self, s, wordDict):
        dic = collections.defaultdict(list)

        def dfs(s):
            if not s:
                return [None]
            if s in dic:
                return dic[s]
            res = []
            for word in wordDict:
                n = len(word)
                # print("x", n, s[:n])
                if s[:n] == word:
                    for r in dfs(s[n:]):  # search rest string
                        if r:
                            res.append(word + " " + r)
                        else:
                            res.append(word)
            dic[s] = res
            return res

        return dfs(s)


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(Solution().workBreak(s, wordDict))  # -> ['cat sand dog', 'cats and dog']
