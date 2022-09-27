# -*- coding: utf-8 -*-
import sys
n,m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
def binary_search(array, start, end):
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        
        for i in array:
            if i <= mid:
                continue
            cnt += (i - mid)
        if cnt < m:
            end = mid - 1

        elif cnt >= m:
            start = mid + 1
    return end

print(binary_search(data, 1, max(data)))
     