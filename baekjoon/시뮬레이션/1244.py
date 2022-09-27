# -*- coding: utf-8 -*-
import sys
k = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
s = int(sys.stdin.readline())
for _ in range(s):
    gen,num = map(int, sys.stdin.readline().split()) # 남학생 : 1, 여학생 : 2
    if gen == 1: #남학생
        for i in range(1, k // num+1):
            index = i * num - 1
            if data[index] == 0:
                data[index] = 1  
            else:
                data[index] = 0
    else: #여학생
        s,e = num - 1, num - 1
        while data[s] == data[e]:
            if data[s] == 0:
                data[s] = 1  
                data[e] = 1  
            else:
                data[s] = 0
                data[e] = 0
            s -= 1
            e += 1
            if s < 0 or e >= k:
                break
            
for i in range(1, k+1):
    print(data[i-1], end = " ")
    if i % 20 == 0 :
        print()