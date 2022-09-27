# -*- coding: utf-8 -*-
import sys
k = int(sys.stdin.readline())
graph = [[] for _ in range(k+1)]
visited = [0] * (k+1)
parent = [0] * (k+1)
def dfs(node):
    visited[node] = 1
    for i in graph[node]:
        if not visited[i]:
            parent[i] = node
            dfs(i)
    
for _ in range(k-1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
for i in range(2,k+1):
    print(parent[i])
#'\n'.join(map(str, parents[2:])) 이렇게 출력 가능