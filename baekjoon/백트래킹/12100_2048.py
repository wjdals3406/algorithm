# -*- coding: utf-8 -*-
#최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록 출력
import sys
import copy
input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
maxvalue = 2

def maxval(data):
    return max(map(max,data))

def dfs(cnt,cp_data):
    global maxvalue
    
    if cnt == 5:
        maxvalue = max(maxvalue, maxval(cp_data))
        return 
    
    for i in range(4):
        check = [[0] * n for _ in range(n)]
        data = copy.deepcopy(cp_data)
        
        if i == 1: #밑으로 이동
            for j in range(n):
                ex = n-2
                sx = n-1
                while ex >= 0:
                    while data[ex][j] == 0 and ex > 0:
                        ex -= 1
                    if data[ex][j] == data[sx][j] and check[sx][j] != 1:
                        data[ex][j] = 0
                        data[sx][j] = data[sx][j] * 2
                        check[sx][j] = 1
                        
                    else:
                        temp = data[ex][j]
                        data[ex][j] = 0
                        if data[sx][j] == 0:
                            sx += 1
                        data[sx-1][j] = temp
                        sx -= 1
                    
                    ex -= 1
                    
        elif i == 2: #위로 이동
            for j in range(n):
                ex = 1
                sx = 0
                while ex < n:
                    while data[ex][j] == 0 and ex < n-1:
                        ex += 1
                    if data[ex][j] == data[sx][j] and check[sx][j] != 1:
                        data[ex][j] = 0
                        data[sx][j] = data[sx][j] * 2
                        check[sx][j] = 1
                        
                    else:
                        temp = data[ex][j]
                        data[ex][j] = 0
                        if data[sx][j] == 0:
                            sx -= 1
                        data[sx+1][j] = temp
                        sx += 1
                    
                    ex += 1
                    
        elif i == 3: #오른쪽으로 이동
            for j in range(n):
                ey = n-2
                sy = n-1
                while ey >= 0:
                    while data[j][ey] == 0 and ey > 0:
                        ey -= 1
                    if data[j][ey] == data[j][sy] and check[j][sy] != 1:
                        data[j][ey] = 0
                        data[j][sy] = data[j][sy] * 2
                        check[j][sy] = 1
                        
                    else:
                        temp = data[j][ey]
                        data[j][ey] = 0
                        if data[j][sy] == 0:
                            sy += 1
                        data[j][sy-1] = temp
                        sy -= 1
                    
                    ey -= 1
                    
        elif i == 0: #왼쪽으로 이동
            for j in range(n):
                ey = 1
                sy = 0
                while ey < n:
                    while data[j][ey] == 0 and ey < n-1:
                        ey += 1
                    if data[j][ey] == data[j][sy] and check[j][sy] != 1:
                        data[j][ey] = 0
                        data[j][sy] = data[j][sy] * 2
                        check[j][sy] = 1
                        
                    else:
                        temp = data[j][ey]
                        data[j][ey] = 0
                        if data[j][sy] == 0:
                            sy -= 1
                        data[j][sy+1] = temp
                        sy += 1
                    
                    ey += 1
            
        dfs(cnt+1, data)

  
dfs(0,copy.deepcopy(data))
            
print(maxvalue)
