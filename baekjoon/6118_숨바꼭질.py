import sys
from collections import defaultdict, deque
n, m = map(int, sys.stdin.readline().split())
dic = defaultdict(list)
visited = [int(1e9)] * (n+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)


def bfs():
    visited[1] = 0
    que = deque([(1, 0)])

    while que:
        x, cost = que.popleft()

        for i in dic[x]:
            ncost = cost + 1
            if ncost < visited[i]:
                visited[i] = ncost
                que.append((i, ncost))

    res = defaultdict(list)
    for i in range(1, n+1):
        res[visited[i]].append(i)

    maxlen = max(res.keys())
    print(res[maxlen][0], maxlen, len(res[maxlen]))


bfs()
