import sys
from bisect import bisect_left
t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int, sys.stdin.readline().split())
    a = sorted(list(map(int, sys.stdin.readline().split())))
    b = sorted(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    for i in a:
        cnt += bisect_left(b,i)
    print(cnt)


