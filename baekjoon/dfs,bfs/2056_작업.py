import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
graph = defaultdict(list)
time = [0] * (n+1)
table = [0] * (n+1)
for now in range(1, n+1):
    tmp = list(map(int, sys.stdin.readline().split()))
    t, k = tmp[0], tmp[1]
    if now == 1:
        time[now] = t
    for j in range(k):
        pre = tmp[j+2]
        graph[pre].append(now)
    table[now] = t
    time[now] = t


def dfs(node):
    if len(graph[node]) == 0:
        return
    for next in graph[node]:
        if time[next] < time[node] + table[next]:
            time[next] = time[node] + table[next]
            dfs(node)


for i in graph:
    dfs(i)
for i in range(1, n+1):
    if time[i] == 0:
        time[i] = table[i]
print(max(time))
