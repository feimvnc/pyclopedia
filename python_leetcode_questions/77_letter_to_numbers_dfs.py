""" 
Given phone page number and letters, return all combinations of letters giving numbers.

Example
Input: 5
Output: ["j", "k", "l"]

Input: 23
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""

class Solution:

    def dfs(self, digits, idx, curString, numberToLetter, result):
        # exit condition 
        if idx == len(digits):
            result.append(curString)
            return 
        ch = digits[idx]
        for letter in numberToLetter[ch]:
            self.dfs(digits, idx+1, curString + letter, numberToLetter, result)

    def letterCombinations(self, digits):
        # edge case
        if not digits:   
            return [] 
        numberToLetters =  {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", 
                            "7": "pqrs","8": "tuv", "9": "wxyz"}
        result = [] 
        self.dfs(digits, 0, "", numberToLetters, result)
        return result 

print(Solution().letterCombinations('23'))  # -> ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print(Solution().letterCombinations('5'))   # -> ['j', 'k', 'l']