# -*- coding: utf-8 -*-
import sys
k = int(sys.stdin.readline())

for _ in range(k):
    n = int(sys.stdin.readline())
    data = sorted([sys.stdin.readline().rstrip() for _ in range(n)])
    flag = 0
    for i in range(len(data)-1): #startswith함수 사용하면 됨
        dlen = len(data[i])
        if data[i] == data[i+1][:dlen]:
            print("NO")
            flag = 1
            break
    if not flag:
        print("YES")