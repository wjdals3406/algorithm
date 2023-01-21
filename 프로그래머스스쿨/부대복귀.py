from collections import deque
def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)
    
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    que = deque([destination])
    visited[destination] += 1
    while que:
        node = que.popleft()
 
        for i in graph[node]:
            if visited[i] == -1:
                que.append(i)
                visited[i] = visited[node] + 1
                    
    return [visited[i] for i in sources]