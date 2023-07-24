import sys
import heapq
n,m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
heapq.heapify(card)

for _ in range(m):
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    heapq.heappush(card, a+b)
    heapq.heappush(card, a+b)

print(sum(card))