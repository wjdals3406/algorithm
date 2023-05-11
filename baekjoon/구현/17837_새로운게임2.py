import sys
n, k = map(int, sys.stdin.readline().split())
#0은 흰색, 1은 빨간색, 2는 파란색
color = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
data = [[[] for _ in range(n)] for _ in range(n)] #보드판 위의 말 번호
horse = [] #말의 위치와 방향 
for i in range(k):
    r,c,d = map(int, sys.stdin.readline().split())
    data[r-1][c-1].append(i)
    horse.append([r-1, c-1, d])
    
dir = {1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)}

def horse_change(color,x,y,nx,ny):
    idx = data[x][y].index(i)
    move_list = data[x][y][idx:]
    
    #data 변경
    data[x][y] = data[x][y][:idx]
    
    if color == 1: #빨간색
        #순서 반대
        move_list.reverse()
    data[nx][ny].extend(move_list)
    if len(data[nx][ny]) >= 4:
        return 1
    
    #horse 변경
    for midx in move_list:
        horse[midx][0], horse[midx][1] = nx, ny
    
    return 0

cnt = 1
flag = 0
while True:
    for i in range(k):
        x,y,d = horse[i]
        nx, ny = x + dir[d][0], y + dir[d][1]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or color[nx][ny] == 2:
            if d % 2 == 0:
                d = d - 1
            else:
                d = d + 1
                    
            horse[i][2] = d #방향 반대로
            nx, ny = x + dir[d][0], y + dir[d][1]
            
            if 0 <= nx < n and 0 <= ny < n and color[nx][ny] < 2 :
                if horse_change(color[nx][ny],x,y,nx,ny):
                    flag = 1
                    break
        
        else :
            #흰 색
            if color[nx][ny] == 0:
                if horse_change(0,x,y,nx,ny):
                    flag = 1
                    break
                    
            #빨간색
            elif color[nx][ny] == 1:
                if horse_change(1,x,y,nx,ny):
                    flag = 1
                    break
            
    if flag:
        print(cnt)
        break
    
    cnt += 1
    
    if cnt > 1000:
        print(-1)
        break
