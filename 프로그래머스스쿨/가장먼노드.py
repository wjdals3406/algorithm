from collections import defaultdict, deque
def solution(n, edge):
    #�ִܰ�η� �̵����� ��, ������ ������ ���� ���� ���
    #1�� ��忡�� ���
    #�����
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