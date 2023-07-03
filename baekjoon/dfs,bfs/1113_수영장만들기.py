import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
data = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
res = 0


def bfs(x, y, num):
    global res
    que = deque([(x, y)])
    visited[x][y] = num
    value = data[x][y]
    OUT = 0

    if x == 0 or x == n-1 or y == 0 or y == m-1:
        OUT = 1

    minval = int(1e9)
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if data[nx][ny] <= value and not visited[nx][ny]:
                que.append((nx, ny))
                visited[nx][ny] = num

                if nx == 0 or nx == n-1 or ny == 0 or ny == m-1:
                    OUT = 1
            elif data[nx][ny] > value and not visited[nx][ny]:
                minval = min(minval, data[nx][ny])

    if not OUT: #IN이면
        for i in range(n):
            for j in range(m):
                if visited[i][j] == num:
                    res += minval - value
                    data[i][j] = minval


value = set()
for i in range(n):
    for j in range(m):
        if data[i][j] not in value:
            value.add(data[i][j])
value = sorted(value)

for k in value:
    visited = [[0] * m for _ in range(n)]
    num = 1
    for i in range(n):
        for j in range(m):
            if data[i][j] == k and not visited[i][j]:
                bfs(i, j, num)
                num += 1

print(res)
