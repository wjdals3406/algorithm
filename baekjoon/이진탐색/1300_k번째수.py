import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
# 배열 A와 B의 인덱스는 1부터 시작


def binary_search(start, end):
    while start <= end:
        row = (start + end) // 2

        sum = 0
        for i in range(1, n+1):
            sum += min(row//i, n)

        if sum >= k:
            end = row - 1
            answer = row
        else:
            start = row + 1

    return answer


print(binary_search(0, k))
