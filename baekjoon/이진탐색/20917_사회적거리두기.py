# n개의 콘센트 위치 중 s개를 선택하여 좌석을 선택하되,
# 가장 가까운 두 좌석의 거리 (D라 하자)가 최대가 되도록
import sys
t = int(sys.stdin.readline())


def binary_search(start, end, s):
    while start <= end:
        mid = (start + end) // 2

        pre, cnt = 0, 0
        for c in range(1, len(data)):
            if data[c] - data[pre] >= mid:
                cnt += 1
                pre = c
            if cnt > s:
                break

        if cnt >= s:
            start = mid + 1
        else:
            end = mid - 1

    return end


for _ in range(t):
    n, s = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()
    print(binary_search(0, data[n-1] - data[0], s-1))
