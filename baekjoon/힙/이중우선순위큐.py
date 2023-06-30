import sys
import heapq
from collections import defaultdict
t = int(sys.stdin.readline())


#Q에 남아 있는 값 중 최댓값과 최솟값을 출력
for _ in range(t):
    minheap, maxheap = [], []
    hdic = defaultdict(int)
    k = int(sys.stdin.readline())
    
    for _ in range(k):
        char, n = map(str, sys.stdin.readline().split())
        n = int(n)
        if char == "I":
            heapq.heappush(minheap, n) #input 그대로의 값
            heapq.heappush(maxheap, -n)
            hdic[n] += 1
        elif char == "D" and minheap and maxheap:
            #최댓값 삭제
            if n > 0:
                #이미 처리한 값이면 pass
                while maxheap and hdic[-maxheap[0]] == 0:
                    heapq.heappop(maxheap)
                    
                if maxheap:
                    value = -heapq.heappop(maxheap)
                    hdic[value] -= 1
                
            #최솟값 삭제
            elif n < 0:
                while minheap and hdic[minheap[0]] == 0:
                    heapq.heappop(minheap)
                
                if minheap:
                    value = heapq.heappop(minheap)
                    hdic[value] -= 1
    
    #이미 처리한 값이면 pass
    while maxheap and hdic[-maxheap[0]] == 0:
        heapq.heappop(maxheap)
    
    #최솟값 삭제
    while minheap and hdic[minheap[0]] == 0:
        heapq.heappop(minheap)
 
    if minheap and maxheap:
        print(-maxheap[0], minheap[0])
    else: print("EMPTY")
        

    