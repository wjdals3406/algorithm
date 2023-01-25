# -*- coding: utf-8 -*-
import sys
from collections import Counter,defaultdict
#� ���ڸ� ��Ȯ�� K���� �����ϴ� ���� ª�� ���� ���ڿ��� ���� -> �ᱹ �հ� �ڰ� �ش� ���ڿ��� ��
#� ���ڸ� ��Ȯ�� K���� �����ϰ�, ���ڿ��� ù ��°�� ������ ���ڰ� �ش� ���ڷ� ���� ���� �� ���� ���ڿ��� ����

t = int(sys.stdin.readline())
for _ in range(t):
    word = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline())
    wcnt = Counter(word)
    dic = defaultdict(list)
    
    #���ڸ� k�� �̻� ������ �ִ� ��� �߸���
    for key,val in wcnt.items():
        if val >= k:
            for i in range(len(word)):
                if word[i] == key:
                    dic[key].append(i)
    #dic -> {'u': [1, 7], 'r': [4, 11], 'a': [5, 8, 13], 'o': [10, 15]})
    
    #���ڿ��� ���� ���ϱ�
    res = []
    for key,val in dic.items():
        s,e = 0,k-1
        d = dic[key]
        while e < len(d):  
            res.append(d[e] - d[s] + 1) #�ε��� ���� ���� ���� ���ӵ� ���ڿ� ���̸� ���� �� ����
            s += 1
            e += 1
            
    if len(res) == 0:
        print(-1)
    else:
        print(min(res), max(res))
        