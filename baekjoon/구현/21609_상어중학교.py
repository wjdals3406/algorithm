#블록은 검은색 블록, 무지개 블록, 일반 블록
#일반 블록: M가지 색상이 있고, 색은 M이하의 자연수로 표현
#일반 블록 적어도 하나 이상, 일반 블록의 색은 모두 같아야 함
#검은색 블록: -1 / 있으면 안됨
#무지개 블록: 0

#인접한 칸: 상하좌우 거리가 1인 두 칸 (r1, c1)과 (r2, c2)
#격자에 중력이 작용하면 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동

import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(num,i,j):
    que = deque([[i,j]])
    cnt,rainbow = 1,0
    visited[i][j] = num
    rm = [[i,j]]
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if (visited[nx][ny] != num and data[nx][ny] == 0) or (not visited[nx][ny] and data[nx][ny] == num):
                cnt += 1
                que.append((nx,ny))
                rm.append((nx,ny))
                visited[nx][ny] = num
                if data[nx][ny] == 0:
                    rainbow += 1
    if cnt <= 1:
        return None,None,None
    
    return cnt, rainbow, rm

def find_BigBlock_group():
    global score
    blist = []
    for i in range(n):
        for j in range(n):
            if data[i][j] > 0 and not visited[i][j]: #이부분에서 data[i][j] > -1 했더니 시간초과 났다..^^
                cnt, rainbow, rm = bfs(data[i][j], i,j)
                if cnt == None:
                    continue
                blist.append((cnt, rainbow, i,j, rm))
                
    blist.sort(key = lambda x : (-x[0], -x[1], -x[2], -x[3]))
    
    if len(blist) == 0:
        return 0
    
    score += blist[0][0] ** 2
    
    for x,y in blist[0][-1]: #2단계
        data[x][y] = -2
    return 1
    
                    
def move():
    for j in range(n):
        for i in range(n-1,-1,-1):
            if data[i][j] >= 0:
                idx = i
                while idx + 1 <= n-1 and data[idx+1][j] == -2: #다음칸이 빈칸이면 이동
                    idx += 1
                
                data[idx][j], data[i][j] = data[i][j], data[idx][j] #내려오기
                     
def turn_left_90():
    new_data = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_data[i][j] = data[j][n-1-i]
            
    return new_data
    

#블록 그룹이 존재하는 동안 계속해서 반복
score = 0
visited = [[0] * n for _ in range(n)]
while find_BigBlock_group():
    move() #3단계
    data = turn_left_90() #4단계
    move() #5단계
    visited = [[0] * n for _ in range(n)]

print(score)