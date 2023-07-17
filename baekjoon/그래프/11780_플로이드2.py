import sys
import copy
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[int(1e9)] * (n+1) for _ in range(n+1)]
edge = [[[] for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    if cost < graph[a][b]:
        graph[a][b] = cost
        edge[a][b] = [a, b]

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k]+graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k]+graph[k][b]
                # 순서가 유지되는 리스트 중복 제거
                edge[a][b] = list(dict.fromkeys(
                    copy.copy(edge[a][k]) + copy.copy(edge[k][b])))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j] if graph[i][j] < int(1e9) else 0, end=" ")
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if not edge[i][j]:
            print(0)
        else:
            print(len(edge[i][j]), " ".join(list(map(str, edge[i][j]))))
