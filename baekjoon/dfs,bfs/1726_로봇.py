import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0,0,0,0] for _ in range(m)] for _ in range(n)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())
sx, sy, ex, ey = sx - 1, sy - 1 ,ex -1, ey - 1
sd, ed = sd -1, ed - 1
dx = (0, 0, 1, -1) # 동 서 남 북
dy = (1, -1, 0, 0)
change_dir = ((2, 3), (2, 3), (0, 1), (0, 1))

# 방향 마다 visited가 필요함
# 왼쪽 또는 오른쪽으로 90° 회전 (최대 1번 회전 가능 <- 이걸 캐치 못해서 틀렸다..^^)
# 한 방향으로 최대 k번 move
# 로봇을 도착 지점에 원하는 방향으로 이동시키는데 필요한 최소 명령 횟수
def bfs():
    que = deque([(sx, sy, 0, sd)])
    visited[sx][sy][sd] = 1

    while que:
        x, y, num, nd = que.popleft()
        
        if x == ex and y == ey and ed == nd:
            return num

        #같은 방향으로 최대 k번 
        for k in range(1,4):
            nx,ny = x + dx[nd]*k, y + dy[nd]*k
            if nx < 0 or nx >= n or ny < 0 or ny >= m or data[nx][ny]:
                break
            if not visited[nx][ny][nd]:
                visited[nx][ny][nd] = 1
                que.append((nx,ny, num+1, nd))
            
        #방향 바꾸기
        for d in change_dir[nd]:
            if visited[x][y][d]:
                continue
            
            visited[x][y][d] = 1
            que.append((x,y, num+1, d))
            
print(bfs())
            