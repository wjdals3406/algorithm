import sys
from collections import deque
m, n, k = list(map(int, sys.stdin.readline().split()))
rec = [list(map(int, sys.stdin.readline().split())) for i in range(k)]
data = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for x1, y1, x2, y2 in rec:
    for r in range(y2-y1):
        for c in range(x2-x1):
            data[m-y2+r][x1+c] = 1


def bfs(i, j):
    res = 1
    visited[i][j] = 1
    que = deque([[i, j]])

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and data[nx][ny] == 0:
                que.append((nx, ny))
                visited[nx][ny] = 1
                res += 1
    return res


cnt = 0
block = []
for i in range(m):
    for j in range(n):
        if not visited[i][j] and data[i][j] == 0:
            block.append(bfs(i, j))
            cnt += 1
print(cnt)
print(*sorted(block))
