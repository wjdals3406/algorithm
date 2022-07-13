# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = data[0][0]
    
for r in range(1, n):
    for c in range(0, r+1):
        if c==0:
            dp[r][c] = dp[r-1][c] +  data[r][c]
        elif c==r:
            dp[r][c] = dp[r-1][c-1] +  data[r][c]
        else:
            dp[r][c] = max(dp[r-1][c], dp[r-1][c-1]) + data[r][c]
result = -1
for i in range(n):
    result = max(result, dp[n-1][i])
    
print(result)            