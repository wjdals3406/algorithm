import sys
from collections import deque
n, m, k = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = int(1e9)


def bfs():
    global answer
    # k 저장
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = k
    que = deque([(0, 0, k, 1)])

    while que:
        x, y, broke, cnt = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 해당 좌표까지 방문했을 때의 k의 잔여량보다 현재 k 잔여량이 더 높으면 방문함
            if visited[nx][ny] < broke:
                if data[nx][ny] == 1:
                    if broke - 1 < 0:
                        continue
                    if visited[nx][ny] == broke - 1:
                        continue
                    visited[nx][ny] = broke - 1
                    que.append((nx, ny, broke - 1, cnt + 1))
                else:
                    visited[nx][ny] = broke
                    que.append((nx, ny, broke, cnt + 1))

                if nx == n-1 and ny == m-1:
                    answer = cnt + 1
                    return


bfs()
if n == 1 and m == 1:
    if data[0][0] == 0 or (data[0][0] == 1 and k >= 1):
        print(1)
else:
    print(answer) if answer < int(1e9) else print(-1)
