# 배열을 넘기지 말고 인덱스를 넘기자
import sys
data = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
row = [[0] * 10 for _ in range(9)]
col = [[0] * 10 for _ in range(9)]
div = [[[0] * 10 for _ in range(3)] for _ in range(3)]
coord = []
for i in range(9):
    for j in range(9):
        num = data[i][j]
        if num == 0:
            coord.append((i, j))
            continue
        r, c = i//3, j//3
        div[r][c][num] = 1
        row[i][num] = 1
        col[j][num] = 1


def dfs(idx):
    if idx == len(coord):
        for i in data:
            print(*i)
        exit()

    x, y = coord[idx]
    for i in range(1, 10):
        r, c = x//3, y//3
        if row[x][i] == 0 and col[y][i] == 0 and div[r][c][i] == 0:
            row[x][i] = col[y][i] = div[r][c][i] = 1
            data[x][y] = i
            dfs(idx+1)
            row[x][i] = col[y][i] = div[r][c][i] = 0
            data[x][y] = 0


dfs(0)
