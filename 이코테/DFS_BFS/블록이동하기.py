# -*- coding: utf-8 -*-
def rotate_90(data, start, end): #�ð����(���� start ����) # ������ ȸ��
    n = len(data)
    #�밢���� 1�� ������ Ȯ��
    if end[0]+1 < n and data[end[0]+1][end[1]] != 1 and data[start[0]+1][start[1]] != 1:
        end = (start[0]+1, start[1])
        return end, start 
    return -1, -1 #rotate ����

def rotate_270(data, start, end): #�ݽð����(���� end ����) # ������ ȸ��
    n = len(data)
    #�밢���� 1�� ������ Ȯ��
    if start[0]+1 < n and data[start[0]+1][start[1]] != 1 and data[end[0]+1][end[1]] != 1:
        start = (end[0]+1, end[1])
        return start, end
    return -1, -1 #rotate ����

def solution(data):
    start = (0,0)
    end = (0,1)
    
    while data[end[0]][end[1]] != 1:
        end = (end[0], end[1]+1)
    start, end = rotate_90(data, start, end)
    if start == -1:
            #�ൿ �����


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))