import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

result = 0
for i in list(combinations(data, 3)):
    if sum(i) > m:
        continue
    result = max(result, sum(i))

print(result)