# -*- coding: utf-8 -*-
import sys
from collections import Counter,defaultdict
#� ���ڸ� ��Ȯ�� K���� �����ϴ� ���� ª�� ���� ���ڿ��� ���� -> �ᱹ �հ� �ڰ� �ش� ���ڿ��� ��
#� ���ڸ� ��Ȯ�� K���� �����ϰ�, ���ڿ��� ù ��°�� ������ ���ڰ� �ش� ���ڷ� ���� ���� �� ���� ���ڿ��� ����

k = int(sys.stdin.readline())
for _ in range(k):
    word = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    wcnt = Counter(word)
    dic = defaultdict(list)
    for key,val in wcnt.items():
        if val >= n:
            for i in range(len(word)):
                if word[i] == key:
                    dic[key].append(i)
    
    res = []
    for key,val in dic.items():
        s,e = 0,n-1
        d = dic[key]
        while e < len(d):  
            res.append(d[e] - d[s] + 1)
            s += 1
            e += 1
    if len(res) == 0:
        print(-1)
    else:
        print(min(res), max(res))
        