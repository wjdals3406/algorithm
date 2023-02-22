# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split())) #카드가 i개 포함된 카드팩의 가격은 Pi원
card = [0] + card
dp = card[:] #i번째 값은, i번째까지의 최댓값

# for i in range(1,n+1):
#     for j in range(i,n+1, i):
#         dp[j] = max(card[i] * (j//i), dp[j])

for i in range(2,n+1):
    for j in range(1,i//2+1):
        dp[i] = max(dp[j] + dp[i-j], dp[i])

print(dp[-1])
        
    

