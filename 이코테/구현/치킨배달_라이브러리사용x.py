# -*- coding: utf-8 -*-
import sys
from itertools import combinations
import copy
n, m = map(int,sys.stdin.readline().split())
city = [[0 for _ in range(1)] for _ in range(n+1)] 

def cal_distance(house, chicken):
    x = abs(house[0] - chicken[0])
    y = abs(house[1] - chicken[1])
    return x + y

def pick( items, n, picked, picked_size, toPick , comblist) :
    #m = picked_size
    if toPick == 0 : 
        newitem = copy.deepcopy(picked)
        for i in range(len(newitem)):
            newitem[i] = items[picked[i]]
            
        comblist.append(newitem)
        return comblist
    lastIndex = picked_size - toPick - 1 # 가장 최근에 뽑힌 수가 저장된 위치 index
    if picked_size == toPick :
        smallest = 0; 
    else :
        smallest = picked[lastIndex] + 1
    for i in range(smallest, n):
        picked[lastIndex + 1] = i
        comblist= pick(items, n, picked, picked_size, toPick - 1, comblist) 
    
    return comblist
    

for i in range(1,n+1):
    city[i] += (list(map(int,sys.stdin.readline().split())))

chicken = [] 
for i in range(1, n+1): # 치킨 집 좌표 리스트에 넣기
    for j in range(1,n+1):
        if city[i][j] == 2:
            chicken.append([i,j])
            
picked = [0 for _ in range(m)]
comblist = []
comb= pick( chicken, len(chicken), picked, m, m , comblist)
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