# -*- coding: utf-8 -*-
#나는 앞에서부터 값을 확인하려해서 어렵게 다가갔는데, 뒤에서부터 값을 확인해도 된다는 것을 생각하기!
import sys
k = int(sys.stdin.readline())
from collections import deque
for _ in range(k):
    n = int(sys.stdin.readline())
    data = deque(map(int, sys.stdin.readline().split()))
    data_sort = sorted(data, reverse=True)
    res = 0
    for i in data_sort:
        if i not in data:
            continue
        sidx = data.index(i) 
        if sidx > 0:
            value = data[sidx]
            for j in range(sidx):
                res += value - data[0]
                data.popleft()
        data.popleft()
        # data = data[sidx+1:] #이게 시간 많이 걸림
        if not data:
            break
    print(res)
    
# from sys import stdin
# n = int(stdin.readline())

# for i in range(n):
#     result = 0
#     count = int(stdin.readline())
#     numberList = list(map(int, stdin.readline().split()))

#     temp = numberList[-1]
#     for i in range(len(numberList) - 1, -1, -1):
#         if numberList[i] > temp:
#             temp = numberList[i]
#         else:
#             result += temp - numberList[i]

#     print(result)