# -*- coding: utf-8 -*-
import sys
from itertools import combinations
l,c = map(int, sys.stdin.readline().split()) # len이 l인 단어 만들기, 총 c 종류의 알파벳
words = list(map(str, sys.stdin.readline().split()))
five = [] #최소 한 개
others = []#최소 두 개
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
        

