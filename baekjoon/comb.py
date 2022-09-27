# -*- coding: utf-8 -*-
#12865를 조합으로 풀었을 때
import sys
n,k = map(int, sys.stdin.readline().split())
data = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
data.sort(key = lambda x : x[0])
maxval = 0

def gen_combinations(arr, n):
    result =[] 

    if n == 0: 
        return [[]]

    for i in range(0, len(arr)): 
        elem = arr[i]
        rest_arr = arr[i + 1:] 
        for C in gen_combinations(rest_arr, n-1): 
            if sum(map(lambda x: x[0], [elem]+C)) > k:
                break
            
            result.append([elem]+C) 
            
    return result

for i in range(1, n+1):
    for j in gen_combinations(data, i):
        vsum = sum(map(lambda x: x[1], j))
        maxval = max(maxval, vsum)
print(maxval)
    