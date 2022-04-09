# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
money = list(map(int,sys.stdin.readline().split()))
money.sort()

d = [0] * sum(money)

for i in money:
    
    

# for i in range(sum(money)):
#     if i in list(set(money)):
#         continue
    
#     for j in money:
#         i = i - j
#         if i <=0: 
#             break
    
    