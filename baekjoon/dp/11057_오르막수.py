n = int(input())
dp = [[1] * 10 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
print(dp[n][9] % 10007)