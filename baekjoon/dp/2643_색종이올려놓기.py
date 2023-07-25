import sys
n = int(sys.stdin.readline())
# 두 번째 원소가 크도록
paper = [sorted(list(map(int, sys.stdin.readline().split())))
         for _ in range(n)]

# 두 번쨰 원소를 기준으로 sort -> 첫 번째 원소를 기준으로 가장 긴 증가하는 부분 수열 찾기
paper.sort(key=lambda x: (x[1], x[0]))
print(paper)
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if paper[i][0] >= paper[j][0]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
