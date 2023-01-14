from collections import deque
def solution(n, computers):
    visited = [0 for _ in range(n)] # ��Ʈ��ũ ����, 1�̻��� ���� ������
    
    def bfs(start,num):
        que = deque([start])
        visited[start] = num
        while que:
            node = que.popleft()
            for i in range(n): 
                if not visited[i] and computers[node][i] == 1:
                    visited[i] = num
                    que.append(i)
                
    num = 1
    for i in range(n):
        if not visited[i]:
            bfs(i,num)
        num += 1
    
    return len(set(visited))
