#CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기 구하기
import sys
from itertools import product
n,m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dir_dic = {1:[[(0,1)], [(0,-1)], [(1,0)], [(-1,0)]],
           2:[[(0,1), (0,-1)], [(-1,0), (1,0)]],
           3:[[(-1,0), (0,1)], [(0,1), (1,0)], [(1,0), (0,-1)], [(0,-1), (-1,0)]],
           4:[[(0,-1), (1,0), (-1,0)],
                 [(0,1), (1,0), (-1,0)],
                 [(0,1), (0,-1), (-1,0)],
                 [(0,1), (0,-1), (1,0)]
            ],
           5:[[(0,1), (0,-1), (1,0), (-1,0)]]}


dlist = []
for i in range(n):
    for j in range(m):
        if 0 < data[i][j] < 6:
            dlist.append((i,j))

def count():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                cnt += 1
    return cnt

def dfs(idx):
    global res
    if idx == len(dlist):
        res = min(res, count())
        return

    x,y = dlist[idx]
    cnum = data[x][y]
    for case in dir_dic[cnum]:
        #하나의 case
        for dx,dy in case:
            nx, ny = x + dx, y + dy
            while 0 <= nx < n and 0 <= ny < m and data[nx][ny] != 6:
                if 0 < data[nx][ny] < 6:
                    nx += dx
                    ny += dy
                    continue
                data[nx][ny] -= 1
                nx += dx
                ny += dy

        dfs(idx+1)

        for dx,dy in case:
            nx, ny = x + dx, y + dy
            while 0 <= nx < n and 0 <= ny < m and data[nx][ny] != 6:
                if 0 < data[nx][ny] < 6:
                    nx += dx
                    ny += dy
                    continue
                data[nx][ny] += 1
                nx += dx
                ny += dy

res = int(1e9)
dfs(0)
print(res)