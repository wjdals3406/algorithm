# -*- coding: utf-8 -*-
#시간초과
import sys
from itertools import combinations
import copy
h, line, w = map(int, sys.stdin.readline().split())
copy_data = [[-1] * (h+1) for _ in range(w+2)] #w는 1부터 w까지 선이 그어질 수 있으므로 w+1까지 행을 생성해야 함 / 이때, 인덱스에 편리하게 접근하기 위해 1씩 더함
line_list = []
for _ in range(line):#0은 시작, 1은 정점
    a,b = map(int, sys.stdin.readline().split())
    copy_data[a][b] = 0 #오른쪽으로 이동
    copy_data[a][b+1] = 1 #왼쪽으로 이동
    line_list.append((a,b))
    line_list.append((a,b+1))

def is_same(data):
    for i in range(1,h+1):
        x,y = 1,i
        while x <= w:
            if data[x][y] == 0: #우측 하단으로 이동
                y += 1
                x += 1
            elif data[x][y] == 1: #좌측 하단으로 이동
                y -= 1
                x += 1
            elif data[x][y] == -1:
                x += 1 #밑으로 직진
        if y != i:
            return False
    return True

coordlist = []
for i in range(1,w+1):
    for j in range(1,h): #맨마지막 열은 리스트에 넣으면 안됨
        if (i,j) not in line_list:
            coordlist.append([i,j])

#정답이 3보다 큰 값이면 -1을 출력한다
def make_line():
    for i in range(1,4):
        comb_list = list(combinations(coordlist, i))
        for one_case in comb_list:
            flag = 0
            # copy_data = copy.deepcopy(data) #이게 시간이 많이 소요됨
            for oindex in range(len(one_case)):
                x,y = one_case[oindex]
                if copy_data[x][y] == -1 and copy_data[x][y+1] == -1: #두 가로선이 연속하거나 서로 접하면 안됨
                    copy_data[x][y] = 0
                    copy_data[x][y+1] = 1
                else:
                    flag = 1
                    for iindex in range(oindex+1):
                        x,y = one_case[iindex]
                        copy_data[x][y] = -1
                        copy_data[x][y+1] = -1
                    break #다른 케이스로 넘어감
                
            # break문에서 빠져나온 값은 이거 실행되지/ 않고 바로 for문으로 가야 함
            if flag: 
                continue
            
            if is_same(copy_data):
                return i
            
            # for x,y in one_case: #이 방식은 
            #     data[x][y] = -1
            #     data[x][y+1] = -1
            for iindex in range(oindex+1):
                x,y = one_case[iindex]
                copy_data[x][y] = -1
                copy_data[x][y+1] = -1
            
    return -1

if is_same(copy_data):
    print(0)
else:   
    print(make_line())
        