# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

b = [[0,0] for _ in range(n*n+1)]
[(key, sum+=val) for key,val in b.items()]

for i in range(1,n+1):
    for j in range(i, n+1):
        val = i*j
        if i == j:
            b[val][0] += 1
        else:
            b[val][0] += 2
        
sum = 0
for i in range(1,n+1):
    for j in range(i, n+1):
        val = i*j
        sum += b[val][0]
        b[val][1] = sum
            

def binary_search(array, start, end):
    while start <= end :
        mid = (start + end) // 2
        if array[mid][1] == k:
            return mid
        elif array[mid][1] < k:
            start = mid + 1
        elif array[mid][1] > k:
            end = mid - 1
    return end

start, end = 0, n*n
print(binary_search(b, start, end))

