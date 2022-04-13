# -*- coding: utf-8 -*-
from collections import deque

v = int(input())

indegree = [0] * (v + 1) #�������� 0���� �ʱ�ȭ
graph = [[] for _ in range(v + 1)] #���Ḯ��Ʈ �ʱ�ȭ

#�Ųٷ� �־���� ��
for i in range(1, v+1):
    input_list = list(map(int, input().split()))
    graph[i].append(input_list[0])
    
    for j in input_list[1:-1]: #���ǽð�, ���� ���� ��ȣ��, -1 / ù��° �� -> ù��° ����
        graph[j].append(i) 
        indegree[i] += 1
            
sum_list = [0] * (v+1)
def topology_sort():
    # result = []
    q = deque()
    
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()  #1
        sum_list[now] += graph[now][0]
            
        for i in graph[now][1:]:
            indegree[i] -= 1
            sum_list[i] = max(sum_list[now], sum_list[now])
            if indegree[i] == 0:
                q.append(i)
                
        
topology_sort()
for i in sum_list[1:]:
    print(i)