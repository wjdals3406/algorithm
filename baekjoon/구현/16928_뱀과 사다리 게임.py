# -*- coding: utf-8 -*-
#100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야 하는지
#실수한 이유 : 뱀을 타고 내려오는 것이 더 이득일 때도 있다는 것을 인지 못함 / visited 안썼음
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
ladder,snake = dict(),dict()
visited = [0] * 101
for _ in range(n):
    x,y = map(int, sys.stdin.readline().split())
    ladder[x] = y
    
for _ in range(m):
    x,y = map(int, sys.stdin.readline().split())
    snake[x] = y

def bfs():
    #시작지점 : 1
    que = deque([[1,0]])
    visited[1] =1
    
    while que:
        s,cnt = que.popleft()
        
        for dice in range(1,7):
            next = s + dice                
            if next == 100:
                return cnt + 1
            
            if next < 100 and not visited[next]:
                if next in ladder.keys():
                    next = ladder[next]
                elif next in snake.keys(): 
                    next = snake[next]
                
                if not visited[next]:
                    visited[next] = 1
                    que.append([next, cnt + 1])

print(bfs())