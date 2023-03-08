def solution(n, costs):
    answer = 0

    def find_parent(parent,x):
        if parent[x] != x:
            parent[x] = find_parent(parent,parent[x])
        return parent[x]

    def union_parent(parent,a,b):
        a = find_parent(parent,a)
        b = find_parent(parent,b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    edge = []
    parent = [x for x in range(n)]

    for a,b,cost in costs:
        edge.append((cost,a,b))

    edge.sort()

    for cost,a,b in edge:
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            answer += cost

    return answer