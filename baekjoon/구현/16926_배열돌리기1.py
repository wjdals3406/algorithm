# 회전은 독립적으로 이루어짐 R의 숫자가 충분히 크기 때문에
# 원상태로 돌아오는 경우도 있으니 무조건 돌리면 시간 초과 날 우려 있음
import sys
from collections import deque
n, m, r = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
limit = min(n, m) // 2

board = [[0] * m for _ in range(n)]
for l in range(0, limit):
    que = deque()
    que.extend(data[l][l:m-l])
    que.extend([data[i][m-l-1] for i in range(l+1, n-l)])
    que.extend(data[n-l-1][l:m-l-1][::-1])
    que.extend([data[i][l] for i in range(n-l-2, l, -1)])
    # 반시계 회전
    que.rotate(-r)

    for j in range(l, m-l):
        board[l][j] = que.popleft()
    for j in range(l+1, n-l):
        board[j][m-l-1] = que.popleft()
    for j in range(m-l-2, l-1, -1):
        board[n-l-1][j] = que.popleft()
    for j in range(n-l-2, l, -1):
        board[j][l] = que.popleft()

for i in board:
    print(*i)


# # 배열 반시계 방향으로 R번 회전
# import sys
# from collections import deque
# n, m, r = map(int, sys.stdin.readline().split())
# data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# limit = min(n, m) // 2

# for _ in range(r):
#     # r번 회전
#     for i in range(0, limit):
#         x, y = i, i
#         tmp = data[x][y]

#         # 밑으로
#         for j in range(i, n - i):
#             x = j
#             prev = data[x][y]
#             data[x][y] = tmp
#             tmp = prev

#         # 오른쪽으로
#         for j in range(i+1, m - i):
#             y = j
#             prev = data[x][y]
#             data[x][y] = tmp
#             tmp = prev

#         # 위로
#         for j in range(n-i-2, i-1, -1):
#             x = j
#             prev = data[x][y]
#             data[x][y] = tmp
#             tmp = prev

#         for j in range(m - i-2, i-1, -1):
#             y = j
#             prev = data[x][y]
#             data[x][y] = tmp
#             tmp = prev


# for i in data:
#     print(*i)
