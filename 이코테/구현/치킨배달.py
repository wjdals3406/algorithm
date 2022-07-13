# -*- coding: utf-8 -*-
import sys
from itertools import combinations
n, m = map(int,sys.stdin.readline().split())
city = [[0 for _ in range(1)] for _ in range(n+1)] 
#500ms안에로 시간 단축하기
#combination 라이브러리 사용하지 않기 => 재귀로
def cal_distance(house, chicken):
    x = abs(house[0] - chicken[0])
    y = abs(house[1] - chicken[1])
    return x + y

for i in range(1,n+1):
    city[i] += (list(map(int,sys.stdin.readline().split())))

chicken = [] 
for i in range(1, n+1): # 치킨 집 좌표 리스트에 넣기
    for j in range(1,n+1):
        if city[i][j] == 2:
            chicken.append([i,j])

comb = list(combinations(chicken, m))
total_min = 9999
distance = []         
            
for d in comb:
    for i in range(1, n+1): 
        for j in range(1,n+1):
            if city[i][j] == 1:
                minval = 99999 
                for k in d: # [[2,3], [3,4], [5,6]]                
                    minval=min(minval, cal_distance([i,j], k))
                distance.append(minval)
    total_min = min(total_min,sum(distance))    
    distance = []     

print(total_min)