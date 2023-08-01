import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
start = 1
for _ in range(n-2):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    start = a


def bfs():
    visited[start] = 1
    que = deque([start])

    while que:
        node = que.popleft()

        for i in graph[node]:
            if not visited[i]:
                visited[i] = 1
                que.append(i)

    visited[0] = -1
    print(start, visited.index(0))


bfs()
