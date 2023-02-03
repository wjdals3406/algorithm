# -*- coding: utf-8 -*-
#�ð��ʰ�
import sys
from itertools import combinations
import copy
h, line, w = map(int, sys.stdin.readline().split())
copy_data = [[-1] * (h+1) for _ in range(w+2)] #w�� 1���� w���� ���� �׾��� �� �����Ƿ� w+1���� ���� �����ؾ� �� / �̶�, �ε����� ���ϰ� �����ϱ� ���� 1�� ����
line_list = []
for _ in range(line):#0�� ����, 1�� ����
    a,b = map(int, sys.stdin.readline().split())
    copy_data[a][b] = 0 #���������� �̵�
    copy_data[a][b+1] = 1 #�������� �̵�
    line_list.append((a,b))
    line_list.append((a,b+1))

def is_same(data):
    for i in range(1,h+1):
        x,y = 1,i
        while x <= w:
            if data[x][y] == 0: #���� �ϴ����� �̵�
                y += 1
                x += 1
            elif data[x][y] == 1: #���� �ϴ����� �̵�
                y -= 1
                x += 1
            elif data[x][y] == -1:
                x += 1 #������ ����
        if y != i:
            return False
    return True

coordlist = []
for i in range(1,w+1):
    for j in range(1,h): #�Ǹ����� ���� ����Ʈ�� ������ �ȵ�
        if (i,j) not in line_list:
            coordlist.append([i,j])

#������ 3���� ū ���̸� -1�� ����Ѵ�
def make_line():
    for i in range(1,4):
        comb_list = list(combinations(coordlist, i))
        for one_case in comb_list:
            flag = 0
            # copy_data = copy.deepcopy(data) #�̰� �ð��� ���� �ҿ��
            for oindex in range(len(one_case)):
                x,y = one_case[oindex]
                if copy_data[x][y] == -1 and copy_data[x][y+1] == -1: #�� ���μ��� �����ϰų� ���� ���ϸ� �ȵ�
                    copy_data[x][y] = 0
                    copy_data[x][y+1] = 1
                else:
                    flag = 1
                    for iindex in range(oindex+1):
                        x,y = one_case[iindex]
                        copy_data[x][y] = -1
                        copy_data[x][y+1] = -1
                    break #�ٸ� ���̽��� �Ѿ
                
            # break������ �������� ���� �̰� �������/ �ʰ� �ٷ� for������ ���� ��
            if flag: 
                continue
            
            if is_same(copy_data):
                return i
            
            # for x,y in one_case: #�� ����� 
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
        