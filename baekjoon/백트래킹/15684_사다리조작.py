# -*- coding: utf-8 -*-
#풀이1
import sys
h, line, w = map(int, sys.stdin.readline().split())
data = [[-1] * (h+1) for _ in range(w+2)] #사다리가 끝나는 지점은 w+1인 지점임

for _ in range(line):#0은 시작, 1은 정점
    a,b = map(int, sys.stdin.readline().split())
    data[a][b] = 0 #오른쪽으로 이동
    data[a][b+1] = 1 #왼쪽으로 이동

def is_same():
    for i in range(1,h+1): #각 세로선마다 확인
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

#정답이 3보다 큰 값이면 -1을 출력한다
def make_line(startW, count):
    if count == 0:
        if is_same():
            return 1
        return 0
    
    for r in range(startW, w+1): #
        for c in range(1, h):
            if data[r][c] == -1 and data[r][c+1] == -1: #아무 선이 이어져있지 않으면
                data[r][c], data[r][c+1] = 0, 1
                if make_line(r, count - 1):
                    return 1
                data[r][c], data[r][c+1] = -1, -1
            
        
    return 0

#선을 몇 개 추가할 것인지
if is_same():
    print(0)
else:   
    flag = 0
    for i in range(1,4):
        if make_line(1, i):
            print(i)
            flag = 1
            break
        
    if not flag:
        print(-1)
        
#풀이2
# import sys
# from itertools import combinations
# h, line, w = map(int, sys.stdin.readline().split())
# data = [[-1] * (h+1) for _ in range(w+2)] #w는 1부터 w까지 선이 그어질 수 있으므로 w+1까지 행을 생성해야 함 / 이때, 인덱스에 편리하게 접근하기 위해 1씩 더함

# for _ in range(line):#0은 시작, 1은 정점
#     a,b = map(int, sys.stdin.readline().split())
#     data[a][b] = 0 #오른쪽으로 이동
#     data[a][b+1] = 1 #왼쪽으로 이동

# def is_same():
#     for i in range(1,h+1):
#         x,y = 1,i
#         while x <= w:
#             if data[x][y] == 0: #우측 하단으로 이동
#                 y += 1
#                 x += 1
#             elif data[x][y] == 1: #좌측 하단으로 이동
#                 y -= 1
#                 x += 1
#             elif data[x][y] == -1:
#                 x += 1 #밑으로 직진
#         if y != i:
#             return False
#     return True

# coordlist = []
# for i in range(1,w+1):
#     for j in range(1,h): #맨마지막 열은 리스트에 넣으면 안됨
#         coordlist.append([i,j])

# #정답이 3보다 큰 값이면 -1을 출력한다
# def make_line():
#     for i in range(1,4):
#         for one_case in combinations(coordlist, i):
#             flag = 0
#             for idx,value in enumerate(one_case):
#                 x,y = value
#                 if data[x][y] == -1 and data[x][y+1] == -1: #두 가로선이 연속하거나 서로 접하면 안됨
#                     data[x][y] = 0
#                     data[x][y+1] = 1
#                 else:
#                     flag = 1
#                     for ridx in range(idx):
#                         x,y = one_case[ridx]
#                         data[x][y] = -1
#                         data[x][y+1] = -1
#                     break #다른 케이스로 넘어감
                
#             # break문에서 빠져나온 값은 이거 실행되지/ 않고 바로 for문으로 가야 함
#             if flag: 
#                 continue
            
#             if is_same():
#                 return i
#             else:
#                 for x,y in one_case:
#                     data[x][y] = -1
#                     data[x][y+1] = -1

#     return -1

# if is_same():
#     print(0)
# else:   
#     print(make_line())
        