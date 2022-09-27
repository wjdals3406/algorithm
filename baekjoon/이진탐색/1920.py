from bisect import bisect_left, bisect_right
import sys

def count_by_range(data, left, right):
    a = bisect_left(data, left)
    b = bisect_right(data, right)
    return b - a

_ = sys.stdin.readline()
data = list(map(int, sys.stdin.readline().split()))
data.sort()
m = int(sys.stdin.readline())
search = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    print(1) if count_by_range(data, search[i], search[i]) > 0 else print(0)
