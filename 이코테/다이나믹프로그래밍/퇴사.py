# -*- coding: utf-8 -*-

import sys
n = int(input())
T = [] # 상담을 완료하는데 걸리는 기간
P = [] # 상담 이후 받을 수 있는 금액
dp = [0] * (n+1) #현재 일자까지의 최대 이익
max_value = 0

for _ in range(n):
    t, p = list(map(int,sys.stdin.readline().split()))
    T.append(t) 
    P.append(p) 
    
for i in range(n-1, -1, -1):
    time = T[i] + i
    
    #상담이 기간 안에 끝나는 경우
    if time <= n:
        dp[i] = max(P[i] + dp[time], max_value)
        max_value = dp[i] #dp 중에서의 max값
    
    else:
        dp[i] = max_value
        
print(dp)