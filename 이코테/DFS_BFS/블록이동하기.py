# -*- coding: utf-8 -*-
def rotate_90(data, start, end): #시계방향(축이 start 기준) # 밑으로 회전
    n = len(data)
    #대각선에 1이 없는지 확인
    if end[0]+1 < n and data[end[0]+1][end[1]] != 1 and data[start[0]+1][start[1]] != 1:
        end = (start[0]+1, start[1])
        return end, start 
    return -1, -1 #rotate 못함

def rotate_270(data, start, end): #반시계방향(축이 end 기준) # 밑으로 회전
    n = len(data)
    #대각선에 1이 없는지 확인
    if start[0]+1 < n and data[start[0]+1][start[1]] != 1 and data[end[0]+1][end[1]] != 1:
        start = (end[0]+1, end[1])
        return start, end
    return -1, -1 #rotate 못함

def solution(data):
    start = (0,0)
    end = (0,1)
    
    while data[end[0]][end[1]] != 1:
        end = (end[0], end[1]+1)
    start, end = rotate_90(data, start, end)
    if start == -1:
            #행동 취소함


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))