from bisect import bisect_left, bisect_right
import sys

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n, k = list(map(int,sys.stdin.readline().rstrip().split()))
data = list(map(int,sys.stdin.readline().rstrip().split()))
print(-1 if count_by_range(data, k, k) == 0 else count_by_range(data, k, k))