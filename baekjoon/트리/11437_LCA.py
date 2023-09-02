# 이 문제의 경우 루트가 1번이라는 것 외에는
# 특정 노드의 부모 노드가 몇인지 알 수 없다
# => 밑에서 위가 아닌, 위에서 아래로 내려와야 함
# 1) 깊이를 먼저 동일하기 맞춰주기
# 2) 그다음 최소 공통 조상 찾기
import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
depth = [-1] * (n+1)  # 특정 노드에서의 depth
depth[1] = 1
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node, d):
    for c in graph[node]:
        if depth[c] == -1:
            depth[c] = d
            parent[c] = node
            dfs(c, d+1)


def find_parent(a, b):
    # 깊이를 같게 해줌
    while depth[a] > depth[b]:
        a = parent[a]

    while depth[a] < depth[b]:
        b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a


dfs(1, 2)
m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(find_parent(a, b))
