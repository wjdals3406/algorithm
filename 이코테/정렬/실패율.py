def solution(N, stages):
    result = []
    fail = [[0, i+1] for i in range(N)]
    visited=[0 for _ in range(N)]
    stages.sort()
    
    for i in range(len(stages)):
        if stages[i] > N:
            break
        if visited[stages[i] - 1]:
            continue
        else:
            fail[stages[i] - 1] = [stages.count(stages[i])/len(stages[i:]), stages[i]]
            visited[stages[i] - 1] = 1
    fail.sort(key = lambda x : (-x[0], x[1]))
    
    for i in fail:
        result.append(i[1])
            
    return result

N = 5	
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))