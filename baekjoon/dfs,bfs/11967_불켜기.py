# 한 번 이동할 때 상화좌우 인접한 곳 탐색 -> 불이 켜져 있는 방으로 이동
import sys
from collections import defaultdict, deque
n, m = map(int, sys.stdin.readline().split())
dic = defaultdict(list)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
light = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
for _ in range(m):
    x, y, a, b = map(int, sys.stdin.readline().split())
    dic[(x-1, y-1)].append((a-1, b-1))


def is_reachable(sx, sy, ex, ey):
    reachable = [[0] * n for _ in range(n)]
    reachable[sx][sy] = 1
    que = deque([[sx, sy]])

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not reachable[nx][ny] and light[nx][ny]:
                    reachable[nx][ny] = 1
                    que.append((nx, ny))
                    if (nx, ny) == (ex, ey):
                        return 1

    return 0


def bfs():
    light[0][0] = 1
    visited[0][0] = 1
    que = deque([[0, 0]])
    cnt = 1
    while que:
        x, y = que.popleft()

        for nx, ny in dic[(x, y)]:
            # 불을 아직 안켰으면 켜기
            if not light[nx][ny]:
                light[nx][ny] = 1
                cnt += 1

            if not visited[nx][ny] and is_reachable(x, y, nx, ny):
                visited[nx][ny] = 1
                que.append((nx, ny))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if light[nx][ny] and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = 1

    print(cnt)


bfs()
