# -*- coding: utf-8 -*-
n = int(input())
dp = [x for x in range (n+1)]

for i in range(1,n+1):
    for j in range(1, i):
        if i < j**2:
            break
        if dp[i] > dp[i-j**2] + 1:
            dp[i] = dp[i-j**2] + 1
print(dp[n])


#시간초과
# dp = [n] * (n+1)
# dp[1] = 1
# for i in range(2,n+1):
#     if i**2 <= n: 
#         dp[i**2] = 1
        
#     for j in range(1, i):
#         if dp[i] > (dp[j] + dp[i-j]):
#             dp[i] = dp[j] + dp[i-j]

# print(dp[n])