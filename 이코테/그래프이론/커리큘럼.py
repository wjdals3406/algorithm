# -*- coding: utf-8 -*-
from collections import deque

v = int(input())

indegree = [0] * (v + 1) #진입차수 0으로 초기화
graph = [[] for _ in range(v + 1)] #연결리스트 초기화

#거꾸로 넣어줘야 함
for i in range(1, v+1):
    input_list = list(map(int, input().split()))
    graph[i].append(input_list[0])
    
    for j in input_list[1:-1]: #강의시간, 선수 강의 번호들, -1 / 첫번째 줄 -> 첫번째 강의
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