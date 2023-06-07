import sys
from collections import deque
import copy
n,m,t = map(int, sys.stdin.readline().split())
data = [deque(map(int, sys.stdin.readline().split())) for _ in range(n)]
turn_list = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]

#di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향
def turn_right(x,k):
    for i in range(x, n+1, x):
        data[i-1].rotate(k)

def turn_left(x,k):
    for i in range(x, n+1, x):
        data[i-1].rotate(-k)

def check_is_same():
    tmp = copy.deepcopy(data)
    flag,sumval,count = 0,0,0
    for i in range(n):
        sumval += sum(data[i])
        for j in range(m):
            if data[i][j] > 0:
                count += 1

            if data[i][j] != 0 and data[i][j] == data[i][(j+1)%m]:
                flag = 1
                tmp[i][j] = 0
                tmp[i][(j+1)%m] = 0

            if i < n -1 and data[i][j] != 0 and data[i][j] == data[i+1][j]:
                flag = 1
                tmp[i][j] = 0
                tmp[i+1][j] = 0

    if not flag and sumval > 0:
        avg = sumval / count
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 0:
                    continue
                if tmp[i][j] > avg:
                    tmp[i][j] -= 1
                elif tmp[i][j] < avg:
                    tmp[i][j] += 1
    return tmp

for x, d, k in turn_list:
    if d == 0:
        turn_right(x, k)
    else:
        turn_left(x,k)
    data = check_is_same()
print(sum(map(sum, data)))