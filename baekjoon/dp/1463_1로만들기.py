n = int(input())
dp = [x-1 for x in range(n+1)]

for i in range(2,n+1):
    if i % 3 == 0:
        dp[i] = min(dp[i//3] + 1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i//2] + 1, dp[i])
    if (i-1) % 2 == 0:
        dp[i] = min(dp[(i-1)//2] + 2, dp[i])
    if (i-1) % 3 == 0:
        dp[i] = min(dp[(i-1)//3] + 2, dp[i])
    
    dp[i] = min(dp[i-1]+1, dp[i])
    
print(dp[n])

#개선 코드
# n = int(input())
# d = [0] * (n + 1)

# for i in range(2, n + 1):
#     d[i] = d[i - 1] + 1
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)	
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
# print(d[n])