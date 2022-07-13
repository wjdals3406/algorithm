import sys
from itertools import combinations

def distance(*arg):
    ax,ay,az = arg[0]
    bx,by,bz = arg[1]
    return min(abs(ax - bx), abs(ay - by), abs(az - bz))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline())
parent = [0] * (n + 1)
for i in range(1, n+1):
    parent[i] = i
    
edges = []
data = []
index = [i for i in range(n)]

for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
    
comb = list(combinations(index, 2))
for i in comb:
    cost = distance(data[i[0]], data[i[1]])
    edges.append((cost, i[0], i[1]))
    
edges.sort()

result = 0
for edge in edges:
    cost,a,b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b) 
        result += cost
        
print(result)