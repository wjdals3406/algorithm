# -*- coding: utf-8 -*-
import sys
import heapq
INF = int(1e9)
n,e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

# start, end = 1, n # 1부터 n까지 이동할 때, 주어진 두 간선은 모두 꼭 통과해야함

for _ in range(e):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
v1, v2 = map(int, sys.stdin.readline().split())
    
def dijkstra(s):
    distance = [INF] * (n+1)
    h = []
    heapq.heappush(h, (0, s))
    distance[s] = 0
    while h:
        dist, node = heapq.heappop(h)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))
    return distance
# 1 -> v1 -> v2 -> n
# 1 -> v2 -> v1 -> n            
s = dijkstra(1)
a = dijkstra(v1)
b = dijkstra(v2)
res = min(s[v1] + a[v2] + b[n], s[v2] + b[v1] + a[n])
print(-1 if res >= INF else res)

