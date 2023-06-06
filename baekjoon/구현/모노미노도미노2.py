import copy
import sys
'''
행이나 열이 타일로 가득찬 경우와 연한 칸에 블록이 있는 경우가 동시에 발생할 수 있다.
이 경우에는 행이나 열이 타일로 가득 찬 경우가 없을 때까지 점수를 획득하는 과정이
모두 진행된 후, 연한 칸에 블록이 있는 경우를 처리해야 한다.

얻은 점수, 초록색 보드와 파란색 보드에 타일이 있는 칸의 개수
'''

data = [[0] * 10 for _ in range(10)]
def stack_tile(t,i,j):
    #경계션 밖을 넘어가지 않고, 다른 타일에 부딪히지 않을 때까지 이동
    #타일 색깔 -> 10
    '''
    t = 1: 크기가 1×1인 블록을 (x, y)에 놓은 경우
    t = 2: 크기가 1×2인 블록을 (x, y), (x, y+1)에 놓은 경우
    t = 3: 크기가 2×1인 블록을 (x, y), (x+1, y)에 놓은 경우
    '''
    x,y = i,j
    if t == 1:
        #초록으로 이동
        while x < 9 and data[x+1][y] != 1:
            x += 1
        data[x][y] = 1

        #파랑으로 이동
        x, y = i, j
        while y < 9 and data[x][y+1] != 1:
            y += 1
        data[x][y] = 1

    elif t == 2:
        #초록으로 이동
        while x < 9 and y < 3 and data[x+1][y] != 1 and data[x+1][y+1] != 1:
            x += 1
        data[x][y] = 1
        data[x][y+1] = 1

        #파랑으로 이동
        x, y = i, j
        while y < 9 and data[x][y+1] != 1:
            y += 1
        data[x][y] = 1
        data[x][y-1] = 1

    elif t == 3:
        #초록으로 이동
        while x < 9 and data[x + 1][y] != 1:
            x += 1
        data[x][y] = 1
        data[x-1][y] = 1

        #파랑으로 이동
        x, y = i, j
        while x < 3 and y < 9 and data[x][y+1] != 1 and data[x+1][y+1] != 1:
            y += 1
        data[x][y] = 1
        data[x + 1][y] = 1

#연한색이랑 파란색이랑 동시에 full일 때 파란색이 없어진 후에 연한색에 있는 tile도 내려오나?
#아니면 연한색에 있던 tile은 그대로..?
def is_row_col_full():
    global res
    # 파란색 확인
    for j in range(4,10):
        cnt = 0
        for i in range(4):
            cnt += data[i][j]

        if cnt == 4:
            # tile 제거 및 이동
            for i in range(4):
                for k in range(j,4,-1):
                    data[i][k] = data[i][k-1]
            for i in range(4):
                data[i][4] = 0
            res += 1

    # 초록색 확인
    for i in range(4, 10):
        if sum(data[i]) == 4:
            res += 1

            #tile 이동
            for k in range(i,4,-1):
                data[k] = copy.deepcopy(data[k-1])
            data[4] = [0] * 10

def zero_one_full():
    for j in range(4,6):
        for i in range(4):
            if data[i][j] == 1:
                # tile 제거 및 이동
                for i in range(4):
                    for k in range(9, 4, -1):
                        data[i][k] = data[i][k - 1]
                for i in range(4):
                    data[i][4] = 0
                break

    for i in range(4,6):
        if sum(data[i]) > 0:
            # tile 이동
            for k in range(9, 4, -1):
                data[k] = copy.deepcopy(data[k - 1])
            data[i] = [0] * 10


n = int(sys.stdin.readline())
res = 0
for _ in range(n):
    t,x,y = map(int, sys.stdin.readline().split())
    stack_tile(t, x, y)
    #한 줄이 완성이 되면 / 연한 색깔에 위치하면 remove
    is_row_col_full()
    zero_one_full()

cnt = 0
for i in range(10):
    for j in range(10):
        if data[i][j] == 1:
            cnt += 1
print(res)
print(cnt)
