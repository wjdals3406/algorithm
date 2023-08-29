import sys
n, m, x, y, k = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
move = list(map(int, sys.stdin.readline().split()))
dir = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
# 이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력
# 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며,
# 출력도 하면 안 된다.

dice = [0, 0, 0, 0, 0, 0]


def turn(dir):
    if dir == 1:  # 좌
        dice[1], dice[2], dice[3], dice[4], dice[5] = dice[5], dice[1], dice[2], dice[4], dice[3]
    elif dir == 2:  # 우
        dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[3], dice[5], dice[4], dice[1]
    elif dir == 3:  # 위
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[4], dice[3], dice[5], dice[0]
    else:  # 아
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[-1], dice[1], dice[0], dice[3], dice[2], dice[4]


for d in move:
    nx, ny = x+dir[d][0], y+dir[d][1]
    if 0 <= nx < n and 0 <= ny < m:
        turn(d)
        if data[nx][ny] == 0:
            data[nx][ny] = dice[-1]  # 맨 뒤의 수
        elif data[nx][ny] != 0:
            dice[-1] = data[nx][ny]
            data[nx][ny] = 0
        print(dice[2])
        x, y = nx, ny
