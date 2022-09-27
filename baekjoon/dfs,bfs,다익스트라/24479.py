import sys
sys.setrecursionlimit(10**9)
n,m,r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt_list = [0] * (n)
for _ in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()
    
count = 0
def dfs(v):
    global count
    visited[v] = True
    count += 1
    cnt_list[v-1] = count
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

#global ���ϰ� �̷��� �ϸ� �ȵ�/ �Ű������� �Ѱ��ٰŸ� count ���� return ���ֱ�!
# count = 0
# def dfs(graph, v, visited, count):
#     visited[v] = True
#     count += 1
#     cnt_list[v-1] = count
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited, count)


dfs(r)
for i in cnt_list:
    print(i)            