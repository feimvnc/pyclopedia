"""
Your task is to implement the function strstr.
The function takes two strings as arguments (s,x) and
locates the occurrence of the string x in the string s.
The function returns and integer denoting the first occurrence of the
string x in s (0 based indexing).
"""

class Solution:

    def str_str(self, s: str, p: str) -> int:
        try: 
            res = s.index(p)
        except: 
            res = -1 
        return res 
   

s = 'hello' 
p = 'lo'
print(Solution().str_str(s, p))
print(Solution().str_str_dict(s, p))


""" 
python 90_find_str_idx_in_str.py 
3
{'h': 0, 'e': 1, 'l': 3, 'o': 4}
3
l
"""