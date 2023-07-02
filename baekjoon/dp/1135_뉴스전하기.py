import sys
import heapq
from collections import defaultdict
n = int(sys.stdin.readline())
data = list(map(int, input().split()))
dic = defaultdict(list)
dp = [0] * n #i번째 노드에게 소식 전하는 데 걸리는 시간
#자신의 직속 부하에게만 전화걸기 가능
#전화 정확하게 1분
#모든 직원이 소식을 듣는데 걸리는 시간의 최솟값

for i in range(n):
    dic[data[i]].append(i)
        
def dfs(node):
    if node not in dic: #자식 노드가 없으면 return
        return 0
    
    h = []
    #가장 시간이 오래 걸리는 노드
    for cnode in dic[node]:
        h.append(dfs(cnode))
        
    h.sort(reverse=True)
    h = [i + 1 + h[i] for i in range(len(h))]
    dp[node] = max(h)
    
    return dp[node]
    
    
print(dfs(0))