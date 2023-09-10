"""
Given an string in roman no format (s)  your task is to convert it to integer .Given an string in roman no format (s)
your task is to convert it to integer .
"""

class Roman:
    ROMANS= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'D': 500, 'M':1000}

class Solution: 

    def normalize(self, s: str) -> str:
        cleaned = ''
        for elem in s:
            if elem.upper() in Roman.ROMANS:   # convert to upper case 
                cleaned += elem

        # use map to clean up input 
        # s2 = ''.join(map(lambda x: x if x in Roman.ROMANS else '', s))
        # print(s2)

        return cleaned

    def check_value(self, char: str):
        # print(char,char in Roman.ROMANS ) -> M True
        return char.upper() in Roman.ROMANS

    def roman_to_int(self, s: str) -> int:
        if not s:
            return 0 

        s = self.normalize(s)
        print("cleaned data", s)
        R = Roman.ROMANS
        N = len(s)

        result = R[s[-1]]   # add last value first 

        for i in range(N - 1):   # compute rest 
            # V I I
            # 0 1 2
            if R[s[i]] >= R[s[i+1]] and self.check_value(s[i]):
                result += R[s[i]]
            else:
                result -= R[s[i]]

        return result 

print(Solution().roman_to_int('VII'))   # -> 7
print(Solution().roman_to_int('MDLVII'))   # -> 1557


""" 
python 89_roman_to_int.py 
cleaned data VII
7
cleaned data MDLVII
1557
"""