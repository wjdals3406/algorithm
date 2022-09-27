#bfs
# import sys
# from collections import deque
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)

# for _ in range(m):
#     a,b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
    
# start = 1
# def bfs():
#     que = deque([start])
#     visited[start] = True
#     count = 0
#     while que:
#         v = que.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 count+=1
#                 que.append(i)
#                 visited[i] = True
#     return count

# print(bfs())
#dfs
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
start = 1
cnt = 0
def dfs(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt+=1
            dfs(i)
dfs(start)
print(cnt)
                