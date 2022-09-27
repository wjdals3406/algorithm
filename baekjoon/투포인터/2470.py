# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

# 양수만 있거나 음수만 있을 때
if data[0] * data[-1] >= 0:
    if data[0] >= 0:
        print(data[0], data[1])
    elif data[0] < 0:
        print(data[-2], data[-1])
# 양수, 음수 모두 존재할 때
else:
    s,e = 0,n-1
    re = int(100000e9)
    a,b = 0,0
    
    while s < e: # s랑 e가 하나 떨어져 있을 때 ex) 1,2,3,4,5
        cur = abs(data[s] + data[e]) 
        if e - s == 1:
            if re > cur:
                re = cur
                a,b = data[s], data[e]
            break
        else:
            next = abs(data[s] + data[e-1])
            if cur <= next:
                if re > cur:
                    re = cur
                    a,b = data[s], data[e]
                s += 1
            elif cur > next:
                e -= 1
    print(a,b)
        