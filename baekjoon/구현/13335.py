# -*- coding: utf-8 -*-
import sys
from collections import deque 
#n : 트럭 수, w : 다리 길이, l : 최대 하중
n, w, l = map(int, sys.stdin.readline().split()) 
data = deque(map(int, sys.stdin.readline().split()))
bridge = deque([0 for _ in range(w)])
time = 0
while bridge:
    bridge.popleft()
    if data:
        if sum(bridge) + data[0] <= l:
            bridge.append(data.popleft())
        else:
            bridge.append(0)

    time += 1
    
print(time)
