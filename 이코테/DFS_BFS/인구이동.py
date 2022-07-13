# -*- coding: utf-8 -*-
import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
def check_gap(curr, curc, movr, movc):
    if check[movr][movc] == 1:
        return
    gap = abs(data[movr][movc] - data[curr][curc])
    if gap >= low and gap <= high:
        check[movr][movc] = 1
        move(movr, movc)

def move(r, c):
    visited[r][c] = 1
    if r < n-1:
        check_gap(r, c, r+1, c)
    if r > 0:
        check_gap(r, c, r-1, c)
    if c > 0:
        check_gap(r, c, r, c-1)
    if c < n-1:
        check_gap(r, c, r, c+1)
    return

def make_sum():
    vsum = 0
    for s in visited:
        vsum += sum(s)
    return vsum

n, low, high= map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

result = 0
while True: 
    flag = 1
    visited = [[0 for _ in range(n)] for _ in range(n)]

    data_copy=copy.deepcopy(data)
    for i in range(n):
        for j in range(n):
            check = [[0 for _ in range(n)] for _ in range(n)]
            if visited[i][j]: continue
            check[i][j] = 1
            move(i, j) 
            
            ssum = 0
            count = 0
            for k in range(n):
                for l in range(n):
                    if check[k][l] == 1:
                        ssum += data[k][l]
                        count += 1
            if count == 1: 
                vsum = make_sum()
                if  vsum != n*n: #visited가 모두 1이 아닐 때
                    continue
                else:
                    if vsum == n*n and flag == 0: 
                        result+=1
                        data = data_copy
                        break
                    else: # vsum == n*n인데 flag == 1일 때
                        break
            else:
                flag = 0
                
            ssum=ssum//count

            for k in range(n):
                for l in range(n):
                    if check[k][l] == 1:
                        data_copy[k][l] = ssum
                        
            #visited가 다 1이면 result +=1 
            vsum = make_sum()
            if vsum == n*n and flag == 0: 
                data = data_copy 
                result+=1
                break
        #행, 열 다 idx 0으로 초기화
        if vsum == n*n:
            break
                        
    if flag == 1:
        break
    
print(result)