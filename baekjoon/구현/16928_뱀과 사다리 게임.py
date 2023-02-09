# -*- coding: utf-8 -*-
#100�� ĭ�� �����ϱ� ���� �ֻ����� �ּ� �� �� ������ �ϴ���
#�Ǽ��� ���� : ���� Ÿ�� �������� ���� �� �̵��� ���� �ִٴ� ���� ���� ���� / visited �Ƚ���
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
    #�������� : 1
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