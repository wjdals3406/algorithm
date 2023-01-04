# -*- coding: utf-8 -*-
import sys
n,d,k,c = map(int,sys.stdin.readline().split()) #접시의 수,초밥의 가짓수,연속해서 먹는 접시의 수,쿠폰 번호
data = [int(sys.stdin.readline()) for _ in range(n)] 
data = data * 2

s,e = 0,k
maxval = 0
for i in range(n):
    check = data[s:e]
    check_set = list(set(check))
    
    if c in check: #쿠폰 초밥 존재
        maxval = max(maxval, len(check_set))
    else:
        maxval = max(maxval, len(check_set)+1)
        if len(check) == len(check_set): #겹치는 종류가 없고, 쿠폰 초밥 존재하지 않을 때 -> 무조건 최댓값
            break
    s += 1
    e += 1
print(maxval)
    
        
    