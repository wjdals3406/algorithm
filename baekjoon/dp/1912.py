# -*- coding: utf-8 -*-
import sys
#이전까지의 합이, 그냥 i번째 숫자보다 작은 경우 이전의 기록들은 무의미
# i번째 데이터 이전까지 합을 계산해 봤을 때 최대값을 지속적으로 기록
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
dp[0] = data[0]
for i in range(1,n):
    dp[i] = max(dp[i-1] + data[i], data[i]) 
#맨 처음에 max(dp[i-1] + data[i], dp[i-1])이라고 생각했음
print(max(dp))
