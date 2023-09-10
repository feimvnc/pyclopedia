"""
Given a string, the task is to remove duplicates from it.
Expected time complexity O(n) where n is length of input string and extra space O(1)
under the assumption that there are total 256 possible characters in a string.
"""

class Solution:

    def found_dup(self, curr_str: str, rev_str: str) -> bool:
        return curr_str in rev_str

    def remove_dup(self, s: str) -> str:
        l = list(s)
        # abca   -> acba 
        for i in reversed(range(len(s))):    # remove from back 
            # if l[i] in l[:i]:
            #     del l[i]
            if self.found_dup(l[i], l[:i]):   # check current char against chars till_here
                del l[i]
        return ''.join(l)


s = "abca"
s1 = 'hello'
print(Solution().remove_dup(s))   # -> abc
print(Solution().remove_dup(s1))  # -> helo 
