import sys
import heapq
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    a,*b = map(int, sys.stdin.readline().split())
    if a == 0:
        if data:
            print(-heapq.heappop(data))
        else:
            print(-1)
    else:
        for i in b:
            heapq.heappush(data, -i)
        