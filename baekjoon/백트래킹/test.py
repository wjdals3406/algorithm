def gen_combinations(arr, n):
    result =[] 

    if n == 0: 
        return [[]]

    for i in range(0, len(arr)): 
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        for C in gen_combinations(rest_arr, n-1): 
            result.append([elem]+C) 
              
    return result
gen_combinations([1,2,3,4], 2)