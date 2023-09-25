""" 
Evaluate reverse polish notation, for expression is "number, number, operator".

Example: 
input: tokens = ["2", "1", "+", "3", "*"]
output: 9
"""

from typing import List


class Solution(object):
    def evaluate_rpn(self, tokens: List[str]) -> int:
        stack = []
        OP_SIGN = ("+", "-", "*", "/")
        for token in tokens:
            if token not in OP_SIGN:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                else:
                    if first * second < 0:
                        stack.append(-abs(first) // abs(second))
                    else:
                        stack.append(first // second)
        return stack.pop()


print(Solution().evaluate_rpn(["2", "1", "+", "3", "*"]))  # -> 9
print(Solution().evaluate_rpn(["4", "13", "5", "/", "+"]))  # -> 6
