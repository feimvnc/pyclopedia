'''
input: num= [2,7,11,15]
target: target = 99
output: [0, 1], nums[0] + num[1] = 9
'''

def two_sum(arr, target):
    for i in arr:
        if target - i in arr:
            return [arr.index(i), arr.index(target-i)]

print(two_sum([2,7,11,15], 9))
