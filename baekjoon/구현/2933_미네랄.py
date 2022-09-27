# -*- coding: utf-8 -*-
#'.'는 빈 칸, 'x'는 미네랄
#왼 -> 오, 오 -> 왼 순으로 던짐, 짝수 인덱스 : 왼쪽에서 던지는 경우, 홀수 인덱스 : 오른쪽에서 던지는 경우
# 미네랄
import sys
from collections import deque
r,c = map(int, sys.stdin.readline().split())
data = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
n = int(sys.stdin.readline())
height = list(map(int, sys.stdin.readline().split()))
height = list(map(lambda x : x-1, height)) #인덱스 0부터 시작하기 위해 -1씩 해줌
dx = [-1,1,0,0] #왼, 오, 아래 확인/ 위에 있는지 확인X
dy = [0,0,-1,1]

def bfs(x,y,num): 
    if visited[x][y] > 0:
        return False
    que = deque([[x,y]])
    flag = 0
    while que:
        x,y = que.popleft()
        visited[x][y] = num
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=r or ny < 0 or ny >=c:
                continue
            if data[nx][ny] == 'x' and not visited[nx][ny] : #방문하지 않았을 때
                que.append([nx,ny])
            if nx == r-1: #바닥에 미네랄이 존재 -> 파괴가 안됨
                flag = 1
    if flag : 
        return False
    return True # 바닥에 미네랄이 존재하지 않음 -> 파괴됨

def drop_mineral(x,y): 
    value = visited[x][y]
    vlist = []
    for j in range(c): 
        for i in range(r):
            if data[i][j] == 'x' and visited[i][j] == value:
                vlist.append((i,j))
                data[i][j] = '.'
                #i가 젤 큰 것 찾기
    vlist.sort(key = lambda x : -x[0])
    nx, ny = vlist[0]
    cnt = 0
    nx += 1
    while nx < r and data[nx][ny] == '.':
        cnt += 1
        nx += 1
    for nx,ny in vlist:
        data[nx+cnt][ny] = 'x'
        
def checkDownCnt(fallLst, check):
    downCnt, flag = 1, 0      # downCnt 크기 1씩 늘려가며
    while True:
        for r, c in fallLst:
            if r+downCnt == R-1:        # 땅을 만나거나
                flag = 1
                break
            if cave[r+downCnt+1][c] == 'x' and check[r+downCnt+1][c]:   # 다른 미네랄 만나면
                flag = 1
                break
        if flag:    # 그 때가 떨어질 수 있는 최대 downCnt 값
            break
        downCnt += 1
    return downCnt
                                
for xindex, x in enumerate(height): #왼쪽에서 던질건지, 오른쪽에서 던질건지
    if xindex % 2 == 0:
        check = range(c)
    else:
        check = range(c-1, -1, -1)
        
    x = r-x-1
    for y in check: #그 행에 미네랄이 아예 없을 수도 있음
        if data[x][y] == 'x': #미네랄이면
            data[x][y] = '.' #미네랄 파괴
            cnt = 0
            mlist = []
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >=r or ny < 0 or ny >=c:
                    continue
                if data[nx][ny] == 'x':
                    cnt += 1
                    mlist.append((nx,ny))
            if cnt == 2: #미네랄이 2개가 맞닾아 있었을 때 미네랄이 파괴되는 가능성이 존재
                visited = [[0] * c for _ in range(r)]
                for index in range(cnt):
                    nx,ny = mlist[index]
                    if bfs(nx,ny,index+1): #떨어뜨림
                        downCnt = checkDownCnt(fallLst, check)

                        # 5단계 - 미네랄 떨어질 위치 동굴에 그리기
                        for mr, mc in minerals:
                            data[mr+downCnt][mc] = "x"
                        # drop_mineral(nx,ny) 
                        break
            break
res = ''
for i in data:
    res += ''.join(i)
    res += '\n'
print(res)
