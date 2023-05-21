from random import choices 

one = [i for i in range(5, 55, 5)]
two = choices(one, k=len(one))
three = choices(one, k=len(one))

file = 'test_data.csv'
with open(file, 'w') as f:
    f.write('one,two,three'+'\n')
    for i in range(len(one)): 
        f.write(f'{one[i]},{two[i]},{three[i]}\n')

with open(file, 'r') as f:
    print(f.readlines())


'''

['one,two,three\n', '5,35,30\n', '10,45,40\n', '15,30,20\n', '20,5,20\n', '25,25,35\n', '30,50,35\n', '35,20,25\n', '40,15,25\n', '45,45,45\n', '50,50,40\n']


##
one,two,three
5,35,10
10,20,50
15,45,40
20,50,5
25,5,15
30,35,50
35,15,50
40,15,5
45,20,30
50,50,40
'''
