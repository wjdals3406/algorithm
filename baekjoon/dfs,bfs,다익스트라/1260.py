import sys
from collections import deque
n,m,v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()
    
start = v
def dfs(v):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
def bfs():
    visited[start] = True
    que = deque([start])
    while que:
        v = que.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                que.append(i)

dfs(start)
print()
visited = [False] * (n+1)
bfs()

        