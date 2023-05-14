import sys
from collections import defaultdict
import heapq
n, m = map(int, sys.stdin.readline().split())
indegree = [0] * (n+1)
graph = defaultdict(list)

for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = []

    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    while q:
        now = heapq.heappop(q)
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)

    for i in result:
        print(i)


topology_sort()
