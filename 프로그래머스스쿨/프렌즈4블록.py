# -*- coding: utf-8 -*-
# ���̽㿡���� �̷��� x2[i][j] == x2[i][j + 1] == x2[i + 1][j] == x2[i + 1][j + 1]���� ==�� ���� ����
# and�� �� ���� ���ص� ��
def make_count(m,n,board,dx,dy):
    remove_list = []
    for x in range(m-1):
        for y in range(n-1):
            if board[x][y] == '0':
                continue
            for i in range(3):
                flag = 1
                nx = dx[i] + x
                ny = dy[i] + y

                if board[x][y] != board[nx][ny]:
                    flag = 0
                    break
            if i == 2 and flag:
                remove_list.append((x,y))
                for i in range(3):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    remove_list.append((nx,ny))

    return list(set(remove_list))
    
def remove(remove_list,res,board,m,n):
    res += len((remove_list))
    
    for x,y in remove_list:
        board[x][y] = '0'
    for c in range(n):
        cnt = 0
        flag = 0
        for r in range(m-1,-1,-1):
            if board[r][c] == '0':
                cnt += 1
                flag = 1
                continue
            if flag:
                board[r+cnt][c] , board[r][c] = board[r][c], '0'
                
    return res
            
def solution(m, n, board):
    board = [list(i) for i in board]
    res = 0
    dx = [0,1,1] #��, ��, �밢�� ��
    dy = [1,0,1]
    
                
    while True:
        remove_list = make_count(m,n,board,dx,dy)
        if len(remove_list) == 0:
            break
        res = remove(remove_list,res,board,m,n)
    
    return res

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))