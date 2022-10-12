# -*- coding: utf-8 -*-
import sys
k,n = map(int, sys.stdin.readline().split())
data = [int(sys.stdin.readline()) for _ in range(k)]
def binary_search(array, start, end):
    maxval = -1
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        
        for i in array:
            cnt += (i // mid)
        if cnt < n:
            end = mid - 1

        elif cnt >= n:
            start = mid + 1
            maxval = max(maxval, mid)
    return maxval

print(binary_search(data, 1, max(data)))
     