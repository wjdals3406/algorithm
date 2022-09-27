import sys
n = int(sys.stdin.readline())
data = []
re = ''
for _ in range(n):
    a,*b = map(int, sys.stdin.readline().split())
    if a == 0:
        if data:
            maxval = max(data)
            re += maxval
            data.remove(maxval)
        else:
            re += -1
    else:
        data.extend(b)

        