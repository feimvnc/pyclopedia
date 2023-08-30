from distutils import ccompiler
from syslog import closelog


class Solution:
    def isValid(self, s: str)->bool:
        stack = [] 
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:   # when having closing parentheses
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:    # get opening parentheses
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(c)
        return True if not stack else False    # when stack is empty all valid 


print(Solution().isValid("()[]{}"))    # True
print(Solution().isValid("()[]{}("))    # False 