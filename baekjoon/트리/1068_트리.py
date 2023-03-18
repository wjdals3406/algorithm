import sys
from collections import defaultdict
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
remove = int(sys.stdin.readline())

dic = defaultdict(list)
for i in range(n):
    if data[i] == -1:
        continue
    
    dic[data[i]].append(i)

def dfs(node):
    for i in dic[node]:
        dfs(i)
        data[i] = -2
        
        
data[remove] = -2
dfs(remove)

cnt = 0
for i in range(n):
    if data[i] == -2:
        continue
    if data.count(i) == 0:
        cnt += 1
    
print(cnt)