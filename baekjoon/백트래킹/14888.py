# -*- coding: utf-8 -*-
# ��Ʈ��ŷ�� ��� ������ ����� �� �߿��� Ư���� ������ �����ϴ� ��츸 ���캸�� ��
# DFS ������ ��� ����� ���� Ž���ϴ� ��������, 
# ���ǹ� ���� �ɾ� ���� ����� �� �� ���� ��Ȳ�� �����ϰ�, 
# �׷��� ��Ȳ�� ��쿡�� Ž���� ������Ų �� 
# �� �������� ���ư��� �ٽ� �ٸ� ��츦 Ž���ϰԲ� ����
import sys
from itertools import permutations
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
calculate = list(map(int, sys.stdin.readline().split()))
clist = []
for i in range(4):
    for j in range(calculate[i]):
        clist.append(i)
ccom = list(set(permutations(clist, n-1)))
maxval = -int(1e9)
minval = int(1e9)
for i in ccom:
    sum = data[0]
    for j in range(n-1):
        if i[j] == 0:
            sum += data[j+1]
        elif i[j] == 1:
            sum -= data[j+1]
        elif i[j] == 2:
            sum *= data[j+1]
        elif i[j] == 3:
            if sum < 0:
                sum = -(abs(sum) // data[j+1])
            else:
                sum //= data[j+1]
    maxval = max(maxval, sum)
    minval = min(minval, sum)
    
print(maxval)
print(minval)   
    