def missing_number(arr, n):
    # use a fomula 
    sum1 = n * (n +1) // 2
    sum2 = sum(arr)
    missing = sum1 - sum2 
    return missing

print(missing_number([1,2,3,4,6], 6))
