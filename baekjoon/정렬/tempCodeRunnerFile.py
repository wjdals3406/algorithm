import sys
from collections import Counter
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
data = sorted(Counter(data).items(), key = lambda x: (-x[1], x[0]))
print(data[0])
