# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
#총 소요시간 : 2시간 35분

#상어 : 1 이상 M 이하의 자연수 번호


#1.맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다
#2.1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다
#3.냄새는 상어가 k번 이동하고 나면 사라진다.

#[이동 방향 설정]
#아무 냄새가 없는 칸의 방향으로 잡는다. / 아무 냄새가 없는 칸 중, 우선순위가 높은 칸으로 이동
#그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
#자신의 냄새가 있는 칸이 여러 칸일 경우, 우선순위를 따름

#이동 완료 후, 한 칸에 여러 마리 상어가 있으면, 가장 작은 번호를 제외하고 모두 격자 밖으로 쫓겨남
#1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지 구하기

#nxn / m개 상어, k번 이동(냄새)
input = sys.stdin.readline
n,m,k = map(int,input().split())
shark_loc = [list(map(int,input().split())) for _ in range(n)] #상어가 있는 위치
dx = [0,-1,1,0,0] #위, 아래, 왼쪽, 오른쪽
dy = [0,0,0,-1,1]

for i in range(n):
    for j in range(n):
        if shark_loc[i][j] == 0:
            shark_loc[i][j] = []
        else:
            snum = shark_loc[i][j]
            shark_loc[i][j] = [snum]

shark_cur_dir = [0]
shark_cur_dir.extend(list(map(int,input().split())))

shark_dir_prior = defaultdict(list) #상어의 방향 우선순위
for i in range(1,m+1):
    shark_dir_prior[i].append(0)
    for _ in range(4):
        d = [0]
        d.extend(list(map(int,input().split())))
        shark_dir_prior[i].append(d)
        # shark_dir_prior[i].append(list(map(int,input().split())))
        
smell = [[[0,0] for _ in range(n)] for _ in range(n)] #상어번호, 냄새 지속 시간
def spread_smell(): #모든 상어가 자신의 위치에 자신의 냄새를 뿌린다
    for i in range(n):
        for j in range(n):
            if len(shark_loc[i][j]) > 0:
                smell[i][j][0] = shark_loc[i][j][0]
                smell[i][j][1] = k
            
def move(): #1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동 / 한꺼번에 이동해야 함
    smove = []
    for i in range(n):
        for j in range(n):
            if len(shark_loc[i][j]) > 0:
                snum = shark_loc[i][j][0] #상어 넘버
                sdir = shark_cur_dir[snum] #상어 현재 방향
                
                #본인의 냄새가 있는 곳 체크하기
                my_smell = 0
                flag = 1
                flag2 = 1
                for d in range(1,5):
                    nd = shark_dir_prior[snum][sdir][d] #새롭게 이동할 방향
                    nx = i + dx[nd]
                    ny = j + dy[nd]
                    
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    
                    if smell[nx][ny][0] == 0: #아무 냄새가 없으면 이동
                        smove.append([nx,ny,shark_loc[i][j][0]])
                        # shark_loc[nx][ny].extend(shark_loc[i][j])
                        shark_loc[i][j] = []
                        shark_cur_dir[snum] = nd
                        flag2 = 0
                        break
                    
                    elif smell[nx][ny][0] == snum and flag: #본인의 냄새가 있는 곳이라면
                        flag = 0 #맨 첫번째로 들어오는 것만 체크해야 하기 때문
                        my_smell = (nx,ny,nd)
                        
                if not flag2:
                    continue
                if flag == 0:
                    nx,ny,shark_cur_dir[snum] = my_smell[0], my_smell[1], my_smell[2]
                    smove.append([nx,ny,shark_loc[i][j][0]])
                    # shark_loc[nx][ny].extend(shark_loc[i][j])
                    shark_loc[i][j] = []
    
    for x,y,snum in smove:
        shark_loc[x][y].append(snum)
                        
def check():
    for i in range(n):
        for j in range(n):
            if len(shark_loc[i][j]) > 0:
                shark_loc[i][j].sort()
                shark_loc[i][j] = [shark_loc[i][j][0]]
                    

def shark_num():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if len(shark_loc[i][j]) > 0:
                cnt += 1
    return cnt #이 값이 1이면 True, 아니면 False


def decrease_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if smell[i][j][1] == 0:
                smell[i][j][0] = 0

time = 0
while time <= 1000: #이부분에서 tie < 1000으로 해줘서 틀렸었다,,
    spread_smell()
    move()
    check()
    time += 1
    decrease_smell()
    
    if shark_num() == 1:
        break

if time > 1000:
    print(-1)
else: print(time)
        