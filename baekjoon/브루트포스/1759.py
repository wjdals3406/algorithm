# -*- coding: utf-8 -*-
import sys
from itertools import combinations
l,c = map(int, sys.stdin.readline().split()) # len�� l�� �ܾ� �����, �� c ������ ���ĺ�
words = list(map(str, sys.stdin.readline().split()))
five = [] #�ּ� �� ��
others = []#�ּ� �� ��
for i in words:
    if i in ('a', 'e', 'i', 'o', 'u'):
        five.append(i)
    else:
        others.append(i)

res = []
for i in range(len(five)):
    f_num = i+1
    o_num = l - (f_num)
    if o_num < 2:
        break
    fd = list(combinations(five, f_num))
    od = list(combinations(others, o_num))
    for f in fd:
        for o in od:
            res.append(''.join(sorted(f + o)))
print('\n'.join(map(str, sorted(res))))
        

