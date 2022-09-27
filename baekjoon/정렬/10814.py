import sys
n = int(sys.stdin.readline())
data = [list(sys.stdin.readline().rstrip().split()) for _ in range(n)]
data.sort(key = lambda x : int(x[0]))
for a,b in data:
    print(a, b)
    