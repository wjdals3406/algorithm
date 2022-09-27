# -*- coding: utf-8 -*-
#'.'�� �� ĭ, 'x'�� �̳׶�
#�� -> ��, �� -> �� ������ ����, ¦�� �ε��� : ���ʿ��� ������ ���, Ȧ�� �ε��� : �����ʿ��� ������ ���
# �̳׶�
import sys
from collections import deque
r,c = map(int, sys.stdin.readline().split())
data = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
n = int(sys.stdin.readline())
height = list(map(int, sys.stdin.readline().split()))
height = list(map(lambda x : x-1, height)) #�ε��� 0���� �����ϱ� ���� -1�� ����
dx = [-1,1,0,0] #��, ��, �Ʒ� Ȯ��/ ���� �ִ��� Ȯ��X
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
            if data[nx][ny] == 'x' and not visited[nx][ny] : #�湮���� �ʾ��� ��
                que.append([nx,ny])
            if nx == r-1: #�ٴڿ� �̳׶��� ���� -> �ı��� �ȵ�
                flag = 1
    if flag : 
        return False
    return True # �ٴڿ� �̳׶��� �������� ���� -> �ı���

def drop_mineral(x,y): 
    value = visited[x][y]
    vlist = []
    for j in range(c): 
        for i in range(r):
            if data[i][j] == 'x' and visited[i][j] == value:
                vlist.append((i,j))
                data[i][j] = '.'
                #i�� �� ū �� ã��
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
    downCnt, flag = 1, 0      # downCnt ũ�� 1�� �÷�����
    while True:
        for r, c in fallLst:
            if r+downCnt == R-1:        # ���� �����ų�
                flag = 1
                break
            if cave[r+downCnt+1][c] == 'x' and check[r+downCnt+1][c]:   # �ٸ� �̳׶� ������
                flag = 1
                break
        if flag:    # �� ���� ������ �� �ִ� �ִ� downCnt ��
            break
        downCnt += 1
    return downCnt
                                
for xindex, x in enumerate(height): #���ʿ��� ��������, �����ʿ��� ��������
    if xindex % 2 == 0:
        check = range(c)
    else:
        check = range(c-1, -1, -1)
        
    x = r-x-1
    for y in check: #�� �࿡ �̳׶��� �ƿ� ���� ���� ����
        if data[x][y] == 'x': #�̳׶��̸�
            data[x][y] = '.' #�̳׶� �ı�
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
            if cnt == 2: #�̳׶��� 2���� ���� �־��� �� �̳׶��� �ı��Ǵ� ���ɼ��� ����
                visited = [[0] * c for _ in range(r)]
                for index in range(cnt):
                    nx,ny = mlist[index]
                    if bfs(nx,ny,index+1): #����߸�
                        downCnt = checkDownCnt(fallLst, check)

                        # 5�ܰ� - �̳׶� ������ ��ġ ������ �׸���
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
