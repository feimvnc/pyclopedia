# a small program for object ref count, strong reference, weak reference 
# useful for object memory usage check and garbage monitoring

import ctypes 

def ref_count(address):
    return ctypes.c_long.from_address(address).value 

class Person:
    def __init__(self, name):
        self.name = name 

    def __repr__(self, name):
        return f'Person(name={name})' 

p1 = Person('Guido')
p2 = p1 

print(p1 is p2)
print(f'p1 = {id(p1)}, p2 = {id(p2)}')

print(f'ref_count = {ref_count(id(p1))}')

del p1 

# strong reference
print(f'ref_count = {ref_count(id(p2))}')
print(f'p2 = {id(p2)}')

