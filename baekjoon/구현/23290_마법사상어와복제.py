from itertools import product
import copy

m, s = map(int, input().split())
fish = [[[] for _ in range(5)] for _ in range(5)]
shark_smell = [[0] * 5 for _ in range(5)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for _ in range(m):
    x,y,d = map(int, input().split())
    fish[x][y].append(d-1)
sx,sy = map(int, input().split())
# 상은 1, 좌는 2, 하는 3, 우는 4로 변환
sdir = {1: (-1, 0), 2: (0, -1), 3: (1, 0), 4: (0, 1)}
sdir_list = list(product(range(1,5), repeat=3))
origin = copy.deepcopy(fish)

def fish_move():
    #한 번에 이동
    move_list = []
    for x in range(1, 5):
        for y in range(1, 5):
            if fish[x][y]: #물고기가 있다면
                #물고기 이동
                for i in range(len(fish[x][y])):
                    d = fish[x][y][i]
                    flag = 0
                    for _ in range(8):
                        nx,ny = x + dx[d], y + dy[d]
                        #격자 밖으로 벗어나지 않고, 냄새랑 상어가 없을 때
                        if 1 <= nx <= 4 and 1 <= ny <= 4 and shark_smell[nx][ny] == 0 and (sx != nx or sy != ny):
                            move_list.append((nx,ny,d))
                            flag = 1
                            break
                        else:
                            d = (d - 1) % 8
                    if not flag:
                        move_list.append((x,y,d))
                fish[x][y] = []

    for x,y,d in move_list:
        fish[x][y].append(d)

def shark_move():
    global sx, sy
    rvisit = []
    res = -1
    x,y = sx,sy

    #생선 있을 곳을 리스트에 넣어두고 마지막에 update
    for case in sdir_list:
        visited = []
        flag = 0
        cnt = 0
        nx,ny = sx,sy
        for i in case:
            nx, ny = nx + sdir[i][0], ny + sdir[i][1]
            if 1 <= nx <= 4 and 1 <= ny <= 4:
                if len(fish[nx][ny]) > 0 and (nx,ny) not in visited:
                    cnt += len(fish[nx][ny])
                    visited.append((nx,ny))
            else:
                flag = 1
                break

        if not flag and cnt > res:
            res = cnt
            rvisit = visited
            x, y = nx, ny

    sx, sy = x, y

    for i,j in rvisit:
        fish[i][j] = []
        shark_smell[i][j]=3

def remove_smell():
    for i in range(1, 5):
        for j in range(1, 5):
            if shark_smell[i][j] > 0:
                shark_smell[i][j] -= 1

def copy_fish():
    global fish
    for i in range(1, 5):
        for j in range(1, 5):
            if fish[i][j]:
                origin[i][j].extend(fish[i][j])
    fish = copy.deepcopy(origin)

for _ in range(s):
    fish_move()
    shark_move()
    remove_smell()
    copy_fish()

answer = 0
for i in range(1, 5):
    for j in range(1, 5):
        if fish[i][j]:
            answer += len(fish[i][j])

print(answer)