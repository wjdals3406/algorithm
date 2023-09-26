import sys
# 케이블이 연결되어있는 도시에는 발전소가 반드시 하나만 존재
# union 하기 전에 부모 노드 확인 -> 부모 노드가 발전소라면 pass
n, m, k = map(int, sys.stdin.readline().split())
_ = list(map(int, sys.stdin.readline().split()))
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])
elec = [0] * (n+1)
for i in _:
    elec[i] = 1

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    global total
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if elec[a] and elec[b]:
        return

    if elec[a]:
        parent[b] = a
    elif elec[b]:
        parent[a] = b
    elif a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b
    total += cost


total = 0
for a, b, cost in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

print(total)
