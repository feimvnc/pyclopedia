class Solution(object):
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0 
        temp = s.split(' ')
        temp = [t for t in temp if len(t)>0]
        if len(temp) == 0:
            return 0 
        else:
            return len(temp[-1])
    

print(Solution().lengthOfLastWord("hello world"))
