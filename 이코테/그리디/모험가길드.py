# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline())
fear_list = list(map(int,sys.stdin.readline().split()))
fear_list.sort()

#1 1 2 3 3 -> 3
count = 1
result = 0

for i in fear_list:
    if count < i:
        count += 1
    elif i == count:
        count = 1
        result += 1
        
print(result)
    
