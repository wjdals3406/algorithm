import sys
VALUE = 21
dp = [[[0]*VALUE for _ in range(VALUE)] for _ in range(VALUE)]
for a in range(VALUE):
    for b in range(VALUE):
        for c in range(VALUE):
            if a <= 0 or b <= 0 or c <= 0:
                dp[a][b][c] = 1
            elif a < b and b < c : 
                dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
            else:
                dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20 : 
        return dp[20][20][20]
    return dp[a][b][c]
    
a,b,c = map(int, sys.stdin.readline().split())
while a!= -1 or b!=-1 or c!=-1:
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
    a,b,c = map(int, sys.stdin.readline().split())
    
