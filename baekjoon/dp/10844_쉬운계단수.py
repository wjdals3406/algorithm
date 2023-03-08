n = int(input())

dp = [[0]*10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1
    
for i in range(2,n+1):
    for j in range(10):
        if j== 0:
            dp[i][j] = dp[i-1][1]
        elif j==9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] #직관적으로 식을 이해할 수 있는 방법이 무엇일까

print(sum(dp[n])%1000000000)