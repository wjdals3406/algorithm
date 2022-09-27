# -*- coding: utf-8 -*-
#키로거랑 비슷한 문제
import sys
import heapq
n = int(sys.stdin.readline())
left = []
right = []
result = ''

for i in range(n):
    k = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left, -k)
    else:
        heapq.heappush(right, k)
    if len(left) > 0 and len(right) > 0 and -left[0] > right[0]:
        while -left[0] > right[0]:
            heapq.heappush(right, -heapq.heappop(left))
            heapq.heappush(left, -heapq.heappop(right))
        
    result += str(-left[0]) + '\n'

print(result)
