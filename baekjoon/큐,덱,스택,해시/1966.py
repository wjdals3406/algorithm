import sys
from collections import deque

k = int(sys.stdin.readline())
for _ in range(k):
    n,num = map(int, sys.stdin.readline().rstrip().split())
    data = deque(map(int, sys.stdin.readline().rstrip().split()))
    index = deque(i for i in range(n))
    result = 0
    while data:
        if data[0] >= max(data):
            if index[0] == num:
                print(result+1)
                break
            data.popleft()
            index.popleft()
            result += 1
        else:
            data.append(data.popleft())
            index.append(index.popleft())
        