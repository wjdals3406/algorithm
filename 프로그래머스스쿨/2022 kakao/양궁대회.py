#라이언에게 불리하게
#모든지 점수가 같으면 어피치가 우승 / 점수 획득
#라이언이 가장 큰 점수 차이로 우승하기 위해 어떤 과녁 점수에 맞혀야 하는지
#만약 라이언 우승 불가면(비기거나 질 때) [-1] return
from itertools import combinations_with_replacement
from collections import Counter

def min_list(a,b):
    for i in range(10,-1,-1):
        if a[i] > b[i]:
            return a
        elif a[i] < b[i]:
            return b

def solution(n, info):
    data = list(combinations_with_replacement(range(11), n))
    diff = 0
    rlist = []
    
    for case in data:
        lion = 0
        apeach = 0
        numlist = [0] * 11
        cdic = Counter(case)
        for key in cdic.keys():
            numlist[10-key] = cdic[key]
        
        for k in range(11):
            if info[k] == numlist[k] and info[k] == 0:
                continue
            if info[k] < numlist[k]:
                lion += 10-k
            else:
                apeach += 10-k
              
        if diff <= (lion-apeach) :
            if diff == lion-apeach and rlist:
                rlist = min_list(rlist, numlist)
            else:  
                diff = lion-apeach
                rlist = numlist
                
    if diff == 0: 
        return [-1]
    
    return rlist