class TrieNode:
    def __init__(self):   # init 
        self.children = {}    # dict 
        self.isWord = False  


class Trie:
    def __init__(self):
        self.root = TrieNode()   # root node 

    def insert(self, word):
        now = self.root 
        for ch in word:
            if ch not in now.children:
                now.children[ch] = TrieNode()  # create new node 
                print(now.children[ch])
            now = now.children[ch]
            

            
        now.isWord = True 

    def search(self, word):
        now = self.root 
        for ch in word:
            if ch not in now.children:
                return False 
            now = now.children[ch]
        return now.isWord

    def startsWith(self, prefix):
        now = self.root 
        for ch in prefix:
            if ch not in now.children:
                return False 
            now = now.children[ch]
        return True


t = Trie()
print(t.insert("hello"))
print(t.search("hello"))  # -> True
print(t.startsWith("world"))  #-> False
