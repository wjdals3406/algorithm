import sys
n = int(sys.stdin.readline())
# 마지막 돌을 가져간 사람이 짐 -> 마지막 돌을 가져간 사람이 이기는 줄..^^
# 각 게임횟수-> 누가 이겼는지를 나타냄
# 1: WIN 0: LOSE
dp = [0] * 1001
dp[2] = 1

for i in range(4, n+1):
    # 상근이가 이기는 경우가 있으면 상근이가 이기도록
    minval = min(dp[i-1], dp[i-3], dp[i-4])
    dp[i] = 0 if minval == 1 else 1
print("SK" if dp[n] == 1 else "CY")
