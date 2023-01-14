from collections import deque
def solution(n, computers):
    visited = [0 for _ in range(n)] # ��Ʈ��ũ ����, 1�̻��� ���� ������
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if computers[i][j]:
                graph[i].append(j)
    
    def bfs(start,num):
        que = deque([start])
        visited[start] = num
        while que:
            node = que.popleft()
            for i in graph[node]:
                if not visited[i]:
                    visited[i] = num
                    que.append(i)
                
    num = 1
    for i in range(n):
        if not visited[i]:
            bfs(i,num)
        num += 1
    
    
    return len(set(visited))