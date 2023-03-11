# -*- coding: utf-8 -*-
import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = data[0][0]
    dp[1][0] = data[1][0]
    
    #열 단위로 이동
    #이전 열에 있는 값을 기준으로 이동
    for j in range(1,n):
        for i in range(2):
            if i == 0:
                dp[i][j] = max(dp[i+1][j-1] + data[i][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j-1] + data[i][j], dp[i][j-1])
    
    print(max(dp[0][n-1], dp[1][n-1]))
                  
                