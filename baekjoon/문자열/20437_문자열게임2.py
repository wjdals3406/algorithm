# -*- coding: utf-8 -*-
import sys
from collections import Counter,defaultdict
#어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이 -> 결국 앞과 뒤가 해당 문자여야 함
#어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이

t = int(sys.stdin.readline())
for _ in range(t):
    word = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline())
    wcnt = Counter(word)
    dic = defaultdict(list)
    
    #문자를 k개 이상 가지고 있는 경우 추리기
    for key,val in wcnt.items():
        if val >= k:
            for i in range(len(word)):
                if word[i] == key:
                    dic[key].append(i)
    #dic -> {'u': [1, 7], 'r': [4, 11], 'a': [5, 8, 13], 'o': [10, 15]})
    
    #문자열의 길이 구하기
    res = []
    for key,val in dic.items():
        s,e = 0,k-1
        d = dic[key]
        while e < len(d):  
            res.append(d[e] - d[s] + 1) #인덱스 값을 빼줘 쉽게 연속된 문자열 길이를 구할 수 있음
            s += 1
            e += 1
            
    if len(res) == 0:
        print(-1)
    else:
        print(min(res), max(res))
        