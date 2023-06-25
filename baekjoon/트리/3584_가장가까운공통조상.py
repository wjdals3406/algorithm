import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
t = int(sys.stdin.readline())


def dfs(node, rlist):
    rlist.append(node)
    for i in parent[node]:
        dfs(i, rlist)


for _ in range(t):
    n = int(sys.stdin.readline())
    parent = defaultdict(list)

    for i in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        parent[b].append(a)
    a, b = map(int, sys.stdin.readline().split())

    aplist, bplist = [], []
    dfs(a, aplist)
    dfs(b, bplist)

    aidx, bidx = len(aplist) - 1, len(bplist) - 1
    while aidx >= 0 and bidx >= 0 and aplist[aidx] == bplist[bidx]:
        aidx -= 1
        bidx -= 1

    print(aplist[aidx+1])
