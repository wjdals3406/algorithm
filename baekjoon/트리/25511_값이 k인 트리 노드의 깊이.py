import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
n, k = map(int, sys.stdin.readline().split())
child = defaultdict(list)
for _ in range(n-1):
    p, c = map(int, sys.stdin.readline().split())
    child[p].append(c)
data = list(map(int, sys.stdin.readline().split()))


def dfs(node, depth):
    for c in child[node]:
        if data[c] == k:
            return depth+1
        dvalue = dfs(c, depth+1)
        if dvalue != None:
            return dvalue


if data[0] == k:
    print(k)
else:
    print(dfs(0, 0))
