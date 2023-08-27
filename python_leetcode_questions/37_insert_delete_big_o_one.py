from random import sample 

class Solution:
    def __init__(self):
        self.myset = set()
    
    def insert(self, val:int)->bool:
        if val not in self.myset:
            self.myset.add(val)
            return True 
        return False 
    
    def remove(self, val: int)->bool:
        if val in self.myset:
            self.myset.remove(val)
            return True 
        return False 

    def getRandom(self)->int:
        return sample(self.myset, 1)[0]
          