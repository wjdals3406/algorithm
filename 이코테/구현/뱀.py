# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
board = [[0 for _ in range(n+2)] for _ in range(n+2)] 


for i in range(k):
    a, b = map(int,sys.stdin.readline().split())
    board[a][b] = -1

direction = []
l = int(sys.stdin.readline())
for i in range(l):
    c, d = map(str,sys.stdin.readline().split())
    c = int(c)
    direction.append([c,d])
 
turn_time = [i[0] for i in direction]   

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(direction):
    direction -=1
    if direction == -1:
        direction = 3
    return direction

def turn_right(direction):
    direction +=1
    if direction == 4:
        direction = 0
    return direction

dir = 1
tdir = 1
x = 1
y = 1
time = 0
s = [[x,y]]
while x < n + 1 and x > 0 and y < n+1 and y > 0 and board[x + dx[dir]][y + dy[dir]] != 1:
    x = x + dx[dir]  #head ��ǥ
    y = y + dy[dir]  
    
    if board[x][y] == -1: # �̵��� ���� ����� ���� ��
        board[x][y] = 1
        s.append([x,y])
    
    else: # �̵��� ���� ��� ���� ��
        board[x][y] = 1
        s.append([x,y])
        tx, ty = s[0]
        board[tx][ty] = 0
        del s[0]
        
    time += 1
    if time in turn_time:
        for t, D in direction:
            if time == t:
                if D == 'D':
                    dir=turn_right(dir)
                
                elif D == 'L':
                    dir=turn_left(dir)
                break
            
if x < n + 1 and x > 0 and y < n+1 and y > 0 and board[x + dx[dir]][y + dy[dir]] == 1:
    time += 1           
print(time) 
 