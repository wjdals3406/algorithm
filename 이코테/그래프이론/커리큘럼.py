# -*- coding: utf-8 -*-
from collections import deque

v = int(input())

indegree = [0] * (v + 1) #�������� 0���� �ʱ�ȭ
graph = [[] for _ in range(v + 1)] #���Ḯ��Ʈ �ʱ�ȭ

#���� ���� -1�� �ƴϸ� ���� �־�� ��
for i in range(1, v+1):
    input_list = list(map(int, input().split()))
    for j, jval in enumerate(input_list): #���ǽð�, ���� ���� ��ȣ��, -1 / ù��° �� -> ù��° ����
        if jval == -1:
            break
        
        graph[i].append(jval) # ���ǽð�, ���� ���� ��ȣ��
        if input_list[j+1] != -1:
            indegree[input_list[j+1]] += 1
    
def topology_sort():
    result = []
    sum = 0
    q = deque()
    
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()  #1
        result.append(now)
        
        for i in graph[now][1:]:
            sum += i
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                
        # if len(graph) == 1: #���� ������ �־������
        print(sum)
        sum = 0
                
    # for i in result:
    #     print(i)
        
topology_sort()