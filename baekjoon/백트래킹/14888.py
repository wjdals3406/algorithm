# -*- coding: utf-8 -*-
# 백트래킹은 모든 가능한 경우의 수 중에서 특정한 조건을 만족하는 경우만 살펴보는 것
# DFS 등으로 모든 경우의 수를 탐색하는 과정에서, 
# 조건문 등을 걸어 답이 절대로 될 수 없는 상황을 정의하고, 
# 그러한 상황일 경우에는 탐색을 중지시킨 뒤 
# 그 이전으로 돌아가서 다시 다른 경우를 탐색하게끔 구현
import sys
from itertools import permutations
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
calculate = list(map(int, sys.stdin.readline().split()))
clist = []
for i in range(4):
    for j in range(calculate[i]):
        clist.append(i)
ccom = list(set(permutations(clist, n-1)))
maxval = -int(1e9)
minval = int(1e9)
for i in ccom:
    sum = data[0]
    for j in range(n-1):
        if i[j] == 0:
            sum += data[j+1]
        elif i[j] == 1:
            sum -= data[j+1]
        elif i[j] == 2:
            sum *= data[j+1]
        elif i[j] == 3:
            if sum < 0:
                sum = -(abs(sum) // data[j+1])
            else:
                sum //= data[j+1]
    maxval = max(maxval, sum)
    minval = min(minval, sum)
    
print(maxval)
print(minval)   
    