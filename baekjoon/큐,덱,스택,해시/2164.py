import sys
from collections import deque

n = int(sys.stdin.readline())
data = deque([i for i in range(1, n+1)])
while len(data) > 1:
    data.popleft()
    data.append(data.popleft())
    
print(data[0])