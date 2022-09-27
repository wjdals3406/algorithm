import sys
import heapq
n = int(sys.stdin.readline())
h = []
res = ''
for _ in range(n):
    k = int(sys.stdin.readline())
    if k == 0:
        if h:
            res += str(heapq.heappop(h)) + '\n'
        else:
            res += '0\n'
    else:
        heapq.heappush(h, k)
print(res)
