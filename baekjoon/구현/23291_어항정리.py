import copy
import sys
from collections import deque
sys.stdin = open("sample_input.txt", "r")
n,k = map(int, input().split())
data = deque(map(int, input().split()))
dx = [0,1]
dy = [1,0]
#어항 N개, 물고기 한 마리 이상

#1. 물고기 수가 가장 적은 어항에 물고기 한 마리 넣기
#만약 그러한 게 여러개라면 모두 한 마리씩 넣기
def add_fish():
    f = []
    minval = int(1e9)
    for i in range(n):
        if minval > data[i]:
            minval = data[i]
            f = [i]
        elif minval == data[i]:
            f.append(i)
    for i in f:
        data[i] += 1

def stack_port():
    global data
    pre = deque([data.popleft()]) + deque([0]) * (n-2)
    data = deque([pre, data])

#2개 이상 쌓여 있는 어항 시계방향으로 90도 회전 / 가장 오른쪽 어항 아래에 어항이 있을때까지 반복
def turn_right(data):
    #전체를 오른쪽으로 회전
    r,c = len(data), len(data[0])
    new = deque(deque([0]) * r for _ in range(c))
    for i in range(r):
        for j in range(c):
            new[j][r-i-1] = data[i][j]
    return new
def remake_port(data):
    turn_data, origin = deque(), deque()
    while data:
        row = data.popleft()
        if row[1] != 0:
            turn_data.append(row)
        else:
            origin.append(row[0])
    turn_data.append(origin)

    if len(turn_data[-1]) < len(turn_data[0]):
        return -1, 0

    for i in range(len(turn_data)-1):
        turn_data[i] = turn_data[i] + deque([0]) * (len(turn_data[-1]) - len(turn_data[i]))
    return 1, turn_data

def adjust_fish_num():
    r, c = len(data), len(data[0])
    new = copy.deepcopy(data)

    for x in range(r):
        for y in range(c):
            if data[x][y] == 0: continue
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if data[nx][ny] == 0: continue
                    if data[x][y] > data[nx][ny]:
                        d = (data[x][y] - data[nx][ny]) // 5
                        if d > 0:
                            new[nx][ny] += d
                            new[x][y] -= d
                    else:
                        d = (data[nx][ny] - data[x][y]) // 5
                        if d > 0:
                            new[nx][ny] -= d
                            new[x][y] += d
    return new

def make_one_row():
    r, c = len(data), len(data[0])
    new = deque()
    for j in range(c):
        i = r-1
        while i >= 0 and data[i][j] > 0:
            new.append(data[i][j])
            i -= 1
    return new

def turn_180_remake():
    global data
    r = n
    data = deque([data])
    for _ in range(2):
        turn_data, origin = deque(), deque()
        for i in range(len(data)):
            data[i] = list(data[i])
            turn_data.append(data[i][:r//2])
            origin.append(data[i][r//2:])
        turn_data = turn_right(turn_data)
        turn_data = turn_right(turn_data)
        turn_data.extend(origin)
        data = turn_data
        r = r // 2

def check():
    if max(data) - min(data) <= k:
        return 0
    return 1

cnt = 0
while check():
    add_fish()
    stack_port()
    while True:
        new = turn_right(data)
        is_available, new = remake_port(new)
        if is_available == -1:
            break
        data = new
    #물고기 조절 작업
    data = adjust_fish_num()
    data = make_one_row()
    turn_180_remake()
    data = adjust_fish_num()
    data = make_one_row()
    cnt += 1
print(cnt)

#deque은 slice가 안됨
#행렬 회전할 때 zip을 이용해 다음과 같이 회전 가능
# def rotated(array_2d):
#     list_of_tuples = zip(*array_2d[::-1])
#     return [list(e) for e in list_of_tuples]
