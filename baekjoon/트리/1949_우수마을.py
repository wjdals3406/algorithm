#포도주 시식과 비슷하게 품
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

people = list(map(int, input().split()))
graph = defaultdict(list)
visited = [0] * (n+1)
dp = [0] * (n+1)
people = [0] + people

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(node):
    visited[node] = 1
    total,subtree = 0,0
    
    for i in graph[node]:
        if not visited[i]:
            dfs(i)
            for sub in graph[i]: ##이이전 트리의 값
                if sub != node:
                    subtree += dp[sub]

            total += dp[i]
    
    dp[node] = max(dp[node], total, subtree + people[node]) #현dp값, 이이전트리들 + 현데이터값, 이전트리 합

dfs(1)

print(max(dp))