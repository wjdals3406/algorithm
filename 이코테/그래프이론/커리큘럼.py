# -*- coding: utf-8 -*-
from collections import deque

v = int(input())

indegree = [0] * (v + 1) #진입차수 0으로 초기화
graph = [[] for _ in range(v + 1)] #연결리스트 초기화

#뒤의 값이 -1이 아니면 값을 넣어야 함
for i in range(1, v+1):
    input_list = list(map(int, input().split()))
    for j, jval in enumerate(input_list): #강의시간, 선수 강의 번호들, -1 / 첫번째 줄 -> 첫번째 강의
        if jval == -1:
            break
        
        graph[i].append(jval) # 강의시간, 선수 강의 번호들
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
                
        # if len(graph) == 1: #연결 정보를 넣어놔야함
        print(sum)
        sum = 0
                
    # for i in result:
    #     print(i)
        
topology_sort()