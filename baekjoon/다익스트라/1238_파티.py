# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline
INF = int(1e9)
n,m,x = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a,b,cost = map(int, input().split())
    graph[a].append((cost,b))
    
def dijkstra(s):
    distance = [INF] * (n+1)
    h = []
    heapq.heappush(h,(0,s))
    distance[s] = 0
    
    while h:
        cost, now = heapq.heappop(h)
        if cost > distance[now]:
            continue
        
        for n_cost, n_node in graph[now]:
            update = cost + n_cost
            
            if update < distance[n_node]:
                distance[n_node] = update
                heapq.heappush(h,(update,n_node))
    return distance

res = 0
xdist = dijkstra(x)
for i in range(1,n+1):
    if i == x:
        continue
    i_dist = dijkstra(i)
    res = max(res, i_dist[x]+xdist[i])
print(res)    



# #시간초과
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
# n,m,x = map(int, input().split())
# distance = [[INF] * (n+1) for _ in range(n+1)]

# for _ in range(m):
#     a,b,cost = map(int, input().split())
#     distance[a][b] = cost

# for i in range(1,n+1):
#     distance[i][i] = 0
    
# for k in range(1,n+1):
#     for a in range(1,n+1):
#         for b in range(1,n+1):
#             distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])
   
# res = 0      
# for i in range(1,n+1):
#     if distance[i][x] != INF and distance[x][i] != INF:
#         res = max(res, distance[i][x] + distance[x][i])
            
# print(res)