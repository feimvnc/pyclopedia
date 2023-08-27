""" 
Given a string s containing just the characters '(',')','{','}','[',']', determines if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Examples:
Input: s = "()"
Output: true 

Input: s = "()[]{}"
Output: true 
 
Input: s = "(]"
Output: true 
"""

""" 
Stack operation patterns:
stack = [] 
if condition of item:
    stack.pop()
else: 
    stack.append(item)
"""

from curses.ascii import SO
from lib2to3.pgen2.literals import simple_escapes
from typing import List

class Solution():

    def isValidParentheses(self, s: str) -> bool: 
        stack = [] 
        mapper = {")":"(","]":"[","}":"{"}
        for p in s:
            if p in ")]}":
                if stack and stack[-1] == mapper[p]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(p)  
        return stack == [] 


s1 = "()"
s2 = "()[]{}"
s3 = "(]"

print(Solution().isValidParentheses(s1))
print(Solution().isValidParentheses(s2))
print(Solution().isValidParentheses(s3))


""" 
Simplify Path
Given a string path, which is an absolute path (starting with a slash '/) to a file or directory in a unix-style file system, convert it to the simplified canonical-path.

Canonical path should have the following format:
The path start with a single '/',
Any two directories are separated by a single slash '/'.
The path does not end with a trailling '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
"""

class SolutionStackPath:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = [] 
        for file in path:
            if file == "..":
                if stack: stack.pop()
            elif not file or file == ".":
                continue
            else: 
                stack.append(file)

        return "/"+"/".join(stack)

p="/home/"
p2="/../home/./../"
print(SolutionStackPath().simplifyPath(p))
print(SolutionStackPath().simplifyPath(p2))


""" 
Validate Stack Sequences 

Given two integer arrays pushed and popped, each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

Examples: 
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true 
Explanation:  
push(1), push(2), push(3), push(4),
pop()->4,
push(5),
pop()->5, pop()->3, popp()->2, pop()->1

Input: pushed=[1,2,3,4,5], popped = [4,3,5,1,2]
Output: false 
Explanation: 1 cannot be popped before 2
"""

class SolutionStackSequene():
    def validateStackSequene(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [] 
        for p in pushed:
            stack.append(p)
            while stack and popped and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        return stack==[] and popped==[]


pushed1 = [1,2,3,4,5]
popped1 = [4,5,3,2,1]
pushed2 = [1,2,3,4,5]
popped2 = [4,3,5,1,2]

print(SolutionStackSequene().validateStackSequene(pushed1, popped1))
print(SolutionStackSequene().validateStackSequene(pushed2, popped2))


"""  
Score of Parentheses

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:
"()" has sore 1.
AB has score A+B, where A+B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

Example: 
Input: s = "()"
Output: 1 

Input: s = "(())"
Output = 2  
"""

class SolutionScoreParentheses():
    def scoreOfParentheses(self, s:  str)-> int: 
        sk = [0]

        for ch in s:
            if ch == "(":
                sk.append(0)
            else:
                prev = sk.pop()
                sk[-1] += max(2*prev, 1)
        return sk.pop()

p1 = "()"
p2 = "(())"

print(SolutionScoreParentheses().scoreOfParentheses(p1))
print(SolutionScoreParentheses().scoreOfParentheses(p2))

