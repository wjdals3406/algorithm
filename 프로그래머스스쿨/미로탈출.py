from collections import deque
# 레버를 눌러야 이동 가능


def solution(maps):
    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n, m = len(maps), len(maps[0])

    # 시작 지점 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                sx, sy = i, j
            elif maps[i][j] == "L":
                lx, ly = i, j
            elif maps[i][j] == "E":
                ex, ey = i, j

    def find(sx, sy):
        que = deque([[sx, sy, 0]])
        visited = [[0] * m for _ in range(n)]
        while que:
            x, y, cnt = que.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == "L" and not visited[nx][ny]:
                        return cnt + 1
                    elif maps[nx][ny] != "X" and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        que.append([nx, ny, cnt+1])
        return -1

    def bfs(sx, sy):
        que = deque([[sx, sy, 0]])
        visited = [[0] * m for _ in range(n)]
        while que:
            x, y, cnt = que.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    # 레버 당기고 도착점에 도착하면
                    if maps[nx][ny] == "E":
                        return cnt + 1

                    elif not visited[nx][ny] and maps[nx][ny] != "X":
                        visited[nx][ny] = 1
                        que.append((nx, ny, cnt+1))
        return -1

    le_time = find(sx, sy)
    arr_time = bfs(lx, ly)
    if le_time == -1 or arr_time == -1:
        return -1
    else:
        return le_time + arr_time
