# # -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
n = int(input())
data = [int(input()) for _ in range(n)]
dp = [0] * n
for i in range(n):
    if i == 0:
        dp[i] = data[0]
    elif i == 1:
        dp[i] = data[0] + data[1]
    else:
        dp[i] = max(dp[i-2] + data[i], dp[i-1], dp[i-3] + data[i-1] + data[i]) 
        #3번째에 i-3값이 -1이 나오긴 하지만, dp[-1] = 0이라 어짜피 상관없음

print(dp[-1])