# d: 간선 한 개를 기준으로 양 끝에 달린 노드의 자식 노드가 2개일 때/g: 자식 노드가 3개일 때
import sys
from collections import defaultdict
from math import factorial
n = int(sys.stdin.readline())
graph = []
child = [0] * (n+1)
d = g = 0
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    child[a] += 1
    child[b] += 1
    graph.append((a, b))


def comb(n, pick):
    total = 1
    div = 1
    for i in range(n, n-pick, -1):
        total *= i

    for i in range(1, pick+1):
        div *= i

    return total / div


# child에서 3개 뽑는 방법의 수(조합)
for node in range(1, n+1):
    if child[node] >= 3:
        g += comb(child[node], 3)
for a, b in graph:
    d += (child[a]-1) * (child[b]-1)


if d == g*3:
    print("DUDUDUNGA")
elif d > g*3:
    print("D")
else:
    print("G")
