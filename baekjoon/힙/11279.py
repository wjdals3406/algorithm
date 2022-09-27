import sys
import heapq
n = int(sys.stdin.readline())
h = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h,-num)