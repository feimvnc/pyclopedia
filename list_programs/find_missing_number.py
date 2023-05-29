def missing_number(arr, n):
    a = set(arr)
    b = set([i for i in range(1, n+1)])
    return list((b - a))[0]

print(missing_number([1,2,3,4,6], 6))
