""" 
Given a string of integers and operators +, -, *, /.
Calculate and return the result.

Input: s = "3+2*2"
Output: 7

Input: s = " 3/2"
Output: 1

Use stack to keep track the numbers and operations.
"""

class Solution: 
    def calculate(self, s: str) -> int:
        size = len(s)    # size is used in the loop 
        stack = []     # used to store numbers and ops 
        op = '+'    # default operation, when multiple numbers in stack 
        index = 0    # track current position 

        while index < size: 
            if s[index] == ' ':    # take care of empty char case 
                index += 1
                continue 
            if s[index].isdigit():
                num = ord(s[index]) - ord('0')
                while index+1 < size and s[index+1].isdigit():    # contiguous nums found 
                    index+=1     # move index 1 step forward
                    num = 10*num + ord(s[index]) - ord('0')    # prev num*10 + current  
                if op == '+':
                    stack.append(num)    # append num for later sum 
                elif op == '-':
                    stack.append(-num)    # append negative num 
                elif op == '*':
                    top = stack.pop()    # pop last number, op with current number
                    stack.append(top * num) 
                elif op == "/":
                    top = stack.pop()    # same as *
                    stack.append(int(top/num))   
            elif s[index] in '+-*/':
                op = s[index]
            index += 1 

        return sum(stack)    # last sum up numbers in the stack 


s1 = "3+2*2"
s2 = " 3/2"

print(s1)
print(Solution().calculate(s1))
print(s2)
print(Solution().calculate(s2))

# python 52_basic_calculator_stack.py 
# 3+2*2
# 7
#  3/2
# 1
