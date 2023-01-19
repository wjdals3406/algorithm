import heapq
def solution(operations):
    maxheap = []
    minheap = []
    
    for com in operations:
        com = com.split(' ')
        num = int(com[1])

        if com[0] == 'I':
            heapq.heappush(maxheap, -num)
            heapq.heappush(minheap, num)
        else:
            #�� ť���� ������ ���� -> �ش� ���� ����
            if len(maxheap) == 0:
                continue
            if num == 1:
                minheap.remove(-heapq.heappop(maxheap))
            else:
                maxheap.remove(-heapq.heappop(minheap))
    if len(maxheap) == 0:
        return [0,0]
    else:
        return [-heapq.heappop(maxheap), heapq.heappop(minheap)]
    
    
