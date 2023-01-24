from collections import deque
def solution(maps):
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    n,m = len(maps), len(maps[0])
    #n-1, m-1로 이동해야 함
    #현재는 0,0에 위치
    
    def bfs():
        que = deque([[0,0,1]])
        visited[0][0] = 1
        
        while que:
            x,y,num = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >=n or ny < 0 or ny >=m:
                    continue
                if not visited[nx][ny] and maps[nx][ny]:
                    que.append((nx,ny,num + 1))
                    visited[nx][ny] = 1
                    if nx == n-1 and ny == m-1:
                        return num + 1
        return -1
                        
    
    return bfs()
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))