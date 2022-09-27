import sys
sum = 0
minval = int(1e9)
for i in range(7):
    d = int(sys.stdin.readline())
    if d % 2 != 0:
        sum += d
        if d < minval:
            minval = d
if sum == 0:
    print(-1)
else:
    print(sum)
    print(minval)
        
    