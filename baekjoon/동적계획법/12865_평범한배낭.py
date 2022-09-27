import sys
n,k = map(int, sys.stdin.readline().split())
dp = [0] * (k+1)
for _ in range(n):
    w,v = map(int, sys.stdin.readline().split())
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i-w] + v, dp[i])
print(dp[-1])

 
