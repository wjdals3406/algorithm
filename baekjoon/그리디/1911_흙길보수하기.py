import sys
from collections import deque
n, l = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
data.sort()
cnt = end = 0
for s, e in data:
    start = max(s, end)
    if end >= s:
        start = end + 1
    if start > e:
        continue

    if (e - start) % l > 0:
        cnt += (e - start) // l + 1
        end = start + ((e - start) // l + 1)*l - 1
    else:
        cnt += (e - start) // l
        end = start + (e - start) - 1

print(cnt)
