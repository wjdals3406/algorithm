from collections import defaultdict
import copy

#https://school.programmers.co.kr/questions/25736?question=25736 참고
res = 1
def solution(info, edges):

    graph = defaultdict(list)
    for p, c in edges:
        graph[p].append(c)

    def dfs(node, wolf, sheep, next_visit):
        global res
        if sheep <= wolf:
            return

        for c in graph[node]:
            next_visit.append(c)

        for vindex in range(len(next_visit)):
            vnode = next_visit[vindex]
            if info[vnode] == 0: #양이면
                res = max(res, sheep+1)

                dfs(vnode, wolf, sheep+1, copy.deepcopy(next_visit[:vindex] + next_visit[vindex+1:]))
            else: #늑대면
                dfs(vnode, wolf+1, sheep, copy.deepcopy(next_visit[:vindex] + next_visit[vindex+1:]))

    dfs(0, 0, 1, [])

    return res


print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))

#다른 풀이
# def solution(info, edges):
#     visited = [0] * len(info)
#     answer = []
    
#     def dfs(sheep, wolf):
#         if sheep > wolf:
#             answer.append(sheep)
#         else:
#             return 
        
#         for p, c in edges:
#             if visited[p] and not visited[c]:
#                 visited[c] = 1
#                 if info[c] == 0:
#                     dfs(sheep+1, wolf)
#                 else:
#                     dfs(sheep, wolf+1)
#                 visited[c] = 0

# 	# 루트 노드부터 시작
# 	visited[0] = 1
#     dfs(1, 0)

    return max(answer)
