import heapq
import sys

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))    

INF = int(1e9)
n, m = map(int,sys.stdin.readline().split())
start = 1
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))
    
dijkstra(start)
print(distance)
distance = [-1 if i == INF else i for i in distance ]
print(distance.index(max(distance)), max(distance),  distance.count(max(distance)))  
