import sys
from collections import defaultdict
n, k, p, x = map(str, sys.stdin.readline().split())
p = int(p)
k = int(k)
#각 자리의 숫자를 효과적으로 비교하는 방법은?
numdic = {0: [1, 1, 1, 1, 1, 1, 0],
          1: [0, 0, 0, 1, 1, 0, 0],
          2: [0, 1, 1, 0, 1, 1, 1],
          3: [0, 0, 1, 1, 1, 1, 1],
          4: [1, 0, 0, 1, 1, 0, 1],
          5: [1, 0, 1, 1, 0, 1, 1],
          6: [1, 1, 1, 1, 0, 1, 1],
          7: [0, 0, 0, 1, 1, 1, 0],
          8: [1, 1, 1, 1, 1, 1, 1],
          9: [1, 0, 1, 1, 1, 1, 1]}

#num에서 onum으로 변환하기 위해 켜야하는 불
valdic = defaultdict(dict)
for num in range(10):
    valdic[num][num] = 0
    for onum in range(num+1, 10):
        cnt = 0
        for i in range(7):
            if numdic[num][i] != numdic[onum][i]:
                cnt += 1
        valdic[num][onum] = cnt
        valdic[onum][num] = cnt
        
        
#각 자릿수마다 바꿀 수 있는 경우
#총 n층/ 현재 : x층/ k 자릿수/p: 바꿀 수 있는 최대 수 

#자리 수 동일하게 바꾸기
for _ in range(k - len(n)):
    n = '0' + n
for _ in range(k - len(x)):
    x = '0' + x
    
def change_num(num, tochange):
    global p
    if valdic[num][tochange] <= p:
        p -= valdic[num][tochange]
        return 1
    return 0

res = []
total = 0
def dfs(i): #i는 자릿수
    global res, total, p
    
    if i == k: #하나도 안바꼈을 때, 0000은 제거해야함
        if "".join(res) == x or int("".join(res)) == 0 or int("".join(res)) > int(n[:i]):
            return
        total += 1
        return
    
    if ''.join(res) == n[:i]:
        case = int(n[i]) + 1
    else:
        case = 10
    
    for j in range(case):
        if change_num(int(x[i]), j):
            res.append(str(j))
            dfs(i+1)
            res.pop()
            p += valdic[int(x[i])][j]

dfs(0)
print(total)