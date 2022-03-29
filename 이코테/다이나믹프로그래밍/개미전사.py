# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
store = list(map(int,sys.stdin.readline().split()))

j=0
sum = 0
for i in store:
    j = j+2
    sum += i

#0번째 
#1번쨰 