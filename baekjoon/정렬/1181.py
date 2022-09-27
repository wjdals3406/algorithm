import sys
n = int(sys.stdin.readline())
data = sorted(set([sys.stdin.readline().rstrip() for _ in range(n)]), key = lambda x : (len(x), x))
for i in data:
    print(i)