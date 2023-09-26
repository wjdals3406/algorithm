import sys
from collections import deque
# 그래프 탐색을 해야하는 이유
# -> 중간에 밑으로 내려오고 다시 위로 이동해야하는 경우가 있음
# 스타트링크는 총 F층으로 이루어짐
# 스타트링크는 G층에 있음
# 강호는 S층에 있고 엘베 타고 G층으로 이동
# U: 위로 U층 이동
# D: 밑으로 D층 이동
# 버튼을 적어도 몇 번 눌러야 하는지
# F, S, G, U, D

height, now, dest, up, down = map(int, sys.stdin.readline().split())


def bfs():
    visited = [0] * (height+1)
    visited[now] = 1
    que = deque([[now, 0]])
    while que:
        x, cnt = que.popleft()
        if x > height:
            continue
        elif x == dest:
            return cnt

        if x+up <= height and not visited[x+up]:
            visited[x+up] = 1
            que.append((x+up, cnt+1))
        if x-down > 0 and not visited[x-down]:
            visited[x-down] = 1
            que.append((x-down, cnt+1))
    return "use the stairs"


print(bfs())
