# 마법벽을 피해 (N,M) 위치에 있는 공주님을 구출
# 한 칸 이동하는 데 한 시간
import sys
from collections import deque
n, m, t = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = "Fail"


def bfs():
    # (x, y, 그람을 얻었는지 유무, 시간)
    global answer
    visited_exist = [[0] * m for _ in range(n)]
    visited_not_exist = [[0] * m for _ in range(n)]
    visited_exist[0][0] = visited_not_exist[0][0] = 1
    is_exist = 1 if data[0][0] == 2 else 0
    que = deque([(0, 0, is_exist, 0)])

    while que:
        x, y, check, time = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if nx == n - 1 and ny == m - 1:
                answer = time + 1
                return

            if check == 0 and data[nx][ny] != 1:
                if not visited_not_exist[nx][ny] and time < t:
                    if data[nx][ny] == 2:
                        que.append((nx, ny, 1, time + 1))
                    else:
                        que.append((nx, ny, check, time + 1))
                    visited_not_exist[nx][ny] = 1

            if check == 1:
                if not visited_exist[nx][ny] and time < t:
                    que.append((nx, ny, 1, time + 1))
                    visited_exist[nx][ny] = 1


bfs()
print(answer)
