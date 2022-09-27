# -*- coding: utf-8 -*-
import sys
k = int(sys.stdin.readline())

def dfs(s,cnt):
    visited[s] = 1
    for i in graph[s]:
        if visited[i] == 0:
            cnt = dfs(i,cnt+1)
    return cnt
    
for _ in range(k):
    n,m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0] * (n+1)
    visited[1] = 1
    cnt = dfs(1,0)
    print(cnt)
    

    
    