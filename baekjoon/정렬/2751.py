import sys
n = int(sys.stdin.readline())
data = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)])
for i in data:
    print(i)