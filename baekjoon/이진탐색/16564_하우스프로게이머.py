# 마지막 값의 범위는 data[n-1]이 아니라 data[n-1] + k이라는 것에 주의!
import sys
n, k = map(int, sys.stdin.readline().split())
data = [int(sys.stdin.readline()) for _ in range(n)]
data.sort()


def binary_search(start, end, tmp):
    while start <= end:
        tlevel = (start + end)//2
        tmp = 0

        for l in data:
            if tlevel > l:
                tmp += (tlevel - l)
            else:
                break

        if tmp > k:
            end = tlevel - 1
        else:
            start = tlevel + 1

    return end


print(binary_search(data[0], data[n-1] + k, k))
