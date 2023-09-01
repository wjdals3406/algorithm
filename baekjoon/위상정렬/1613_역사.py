import sys
from collections import deque
n, event = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
distance = [[0] * (n+1) for _ in range(n+1)]
for _ in range(event):
    # a가 b보다 먼저 일어난 사건
    a, b = map(int, sys.stdin.readline().split())
    distance[a][b] = 1
    graph[a].append(b)
    indegree[b] += 1

que = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        que.append(i)

visited = [set() for _ in range(n+1)]


def topology_sort():
    while que:
        cur = que.popleft()

        for next in graph[cur]:
            indegree[next] -= 1
            visited[next].add(cur)
            visited[next].update(visited[cur])
            if indegree[next] == 0:
                que.append(next)


topology_sort()
s = int(sys.stdin.readline())
for i in range(s):
    a, b = map(int, sys.stdin.readline().split())
    if a in visited[b]:
        print(-1)
    elif b in visited[a]:
        print(1)
    else:
        print(0)


# import sys
# from collections import deque
# n, event = map(int, sys.stdin.readline().split())
# distance = [[0] * (n+1) for _ in range(n+1)]
# for _ in range(event):
#     # a가 b보다 먼저 일어난 사건
#     a, b = map(int, sys.stdin.readline().split())
#     distance[a][b] = 1

# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             if distance[a][k] == 1 and distance[k][b] == 1:
#                 distance[a][b] = 1

# s = int(sys.stdin.readline())
# for i in range(s):
#     a, b = map(int, sys.stdin.readline().split())
#     if distance[a][b]:
#         print(-1)
#     elif distance[b][a]:
#         print(1)
#     else:
#         print(0)
