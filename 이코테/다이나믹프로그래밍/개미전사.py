# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
store = list(map(int,sys.stdin.readline().split()))

d = [0] * 101

d[1] = store[0]
d[2] = max(store[0], store[1]) 
for i in range(3, n+1):
    d[i] = max(d[i - 1], d[i - 2] + store[i - 1])
    
print(max(d))
    



#0번째 
#1번쨰 