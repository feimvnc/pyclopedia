class Solution:
    def interpret(self, command: str)->str:
        return command.replace("()", "o").replace("(al)", "al").replace("G", "G")

    def interpret2(self, command: str)->str:
        replacements = [("()", "o"), ("(al)", "al")]
        for a, b in replacements:
            res = command.replace(a, b) 
            command = res # needed updated command
        return res 

print(Solution().interpret("G()(al)"))
print(Solution().interpret2("G()(al)"))
