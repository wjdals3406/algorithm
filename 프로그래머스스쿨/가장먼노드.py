from collections import defaultdict, deque
def solution(n, edge):
    #최단경로로 이동했을 때, 간선의 개수가 가장 많은 노드
    #1번 노드에서 출발
    #양방향
    visited = [-1] * (n+1)
    graph = defaultdict(list)
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)

    def bfs():
        que = deque([1])
        visited[1] = 0
        
        while que:
            node = que.popleft()
            
            for i in graph[node]:
                if visited[i] == -1:
                    visited[i] = visited[node]+1
                    que.append(i)
                    
    bfs()    
    return visited.count(max(visited))