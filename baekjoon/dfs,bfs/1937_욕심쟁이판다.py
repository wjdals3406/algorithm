# bfs로 하면 시간초과남 -> 이미 방문한 지점이어도 값이 update되면 다시 새롭게 방문해야 하기 때문
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if visited[x][y]:
        return visited[x][y]
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if data[x][y] < data[nx][ny]:
                visited[x][y] = max(visited[x][y], dfs(nx, ny) + 1)
    return visited[x][y]


for i in range(n):
    for j in range(n):
        dfs(i, j)

print(max(map(max, visited)))
