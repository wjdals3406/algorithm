# -*- coding: utf-8 -*-
import sys
n,l = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)] # 경사로 놓은 곳 체크해두기
def rotate_90():
    ret = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            ret[c][n-1-r] = data[r][c]
    return ret

res = 0
def func():
    global res
    for i in range(n): 
        cnt = 1
        j = 0
        flag = 0
        while j < n-1: # 2 1 1 1 1 2
            if abs(data[i][j] - data[i][j+1]) > 1: #경사로 놓을 수 없는 경우
                break
            elif abs(data[i][j] - data[i][j+1]) == 1: # 경사로를 높을 수 있는 경우
                if data[i][j] > data[i][j+1]:
                    subj = j
                    j += 1
                    cnt = 1
                    while j < n-1 and data[i][j] == data[i][j+1]:
                        cnt += 1
                        j+=1
                    if cnt < l or visited[i][subj + l]: #경사로가 놓여져 있다면
                        flag = 1
                        break
                    for k in range(1,l+1):
                        visited[i][subj + k] = 1 
                   
                    cnt -= l
                    if cnt <=0:
                        cnt = 1
                    continue
                
                elif data[i][j] < data[i][j+1]:
                    if cnt < l or visited[i][(j+1)-l]: #경사로가 놓여져 있다면
                        flag = 1
                        break
                    for k in range(1,l+1):
                        visited[i][(j+1)-k] = 1 
                    cnt = 1
            else:
                cnt += 1
            j += 1
        if j == n-1 and flag == 0:
            res += 1
        
func()
data = rotate_90()
visited = [[0] * n for _ in range(n)]
func()
print(res)