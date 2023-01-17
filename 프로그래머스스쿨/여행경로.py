# -*- coding: utf-8 -*-
from collections import defaultdict
def solution(tickets):
    answer = []
    t = defaultdict(list) #������� key, �������� value�� ��ųʸ�
    for s,d in tickets:
        t[s].append(d)

    for key in t.keys():
        t[key].sort(reverse=True) #������ �Ųٷ� ���� -> pop �ϱ� ����

    #���� : ICN
    def dfs():
        stack = ['ICN']
        while stack:
            start = stack[-1]
            if not t[start]:# start���� ����ϴ� �װ����� ���°�� �ٷ� �信 �ֱ�
                answer.append(stack.pop())
            else : stack.append(t[start].pop())
    dfs()

    return answer[::-1]
