from collections import deque


def solution(board):
    n = len(board)
    # 각 칸에서의 최소 비용
    # 방향마다 필요함
    visited = [[[int(1e9)] * 4 for _ in range(n)] for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs():
        que = deque([[1, 0, 0, 0], [3, 0, 0, 0]])
        for i in range(4):
            visited[0][0][i] = 0

        while que:
            bd, x, y, money = que.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                    new = money + (100 if bd == i else 600)

                    if new < visited[nx][ny][i]:
                        visited[nx][ny][i] = new
                        que.append((i, nx, ny, new))

    bfs()
    return min(visited[n-1][n-1])
