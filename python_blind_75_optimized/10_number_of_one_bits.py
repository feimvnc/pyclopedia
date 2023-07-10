""" 
Write a function that takes an unsigned integer and returns the number of '1'
bits it has (also known as the Hamming weight).

Input: n = 000000000001011
Output: 3

Explanation: The input binary string
000000000000000000000000000000001011 has a total of there '1' bits
"""

import numpy as np 

class Solution:
    def number_of_one_bits(self, n: int) -> int:
        # convert not to binary string 
        s = np.binary_repr(n)
        print(s)
        # convert to int array 
        ss = np.array(list(s), dtype='i')

        # get the count of nonzero item
        return np.count_nonzero(ss)

s = Solution()
print(s.number_of_one_bits(10))

print(s.number_of_one_bits(127))


""" 
$ python 10_number_of_one_bits.py 
1010
2
1111111
7

"""