""" 
Given a positive integer, output its complement number. 
The complement strategy is to flip the bits of its binary representation.

Example: 
Input: 5 
Output: 2 
Explanation: 5 in binary is 101, 2 in binary is 010
"""

class Solution:
    def findComplement(self, num: int) -> int:
        binary = list("{:b}".format(num))    # convert int to binary str, to list for mutable
        for i in range(len(binary)):
            if binary[i] == "1":   # check binary list value, flip 
                binary[i] = "0"
            else:
                binary[i] = "1"
        return int("".join(binary), base=2)     # default is base=10, so use base=2


print(Solution().findComplement(5))
print(Solution().findComplement(1))
