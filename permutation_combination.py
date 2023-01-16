def permutation(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for rest in permutation(arr[:i] + arr[i+1:], n - 1):
            result.append([elem] + rest)
    return result
    
def combination(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result


def another(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in another(array[i:], r-1):
                yield [array[i]] + next

# print(combination([0,1,2,3], 2))
# print(permutation([0,1,2,3], 2))
another([0,1,2,3], 4)