import sys
from collections import deque
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
data = [[0] * (n+1) for _ in range(n+1)]
data[1][1] = 1
#먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
#만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
#만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
#게임이 몇 초에 끝나는지
for _ in range(k):
    x,y = map(int, sys.stdin.readline().split())
    data[x][y] = 2 #사과

L = int(sys.stdin.readline())
dir = deque([sys.stdin.readline().split() for _ in range(L)]) #초, 방향
dx = [-1,0,1,0] #북,동,남,서
dy = [0,1,0,-1]

time = 0
snake = deque([[1,1]])
d = 1
while True:
    x,y = snake[0]
    if dir and time == int(dir[0][0]):
        _, direction = dir.popleft()
        if direction == 'L':
            d = ((d-1) + 4) % 4
        else:
            d = (d + 1) % 4

    x = x + dx[d] #뱀 이동
    y = y + dy[d]
    snake.appendleft([x,y])
    time += 1

    if x <=0 or x > n or y <=0 or y > n: #벽 또는 자기 자신과 부딪히면 게임이 끝남
        break
    if data[x][y] == 1:
        break
    if data[x][y] == 2:#사과가 있으면
        data[x][y] = 0
    else:#사과가 없으면
        rr,rc = snake.pop()
        data[rr][rc] = 0

    data[x][y] = 1


print(time)


