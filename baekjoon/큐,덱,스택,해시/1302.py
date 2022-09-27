import sys
from collections import Counter
n = int(sys.stdin.readline())
data = [sys.stdin.readline().rstrip() for _ in range(n)]
data = Counter(data)
data = sorted(data.items(), key = lambda x : (-x[1], x[0]))
print(data[0][0])