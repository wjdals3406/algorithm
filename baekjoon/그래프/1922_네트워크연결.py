#모든 컴퓨터를 연결하는데 필요한 최소비용
#크루스칼
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edge = []
parent = [i for i in range(n+1)]
for _ in range(m): 
    a, b, cost = map(int, sys.stdin.readline().split())
    if a == b:
        continue
    
    edge.append((cost, a, b))
               
def find_parent(x):
    if parent[x] != x :
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_node(a,b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edge.sort()
total = 0
for e,a,b in edge:
    if find_parent(a) != find_parent(b):
        union_node(a,b)
        total += e

print(total)
