# -*- coding: utf-8 -*-
import sys
import heapq
n = int(sys.stdin.readline())
# data = []
# for _ in range(n):
#     heapq.heappush(data,tuple(map(int,sys.stdin.readline().split())))
data = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
data.sort()
time = []
heapq.heappush(time, data[0][1])

for s,e in data[1:]:
    if s < time[0]:
        heapq.heappush(time,e)
    else:
        heapq.heappop(time)
        heapq.heappush(time,e)
        
            
print(len(time))
    