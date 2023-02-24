import sys
from collections import deque
n,m,r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

start = r
def dfs(start):
    que = deque([start])
    cnt = 1
    visited[start] = cnt
    while que:
        v = que.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                que.append(i)

dfs(start)
for i in range(1, n+1):
    print(visited[i])
                
    