# -*- coding: utf-8 -*-
import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split())
visited = [-1] * 100001
def bfs():
    visited[n] = 0
    que = deque([n])
    
    while que:
        x = que.popleft()
        if x == k:
            return visited[x]
        
        for nx in (x+1, x-1, x*2):
            if 0<=nx<=100000 and visited[nx] == -1:
                que.append(nx)
                visited[nx] = visited[x] + 1
        
print(bfs())
        

