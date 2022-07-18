# -*- coding: utf-8 -*-
import sys
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
    
n, m = map(int,sys.stdin.readline().split())
parent = [0] * (n + 1)

edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i
    
for i in range(1, n+1):
    data = list(map(int,sys.stdin.readline().split()))
    for j in range(1, n+1):
        if data[j-1] == 1:
            union_parent(parent, i, j)

route = list(map(int,sys.stdin.readline().split()))
result = True
for i in range(len(route)-1):
    if parent[route[i]] != parent[route[i+1]]:
        result = False
    
if result:
    print("YES")
else:
    print("NO")

    