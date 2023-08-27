class Solution: 
    def additiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            for j in range(i+1, n):
                num1 = num[:i]
                num2 = num[i:j]
                if (num1[0]=='0' and i<j) or (num2[0] == '0' and j-i>1):
                    continue 
                while j < n:  
                    num3 = str(int(num1) + int(num2))
                    if not num.startswith(num3, j):
                        break 
                    j += len(num3)
                    num1, num2 = num2, num3 
                
                if j == n:
                    return True 
        return False 


print(Solution().additiveNumber('199100199299'))