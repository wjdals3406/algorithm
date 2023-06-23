# import sys
# def func():
#     dp = [[int(1e9)] * n for _ in range(n)]
#     dp[0][0] = data[0][0]
#     for i in range(n):
#         for j in range(n):
#             if i > 0:
#                 dp[i][j] = min(dp[i][j], dp[i-1][j] + data[i][j])
#             if j > 0:
#                 dp[i][j] = min(dp[i][j], dp[i][j-1] + data[i][j])
#             if i < n-1:
#                 dp[i][j] = min(dp[i][j], dp[i+1][j] + data[i][j])
#             if j < n-1:
#                 dp[i][j] = min(dp[i][j], dp[i][j+1] + data[i][j])

#     print(dp[n-1][n-1])


# n = int(sys.stdin.readline())
# while n > 0:
#     data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#     func()

#     n = int(sys.stdin.readline())


import heapq
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def func():
    cost[0][0] = data[0][0]
    h = [(data[0][0], 0, 0)]

    while h:
        total, x, y = heapq.heappop(h)

        if total > cost[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            next_total = total + data[nx][ny]
            if next_total < cost[nx][ny]:
                cost[nx][ny] = next_total
                heapq.heappush(h, (total + data[nx][ny], nx, ny))


n = int(sys.stdin.readline())
cnt = 1
while n > 0:
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    cost = [[int(1e9)] * n for _ in range(n)]
    func()
    print(f'Problem {cnt}: {cost[n-1][n-1]}')
    n = int(sys.stdin.readline())
    cnt += 1
