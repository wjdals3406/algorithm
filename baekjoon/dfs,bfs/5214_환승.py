# 그냥 bfs를 돌리게 되면 que에 담아지는 경우가 너어무 많음
# -> 이미 방문한 노드들이 que에 많이 담겨 있을 수 있음
import sys
from collections import deque
n, k, m = map(int, sys.stdin.readline().split())
station = [[] for _ in range(n+1)]
hyper = [[] for _ in range(m+1)]
for hidx in range(1, m+1):
    X = list(map(int, sys.stdin.readline().split()))
    for num in X:
        station[num].append(hidx)
        hyper[hidx].append(num)


def bfs():
    visited_station = [0] * (n+1)
    visited_hyper = [0] * (m+1)
    que = deque([[1, 1]])  # node, 거쳐갈 노드 수
    visited_station[1] = 1

    while que:
        node, cnt = que.popleft()

        if node == n:
            return cnt

        # station에서 방문할 수 있는 하이퍼튜브 탐색
        next_visit_hyper = []
        for hyper_idx in station[node]:
            if not visited_hyper[hyper_idx]:
                visited_hyper[hyper_idx] = 1
                next_visit_hyper.append(hyper_idx)

        for n_hyper in next_visit_hyper:
            for n_station in hyper[n_hyper]:
                if not visited_station[n_station]:
                    que.append((n_station, cnt + 1))
                    visited_station[n_station] = 1

    return -1


print(bfs())
