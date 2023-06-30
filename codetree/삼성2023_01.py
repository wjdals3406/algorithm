'''
만약 부서지지 않은 포탑이 1개가 된다면 그 즉시 중지

#공격자 선정
가장 약한 포탑 = 공격자 = 부서지지 않은 포탑 => N+M만큼 공격력 증가
power = [] 공격력
last_attack = [] 가장 최근에 공격한 시점
행과 열의 합 계산해주는 func

공격한지 가장 최근에 공격한 포탑,
행과 열의 합이 가장 큰 포탑,
열 값이 가장 큰 포탑

#2. 공격자의 공격
공격력이 가장 높은 포탑 = 강한 포탑

공격한지 가장 오래된 포탑이 가장 강한 포탑,
행과 열의 합이 가장 작은 포탑,
열 값이 가장 작은 포탑

    #레이저 공격 -> 최단 경로
        [최단 경로 선택] => 우/하/좌/상 순으로 bfs 돌려서 나오는 첫번째 값 get
        최단 경로 여러 개 -> 우/하/좌/상 순으로 먼저 움직인 것이 선택

        [공격]
        최단 경로로 가는 길에 마주한 포탑 -> 공격자 공격력 // 2
        공격 대상 -> 공격력 만큼 피해

    # (최단 경로 없으면) 포탄 공격
        [공격]
        공격자 주위 포탑(인접 8방향) -> 공격자 공격력 // 2
        공격 대상 -> 공격력 만큼 피해

#3. 포탑 부서짐
공격력 0이하 -> 부서짐

#4. 공격을 당하지도, 하지도 않았던 포탑은 공격력 + 1

'''

from collections import deque
import copy
n,m,k = map(int, input().split())
power = [list(map(int, input().split())) for _ in range(n)]
last_attack = [[0] * m for _ in range(n)] #n*m

def find_lowest_power():
    rlist = []
    for i in range(n):
        for j in range(m):
            #공격력, 가장 최근 attack, 행+열, 열, 좌표
            if power[i][j] > 0:
                rlist.append((power[i][j], -last_attack[i][j], -(i+j), -j, i,j))

    rlist.sort()
    return rlist[0][4], rlist[0][5]

def find_highest_power():
    rlist = []
    for i in range(n):
        for j in range(m):
            # 공격력 가장 높은, 가장 오래된 attack, 가장 작은 행+열, 가장 작은 열, 좌표
            if power[i][j] > 0:
                rlist.append((-power[i][j], last_attack[i][j], i + j, j, i, j))

    rlist.sort()
    return rlist[0][4], rlist[0][5]


dir1 = [(0,1), (1,0), (0,-1), (-1,0)] #우/하/좌/상
dir2 = [(0,1), (1,0), (0,-1), (-1,0), #8방향
        (1,-1), (1,1), (-1,1), (-1,-1)]

def layser(sx, sy, ex, ey, case):
    is_attacked_list = [[0] * m for _ in range(n)]
    is_attacked_list[sx][sy], is_attacked_list[ex][ey] = 1, 1
    p = power[sx][sy]
    power[ex][ey] -= p

    for i in range(0, len(case), 2):
        x,y = case[i], case[i+1]
        if (x == attacker_x and y == attacker_y) or (x == attacked_x and y == attacked_y):
            continue
        power[x][y] -= p // 2
        is_attacked_list[x][y] = 1

    return is_attacked_list

rlist = []
def find_short_way(sx,sy,ex,ey):
    que = deque([[[sx,sy], sx,sy]])
    visited = [[0] * m for _ in range(n)]
    visited[sx][sy] = 1

    while que:
        case = que.popleft()
        x,y = case[1], case[2]

        for dx,dy in dir1:
            nx = (x + dx) % n #격자를 벗어나게 되면 반대편으로 이동하게 됨
            ny = (y + dy) % m

            #부서진 포탑이 있는 위치는 지날 수 없음
            if power[nx][ny] <= 0:
                continue

            if not visited[nx][ny]:
                #도착 지점에 도착하면
                if nx == ex and ny == ey:
                    is_attacked_list = layser(sx,sy, ex,ey, case[0])
                    return is_attacked_list

                que.append([case[0] + [nx,ny], nx, ny])
                visited[nx][ny] = 1

    return None


def lose_power():
    p = power[attacker_x][attacker_y]
    power[attacked_x][attacked_y] -= p

    for i in range(n):
        for j in range(m):
            if power[i][j] > 0 and is_attacked_list[i][j] == 1:
                power[i][j] -= (p // 2)


def bomb(sx,sy,ex,ey):
    p = power[sx][sy]
    power[ex][ey] -= p

    for dx,dy in dir2:
        nx = (ex + dx) % n  # 격자를 벗어나게 되면 반대편으로 이동하게 됨
        ny = (ey + dy) % m

        # 부서진 포탑이 있는 위치는 지날 수 없음
        if power[nx][ny] <= 0 or (nx == sx and ny == sy) or (nx == ex and ny == ey):
            continue

        power[nx][ny] -= p//2
        is_attacked_list[nx][ny] = 1

    return is_attacked_list

def clear():
    for i in range(n):
        for j in range(m):
            if power[i][j] > 0 and is_attacked_list[i][j] == 0:
                power[i][j] += 1

def check():
    cnt  = 0
    for i in range(n):
        for j in range(m):
            if power[i][j] > 0:
                cnt += 1

    return cnt

#k번 turn
#부서지지 않은 포탑이 1개가 된다면 그 즉시 중지
for i in range(1,k+1):
    #공격자 선정
    attacker_x, attacker_y = find_lowest_power()

    #공격자 공격
    attacked_x, attacked_y = find_highest_power()

    power[attacker_x][attacker_y] += n + m

    #공격
    last_attack[attacker_x][attacker_y] = i

    #레이저 공격
    is_attacked_list = find_short_way(attacker_x, attacker_y, attacked_x, attacked_y)

    if is_attacked_list == None:
        is_attacked_list = [[0] * m for _ in range(n)]
        is_attacked_list[attacker_x][attacker_y], is_attacked_list[attacked_x][attacked_y] = 1, 1
        bomb(attacker_x, attacker_y, attacked_x, attacked_y)

    # 부서지지 않은 포탑 1개가 되었는지 확인
    if check() == 1:
        break

    #포탑 정비
    clear()


#남아있는 포탑 중 가장 강한 포탑의 공격력을 출력
print(max(map(max, power)))