#최소 필요 피로도 : 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도
#소모 피로도 : 던전을 탐험한 후 소모되는 피로도
#dungeons의 개수가 10개 이하이기 때문에 시간초과 안남
from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for i in list(permutations(dungeons, len(dungeons))):
        total = k
        res = 0 
        for need, remove in i:
            if total >= need:
                total -= remove
                res += 1
            else:
                break
        answer = max(answer, res)
    return answer