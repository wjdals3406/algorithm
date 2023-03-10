# # -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
n = int(input())
day = [list(map(int, input().split())) for _ in range(n)] #T, P
dp = [0] * n 

for i in range(n-1,-1,-1):
    if day[i][0] + i > n: #day[i][0] : time
        continue
    
    next = day[i][0] + i
    if len(dp[next:]) == 0: #next는 마지막날
        dp[i] = day[i][1]
    else:
        dp[i] = max(dp[next:]) + day[i][1]

print(max(dp))
        
# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]
# dp = [0]*(n+5)
# for i in range(n-1, -1, -1):
#     if i+data[i][0] <= n:
#         dp[i] = max(dp[i+data[i][0]]+data[i][1], dp[i+1])
#     else:
#         dp[i] = dp[i+1]
# print(max(dp))
        