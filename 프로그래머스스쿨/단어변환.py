from collections import defaultdict, deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    def is_change(start, end):
        cnt = 0
        for i in range(len(start)):
            if start[i] != end[i]:
                cnt += 1
                
        if cnt == 1:
            return 1
        else:
            return 0
        
    def bfs(start):
        que = deque([[start,0]])
        visited[start] = 1
        res = 51
        while que:
            s, num = que.popleft()
            for i in dic[s]:
                if not visited[i]:
                    if i == target:
                        res = min(res, num+1)
                    else:
                        que.append([i, num + 1])
                        visited[i] = 1
        return res
    
    dic = defaultdict(list)
    visited = defaultdict(list)
    for j in range(len(words)):
        if is_change(begin, words[j]):
            dic[begin].append(words[j])
        visited[begin] = 0
                
    for i in words:
        for j in range(len(words)):
            if is_change(i, words[j]):
                dic[i].append(words[j])
        visited[i] = 0
    
    return bfs(begin)

begin = "hit"	
target = "cog"	
words = ["hot", "dot", "dog", "lot", "log", "cog"]	
print(solution(begin, target, words))