import sys
from collections import deque
n = int(sys.stdin.readline())
a,b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    c,d = map(int, sys.stdin.readline().split())
    graph[c].append(d)
    graph[d].append(c)

start = a
def bfs():
    que = deque([start])
    while que:
        v = que.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                que.append(i)
bfs()
if visited[b] == 0:
    print(-1)
else:
    print(visited[b])
