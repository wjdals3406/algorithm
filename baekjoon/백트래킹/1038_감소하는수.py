# -*- coding: utf-8 -*-
import sys
k = int(sys.stdin.readline())
dp = [[1] * 10 for _ in range(k+1)]
#감소하는 수, 숫자가 중복되면 안됨 ex) 322(x) / 321(ok)
#결국 거꾸로 하면 증가하는 수니까 증가하는 수를 만들면 됨

alist = ['0','1','2','3','4','5','6','7','8','9']
cnt = -1
def pick(arr, n, num):
    global cnt
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for rest in pick(alist[:i], n - 1, num):
            result.append([elem] + rest)
            
            if len([elem] + rest) == num:
                cnt += 1

            if cnt == k:
                return ''.join(result[-1])
                
    return result

flag = 0
for i in range(1,11): 
    res = pick(alist, i, i)

    if type(res) == type(''):
        flag = 1
        break
        
if not flag:
    print(-1)
else:
    print(res) 
