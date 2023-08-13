""" 
Write a function to check whether an input string is a valid IPv4 or IPv6 address or neither.

IPv4
172.16.254.1    -> valid 
172.16.254.01   -> invalid 

IPv6: 
8 groups of 4 hexadecimal digits, 
each group representting 16 bits, separated by ":",
2001:0db8:85a3:0000:0000:8a2e:0370:7334   -> valid 
2001:db8:85a3:0000:0000:8A2E:0370:7334   -> valid  (omit leading zero and using upper case)
"2001:db8::0000:0000:8A2E:0370:7334"     -> invalid, don't replace two zeros with ::

A useful website to test regex functions and string match
https://regex101.com/

"""
import re 

class Solution:
    def  __init__(self):
        self.IPv4Pattern = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$')
        self.IPv6Pattern = re.compile(r'^(([0-9a-fA-F]{1,4}\:){7}([0-9a-fA-F]{1,4}))$') 

    def validIPAddress(self, IP: str) -> str:
        if self.IPv4Pattern.match(IP):
            return "IPv4"
        elif self.IPv6Pattern.match(IP):
            return "IPv6"
        else: 
            return 'Neither'

    # another option for IPv4
    def validIPv4_2(self, IP: str) -> str: 
        a = IP.split('.')
        if len(a)!=4:
            return 'Neither'
        for i in a:
            if (int(i)<=0 and int(i)>=255) or i.startswith('0'):
                return 'Neither'
        return 'IPv4'

    
    # another option for IPv6
    def validIPv6_2(self, IP: str) -> str: 

        def checkHexRange(c: str) ->bool:
            h = [str(i) for i in range(0,10)]
            h += [ i for i in 'abcdefABCDEFs']
            if c in h:
                return True 
            return False 

        a = IP.split(':')
        if len(a)!=8: 
            return 'Neither'
        for i in a:
            for ch in i:
                if not checkHexRange(ch):
                    return 'Neither'
        return "IPv6"
    

a1 = "172.16.254.1"
a2 = "172.16.254.01"
a3="2001:0db8:85a3:0000:0000:8a2e:0370:7334"
a4="2001:db8:85a3:0000:0000:8A2E:0370:7334"
a5="2001:db8:85a3::8A2E:0370:7334"

print(Solution().validIPAddress(a1))
print(Solution().validIPAddress(a2))
print(Solution().validIPAddress(a3))
print(Solution().validIPAddress(a4))
print(Solution().validIPAddress(a5))

print(Solution().validIPv4_2(a1))
print(Solution().validIPv4_2(a2))

print(Solution().validIPv6_2(a4))
print(Solution().validIPv6_2(a5))

