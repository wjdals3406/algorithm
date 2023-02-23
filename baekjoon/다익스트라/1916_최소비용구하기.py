from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = defaultdict(list)
distance = [int(1e9)] * (n+1)
for _ in range(m):
    a,b,cost = map(int, input().split())
    graph[a].append((cost,b))
s,e = map(int, input().split())
    
def dijkstra():
    heap = []
    heapq.heappush(heap,(0,s))
    distance[s] = 0
    
    while heap:
        cost, node = heapq.heappop(heap)    
        if distance[node] < cost:
            continue

        for next_cost, next_node in graph[node]:
            update = cost + next_cost
            if update < distance[next_node]:
                distance[next_node] = update
                heapq.heappush(heap,(update, next_node))
                
dijkstra()
print(distance[e])
                
                
            