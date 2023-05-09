import sys
import heapq
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]
data.sort()

res = 0
if len(data) == 1:
    print(0)

else:
    while data:
        one = heapq.heappop(data)
        two = heapq.heappop(data)
        res += one + two
        if data:
            heapq.heappush(data, one+two)
        else:
            break
    print(res)
