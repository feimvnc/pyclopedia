# pip install thefuzz
from thefuzz import fuzz, process 

s1 = "Hello world"
s2 = "hello world"

# simple basic match
print(s1 is s2)    # False 
print(s1 == s2)    # False 
print(fuzz.ratio(s1, s2))    # similar, .91

# partial match 
s1 = "Hello World"
s2 = "Hello World and bonjour"
print(fuzz.ratio(s1, s2))   # .61
print(fuzz.partial_ratio(s1, s2))    # 100 full match


# sort tokens 
s1 = "Bonjour  Hello World"
s2 = "World Hello Bonjour"
print(fuzz.ratio(s1, s2))   # .56
print(fuzz.partial_ratio(s1, s2))    # .63
print(fuzz._token_sort_ratio(s1, s2))    # 100.0   

# process
sentences = ["Programming Language", 
            "Native Language", 
            "Hello world", 
            "machine learning", 
            "Artificial Learning"]
print(process.extract("programming", sentences, limit=2))
print(process.extract("language", sentences, limit=2))
print(process.extract("learning", sentences, limit=2))
print(process.extractOne("learning", sentences))

# extract items
books = [ 
    "The python book 1 - beginner",
    "The python book 2 - data science",
    "The python book 3 - neural network",
    "The python book 4 - computer vision",
    "The java book - programming",
    "The nature"
]
print(process.extract("python data science", books, 
    limit=3, scorer=fuzz.token_sort_ratio))

# different order not matter
print(process.extract("science data python", books, 
    limit=3, scorer=fuzz.token_sort_ratio))