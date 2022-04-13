# -*- coding: utf-8 -*-

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
    
v, e = map(int, input().split()) # v : ���, e : ����
parent = [[0] for _ in range(v + 1)]

for i in range(1, v+1):
    parent[i] = i

print_array = []
for i in range(e):
    check, a, b = map(int, input().split())
    
    if check == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print_array.append("YES")
        else:
            print_array.append("NO")
            
for i in print_array:
    print(i)
