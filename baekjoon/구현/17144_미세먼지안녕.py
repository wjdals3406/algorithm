import sys
#rxc / t초
r,c,t = map(int, sys.stdin.readline().split())
dust = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
dir_list = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dx = [0,0,-1,0,1]
dy = [0,1,0,-1,0]

#1:오 2:위 3:왼 4:아
clean_board = [[0] * c for _ in range(r)]
def left(i,j):
    x,y = i,j
    # while y < c - 1:
    #     clean_board[x][y] = 1
    #     y += 1
    # while x > 0:
    #     clean_board[x][y] = 2
    #     x -= 1
    # while y > 0:
    #     clean_board[x][y] = 3
    #     y -= 1
    # while clean_board[x][y] != -1:
    #     clean_board[x][y] = 4
    #     x += 1

    for d in range(4):
        while 0 <= x < r and 0 <= y < c and dust[x][y] != -1:
            clean_board[x][y] = d + 1
            x, y = x + dir_list[d][0], y + dir_list[d][1]
        x, y = x - dir_list[d][0], y - dir_list[d][1]

def right(i,j):
    x,y = i,j
    # while y < c - 1:
    #     clean_board[x][y] = 1
    #     y += 1
    # while x < r - 1:
    #     clean_board[x][y] = 4
    #     x += 1
    # while y > 0:
    #     clean_board[x][y] = 3
    #     y -= 1
    # while clean_board[x][y] != -1:
    #     clean_board[x][y] = 2
    #     x -= 1

    for d in [1,4,3,2]:
        while 0 <= x < r and 0 <= y < c and dust[x][y] != -1:
            clean_board[x][y] = d
            x, y = x + dir_list[d-1][0], y + dir_list[d-1][1]
        x, y = x - dir_list[d-1][0], y - dir_list[d-1][1]


robot_x, robot_y = 0,0
flag = 0
for i in range(r):
    for j in range(c):
        if dust[i][j] == -1:
            robot_x, robot_y = i,j
            clean_board[i][j] = -1
            clean_board[i+1][j] = -1
            left(i,j+1)
            right(i+1,j+1)
            flag = 1
            break
    if flag:
        break

def spread_dust():
    dcopy = [[0] * c for _ in range(r)]
    dcopy[robot_x][robot_y] = -1
    dcopy[robot_x+1][robot_y] = -1
    for x in range(r):
        for y in range(c):
            if dust[x][y] > 0:
                cnt = 0
                amount = dust[x][y] // 5
                for i in range(1,5):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < r and 0 <= ny < c and dust[nx][ny] != -1:
                        cnt += 1
                        dcopy[nx][ny] += amount

                dcopy[x][y] += (dust[x][y] - amount * cnt)

    return dcopy

def clean():
    dcopy = [[0] * c for _ in range(r)]
    dcopy[robot_x][robot_y] = -1
    dcopy[robot_x + 1][robot_y] = -1
    for i in range(r):
        for j in range(c):
            if clean_board[i][j] > 0 and dust[i][j] > 0:
                d = clean_board[i][j]
                nx = i + dx[d]
                ny = j + dy[d]
                if dust[nx][ny] == -1:
                    continue
                dcopy[nx][ny] += dust[i][j]
            elif dust[i][j] > 0:
                dcopy[i][j] += dust[i][j]

    return dcopy

def cal_dust():
    total = 0
    for i in range(r):
        for j in range(c):
            if dust[i][j] > 0:
                total += dust[i][j]
    print(total)

for _ in range(t):
    dust = spread_dust()
    dust = clean()
cal_dust()

