import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]

visited[0][1][0] = 1  # 가/대/세
for i in range(1, n):
    if data[0][i] == 1:
        break
    else:
        visited[0][i][0] = 1

for i in range(1, n):
    for j in range(2, n):
        if data[i][j] == 0:
            visited[i][j][0] = visited[i][j-1][0] + visited[i][j-1][1]
            visited[i][j][2] = visited[i-1][j][1] + visited[i-1][j][2]

            if data[i-1][j] == 0 and data[i][j-1] == 0:
                visited[i][j][1] = visited[i-1][j-1][0] + \
                    visited[i-1][j-1][1] + visited[i-1][j-1][2]

print(sum(visited[n-1][n-1]))
