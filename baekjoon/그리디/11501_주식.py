# -*- coding: utf-8 -*-
#���� �տ������� ���� Ȯ���Ϸ��ؼ� ��ư� �ٰ����µ�, �ڿ������� ���� Ȯ���ص� �ȴٴ� ���� �����ϱ�!
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
        # data = data[sidx+1:] #�̰� �ð� ���� �ɸ�
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