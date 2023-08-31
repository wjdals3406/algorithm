# 깊이가 K인 완전 이진 트리
# 중위순회
# 완전 이진 트리이기 때문에 트리가 다 채워져 있음
import sys
from collections import defaultdict
k = int(sys.stdin.readline())  # depth
# 상근이가 방문한 빌딩의 번호가 들어간 순서대로
data = list(map(int, sys.stdin.readline().split()))
depth = defaultdict(list)
n = len(data)


def divide_and_conquer(start, end, d):
    mid = (start + end) // 2
    depth[d].append(data[mid])
    if d < k:
        divide_and_conquer(start, mid, d+1)
        divide_and_conquer(mid+1, end, d+1)


divide_and_conquer(0, n, 1)
for key in depth:
    print(*depth[key])
