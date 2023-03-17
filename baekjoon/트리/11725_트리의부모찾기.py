import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
#트리의 루트 : 1
n = int(sys.stdin.readline())
graph = defaultdict(list)
visited = [0] * (n+1)
visited[1] = 1

for i in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    for i in graph[node]:
        if not visited[i]:
            visited[i] = node
            dfs(i)

dfs(1)
for i in visited[2:]:
    print(i)
            
            