# -*- coding: utf-8 -*-
n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
# board = [[[-1]]*(n+1)] *(n+1) #-> 이렇게 배열 초기화하면 안됨 
# board = [[-1] for _ in range(n+1)] * (n+1)
#=> https://leedakyeong.tistory.com/entry/Python-2-dimension-list 참고하기

board = [[[-1] for _ in range(n+1)] for _ in range(n+1)] 
# bo = [[[-1] for _ in range(n+1)] for _ in range(n+1)]
# pil = [[[-1] for _ in range(n+1)] for _ in range(n+1)]
for x,y,a,b in build_frame:
    if b == 0 : # 삭제
        if len(board[x][y]) > 1:
            board[x][y].remove(-1)
            for i in board[x][y]:
                if i[2] == a:
                    # tmp = board[x][y]
                    if a == 0: #기둥
                        if (x > 0 and board[x-1][y][-1]==1) or (x < n and board[x+1][y][-1]==1 or (y > 0 and board[x][y-1][-1] == 0)):
                                board[x][y].remove(board[x][y])
                    elif a == 1 : #보
                        if (y > 0 and board[x][y-1][-1] == 0) or (x < n and board[x][y-1][-1] == 0) or ((x > 0 and x < n and board[x-1][y][-1]==1) or (x > 0 and x < n and board[x+1][y][-1]==1)):
                                board[x][y].remove(board[x][y])
    else: # 추가
        if y == 0 and a == 1: # 바닥에는 기둥만 있어야 함
            continue
        elif y == 0 and a == 0:
            board[x][y].append([x,y,a])
        elif a == 0: #기둥
            if x == 0:
                if board[x-1][y][-1]==1:
                    board[x][y].append([x,y,a])
            elif x < n:
                if board[x+1][y][-1]==1:
                    board[x][y].append([x,y,a])
            elif y > 0:
                if board[x][y-1][-1] == 0 : 
                    board[x][y].append([x,y,a])

        elif a == 1 : #보
            if y > 0:
                if board[x][y-1][-1] == 0 : 
                    board[x][y].append([x,y,a])
            elif x > 0 and x < n:
                if board[x-1][y][-1]==1 and board[x+1][y][-1]==1:
                    board[x][y].append([x,y,a])
            elif x < n:
                if board[x+1][y-1][-1] == 0 : 
                    board[x][y].append([x,y,a])
            

answer = []
for i in board:
    for j in i:
        for k in j:
            if k != -1:
                answer.append(k)
                    

answer = sorted(answer, key = lambda x : (x[0], x[1], x[2]))

print(board)     
print(answer)
                 
        