import sys
from collections import deque
n = int(sys.stdin.readline())
que = deque()
for _ in range(n):
    com = list(map(str, sys.stdin.readline().rstrip().split()))
    if com[0] == 'push_front':
        que.appendleft(com[1])
    elif com[0] == 'push_back':
        que.append(com[1])
    elif com[0] == 'pop_front':
        if que:
            print(que.popleft())
        else: print(-1)
    elif com[0] == 'pop_back':
        if que:
            print(que.pop())
        else: print(-1)
    elif com[0] == 'size':
        print(len(que))
    elif com[0] == 'empty':
        if que:
            print(0)
        else: print(1)
    elif com[0] == 'front':
        if que:
            print(que[0])
        else: print(-1)
    elif com[0] == 'back':
        if que:
            print(que[-1])
        else: print(-1)