import re 

rules = [
    (r'o', r'x'),
    (r'w', r'x'),
]

class Sed:
    def __init__(self, rules) -> None:
        self._rules = [(re.compile(pattern), sub) for pattern, sub in rules]

    def replace(self, data:str) -> str:
        ret = data 
        for regx, repl in self._rules:
            ret = regx.sub(repl, ret)
            return ret 

text = None 

with open('temp.txt') as f:
    s = f.readlines()
    s2 = re.sub(r'hello', 'world', str(s))
    print(s2)
    sed = Sed(rules)
    text = sed.replace(s2)

with open('temp_new.txt', 'w') as f:
    f.writelines(text)
