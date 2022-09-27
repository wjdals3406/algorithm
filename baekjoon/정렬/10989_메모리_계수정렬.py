import sys
n = int(sys.stdin.readline())
data = [0] * 10001

for _ in range(n):
    data[int(sys.stdin.readline())] += 1

for i in range(1,n+1):
    if data[i] > 0:
        for _ in range(data[i]):
            print(i)
    
