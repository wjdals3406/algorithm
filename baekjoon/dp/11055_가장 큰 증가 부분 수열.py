# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dp = [0] * n # i번째 인덱스값은 합의 최솟값이어야 함
# A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 

def check(index):
    pre = index
    for j in range(index+1, n):
        if data[j] > data[pre]:
            dp[j] = max(dp[j], dp[pre] + data[j])


for i in range(n):
    dp[i] = max(dp[i], data[i])
    if i < n-1:
        check(i)
    
print(max(dp))