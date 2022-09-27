import sys
import heapq
n = int(sys.stdin.readline())
h = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if h:
            value = heapq.heappop(h)
            print(value[1])
        else:
            print(0)
    else:
        heapq.heappush(h,(abs(num),num))