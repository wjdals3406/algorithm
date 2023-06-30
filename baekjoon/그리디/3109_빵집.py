import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
data = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dir = [(-1,1), (0,1), (1,1)] #오위, 오, 오아
res = 0
#원웅이가 놓을 수 있는 파이프라인의 최대 개수를 출력
#각 칸은 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선으로 연결 가능
#경로는 겹칠 수 없고, 서로 접할 수도 없음
#각 칸을 지나는 파이프는 단 하나여야 함
#출발하는 것마다 가장 위로 보내면 됨

def dfs(x, y):
    if y == m-1:
        return 1
    
    for d in range(3):
        nx = x + dir[d][0]
        ny = y + dir[d][1]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m or data[nx][ny] != "." or visited[nx][ny]:
            continue
        
        visited[nx][ny] = 1
        if dfs(nx, ny):
            return 1
    
    return 0

    
#행마다 dfs    
for i in range(n):
    res += dfs(i, 0)
print(res)