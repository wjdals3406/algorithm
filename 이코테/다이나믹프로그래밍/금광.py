# -*- coding: utf-8 -*-
import sys

def memo(r, c):
    if visit[r][c] != 0:
        return visit[r][c]
    if c == 1:
        return data[r][c]
    elif r == 1:
        a = memo(r, c - 1)
        b = memo(r + 1, c - 1)
        visit[r][c] = max(a, b) + data[r][c]
    elif r == n:
        a = memo(r, c - 1)
        b = memo(r - 1, c - 1)
        visit[r][c] = max(a, b) + data[r][c]
    else:
        a = memo(r, c - 1)
        b = memo(r - 1, c - 1)
        d = memo(r + 1, c - 1)
        visit[r][c] = max([a,b,d])+ data[r][c]
    return visit[r][c]

k = int(sys.stdin.readline())
for _ in range(k):
    n, m = map(int,sys.stdin.readline().split())
    info = list(map(int,sys.stdin.readline().split()))
    data = [[0] + info[i:i+m] for i in range(0, len(info), m)]
    data.insert(0, [0])
    visit = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    result = -1
    for r in range(1, n+1, 1):
        result = max(memo(r, m), result)
    print(result)
        