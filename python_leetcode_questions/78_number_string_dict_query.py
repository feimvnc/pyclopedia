""" 
Given an query of digit string and digit to char mapping,
return query's result.

Input: 
query: ["2","3","4"]
dict: ["a", "abc", "de", "fg"]
Output: [2, 2, 0]
Explanation: 
"a", "abc", map to "2" on phone number pad
"de", "fg", map to "3" on phone number pad  
no dict value map to "4", thus 0
"""

class TrieNode:
    def __init__(self):   # init 
        self.children = {}    # dict 
        self.isWord = False   
        self.prefixCount = 0 

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
            now.prefixCount += 1 
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

    def getNumberPrefix(self, word):
        now = self.root 
        for i in range(len(word)):
            ch = word[i]
            if ch not in now.children:
                return 0 
            now = now.children[ch]
        return now.prefixCount


class Solution: 

    def stringtoNum(self, string, letterToNum):
        num = "" 
        for i in range(len(string)):
            ch = string[i]
            num += str(letterToNum[ord(ch) - ord('a')])
        return num 

    def letterCombinationsII(self, queries, dictionary):
        # conver a-z to numbers based on phone number pad 
        trie = Trie() 
        letterToNum = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
        for word in dictionary:
            trie.insert(self.stringtoNum(word, letterToNum))
            # print(self.stringtoNum(word, letterToNum))
        result = []
        for word in queries:
            result.append(trie.getNumberPrefix(word))

        return result   
        

query = ["2","3","4"]
dict_ = ["a", "abc", "de", "fg"]
print(Solution().letterCombinationsII(query, dict_))   # -> [2, 2, 0]
