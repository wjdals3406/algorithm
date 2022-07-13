import heapq
import sys
#다이나믹 방식으로 풀면 안됨
INF = int(1e9)
k = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(k):
    n = int(sys.stdin.readline())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
        
    distance = [[INF] * n for _ in range(n+1)]
    x,y = 0,0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]
    
    while q:
        dist, x,y = heapq.heappop(q)
        
        if distance[x][y] < dist:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    
    print(distance[n-1][n-1])