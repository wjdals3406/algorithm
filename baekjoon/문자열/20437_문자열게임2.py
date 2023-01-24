# -*- coding: utf-8 -*-
import sys
from collections import Counter,defaultdict
#어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이 -> 결국 앞과 뒤가 해당 문자여야 함
#어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이

k = int(sys.stdin.readline())
for _ in range(k):
    word = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    wcnt = Counter(word)
    dic = defaultdict(list)
    for key,val in wcnt.items():
        if val >= n:
            for i in range(len(word)):
                if word[i] == key:
                    dic[key].append(i)
    
    res = []
    for key,val in dic.items():
        s,e = 0,n-1
        d = dic[key]
        while e < len(d):  
            res.append(d[e] - d[s] + 1)
            s += 1
            e += 1
    if len(res) == 0:
        print(-1)
    else:
        print(min(res), max(res))
        