# -*- coding: utf-8 -*-
import sys
import copy
from itertools import combinations

def find(curr, curc, dc):#while�� 1~2���� �ٿ����� -> dx,dy ����ϱ�/ �ۿ��� for�� ������
    r, c = curr,curc
    if r < n-1:
        while dc[r][c] != 'O' and r<n-1:
            r+=1
            if dc[r][c] == 'S':
                return 0
    r, c = curr,curc
    if r > 0:
        while dc[r][c] != 'O' and r>0:
            r-=1
            if dc[r][c] == 'S':
                return 0
    r, c = curr,curc
    if c > 0:
        while dc[r][c] != 'O' and c>0:
            c-=1
            if dc[r][c] == 'S':
                return 0
    r, c = curr,curc
    if c < n-1:
        while dc[r][c] != 'O' and c<n-1:
            c+=1
            if dc[r][c] == 'S':
                return 0
    return 1
    
n = int(input())
data = [list(map(str, input().split())) for _ in range(n)]

empty = []
teacher = []
for r in range(n):
    for c in range(n):
        if data[r][c] == 'X':
            empty.append((r,c))
        if data[r][c] == 'T':
            teacher.append((r,c))
            
comb = list(combinations(empty, 3))

for i in comb:
    flag = 1
    dc =copy.deepcopy(data)
    for j in i:
        dc[j[0]][j[1]] = 'O' #��ֹ� 3�� ����
        
    for t in teacher:
        #��, �Ʒ�, ��, �� �� Ȯ���غ�
        if find(t[0], t[1], dc) == 0: # NO
            flag = 0
            break
    if flag == 1:
        print("YES")
        break
   
if flag == 0:
    print("NO")
