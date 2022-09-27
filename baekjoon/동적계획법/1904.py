import sys
n = int(sys.stdin.readline())
dp = [0] * 1000001 #왜 n+1로 하면 인덱스에러나지..?
dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746
print(dp[n])