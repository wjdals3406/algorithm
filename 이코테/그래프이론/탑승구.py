# -*- coding: utf-8 -*-
import sys
G = int(sys.stdin.readline()) #???
P = int(sys.stdin.readline()) #???

g = [0] * (G+1)
result = 0
for i in range(1, P+1):
    num = int(sys.stdin.readline())
    if g[num] == 0:
        g[num] = i
    else:
        while g[num] != 0:
            num -= 1
        if num <= 0:
            break
        g[num] = i
    result += 1
for j in range(i+1, P+1):
    int(sys.stdin.readline())
    
print(result)

    
    