# -*- coding: utf-8 -*-
import sys
from collections import deque

n,m = map(int, sys.stdin.readline().rstrip().split())
pick = list(map(int, sys.stdin.readline().rstrip().split()))
data = deque([i+1 for i in range(n)])
result = 0

for p in pick:
    if data.index(p) == 0:
        data.popleft()
    else:
        if data.index(p) <= n // 2:
            result += data.index(p)
            data.rotate(-data.index(p))
            data.popleft()
        else:
            result += n-1 - data.index(p) + 1
            data.rotate(n-1 - data.index(p)+1)
            data.popleft()
    n -= 1

print(result)

