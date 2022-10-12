# -*- coding: utf-8 -*-
#i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si이다. 위치 (r, c)는 r행 c열을 의미
# K번 명령한 후, 남아있는 파이어볼 질량의 합을 출력
#행열 1부터 n까지
import sys
from collections import deque
n,m,k = map(int, sys.stdin.readline().split())
data = list(deque([[] for _ in range(n+1)]) for _ in range(n+1)) #nxn 배열 생성
dx = [-1,1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
ball = deque()
for _ in range(m):
    ball_info = deque(map(int, sys.stdin.readline().split()))
    x,y = ball_info[0], ball_info[1]
    data[x][y].append(ball_info)
    ball.append(deque([x,y]))

def move():
    #모든 파이어볼 이동
    ball_len = len(ball)
    for _ in range(ball_len):
        x,y = ball.popleft()
        data_len = len(data[x][y])
        for _ in range(data_len):
            ri, ci, mi, si, di = data[x][y].pop()
            nx = (ri + (dx[di]) * si) % n
            ny = (ci + (dy[di]) * si) % n
            data[nx][ny].append(deque([nx, ny, mi, si, di]))
            if deque([nx, ny]) not in ball:
                ball.append(deque([nx, ny]))

def divide_ball():
    for x in range(1,n+1):
        for y in range(1,n+1):
            if len(data[x][y]) >= 2:
                M,S = 0,0
                even, odd = 1,1
                for ri, ci, mi, si, di in data[x][y]:
                    M += mi
                    S += si
                    if di % 2 != 0 : #모두 짝수가 아니면 -> even값이 1이면 값이 모두 짝수임
                        even = 0
                    elif di % 2 == 0:#모두 홀수가 아니면
                        odd = 0

                M = M // 5
                S = S // len(data[x][y])
                if M == 0: #볼 소멸
                    data[x][y] = deque()
                    ball.remove(deque([x,y]))
                    continue

                if (even and not odd) or (odd and not even): #값이 모두 짝수거나 홀수
                    D = [0, 2, 4, 6]
                else:
                    D = [1, 3, 5, 7]
                data[x][y] = deque([[x,y,M,S,D[i]] for i in range(4)])

for _ in range(k):
    move()
    divide_ball()

total = 0
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for i in data[x][y]:
            total += i[2]
print(total)

