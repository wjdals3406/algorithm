# -*- coding: utf-8 -*-
from collections import defaultdict
def solution(tickets):
    answer = []
    t = defaultdict(list) #출발지가 key, 도착지가 value인 딕셔너리
    for s,d in tickets:
        t[s].append(d)

    for key in t.keys():
        t[key].sort(reverse=True) #사전순 거꾸로 정렬 -> pop 하기 위해

    #시작 : ICN
    def dfs():
        stack = ['ICN']
        while stack:
            start = stack[-1]
            if not t[start]:# start에서 출발하는 항공편이 없는경우 바로 답에 넣기
                answer.append(stack.pop())
            else : stack.append(t[start].pop())
    dfs()

    return answer[::-1]
