#1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지
#0은 빈칸이고, 0이 아닌 수 x는 x번 상어가 들어있는 칸
#1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽
import sys
from collections import deque
n,m,k = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] #상어가 들어있는 배열, data[i][j]값은 상어 번호
shark_direction = list(map(int, sys.stdin.readline().split())) #1부터 m번 까지의 상어의 방향 / shark[i]는 i+1번의 상어의 방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]

sdrank = []
for _ in range(m): #각 상어의 방향 우선순위가 상어 당 4줄씩
    sdrank.append([list(map(int, sys.stdin.readline().split())) for _ in range(4)])

shark = deque()
for i in range(n):
    for j in range(n):
        if data[i][j] > 0:
            shark.append([i,j, data[i][j]]) #상어 위치한 좌표와 상어 번호
            data[i][j] = [data[i][j],k]

smell_time = [[0] * n for _ in range(n)]
def update_smell():
    for i in range(n):
        for j in range(n):
            if data[i][j] != 0:
                data[i][j][1] -= 1 #data[i][j][0]은 상어 번호, data[i][j][1]은 냄새 초
                if data[i][j][1] == 0:
                    data[i][j] = 0

def move_shark():
    #인접한 칸 중 아무 냄새가 없는 칸으로 먼저 이동, 그런 칸들이 많을 때는 우선순위에 따라 진행
    #그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 이동

    #이동한 곳에 상어가 이미 있다면 번호가 작은 것만 남기고 큰 번호는 없애기
    shark_move = []
    while shark:
        smell, shark_smell, = [],[]
        x,y,snum = shark.popleft()
        for i in range(4): #처음부터 우선순위대로 포문을 돌리면 됨
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >=n:
                continue
            if data[nx][ny] == 0:  #아무 냄새가 없는 칸
                smell.append([nx,ny])
            if data[nx][ny] and data[nx][ny][0] == snum:
                shark_smell.append([nx,ny])

        if not smell:#그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 이동 / 마지막에 상어 한거번에 이동시킴
            nx,ny,snum = priority(shark_smell, snum, x, y) #이동할 좌표와 바뀐 방향
        else:
            nx,ny,snum = priority(smell, snum, x, y)
        shark_move.append([nx, ny, snum])

    update_smell()
    while shark_move:
        x, y, snum = shark_move.popleft()
        if data[x][y] != 0 :
        data[x][y] = [snum,k]
        shark.append([x,y,snum])

def priority(board, snum, x, y): #우선순위 따라 방향을 지정해줌
    srank = sdrank[snum-1]
    dir = shark_direction[snum-1]
    for i in srank[dir]:
        nx = x + dx[i-1]
        ny = y + dy[i-1]
        if [nx,ny] in board:
            shark_dir = i+1
            shark_direction[snum - 1] = shark_dir #shark 현재 방향 바꿈
            return nx, ny, snum



#상어가 겹칠 때 해결 안해놨음
time= 0
while True:
    move_shark()
    time += 1










