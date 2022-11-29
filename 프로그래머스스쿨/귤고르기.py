from collections import Counter
#이걸 중복조합으로 풀면 시간초과남 -> 시간복잡도 생각해보기
def solution(k, tangerine):
    #value순으로 정렬
    data = sorted(Counter(tangerine).items(), key=lambda x: x[1])
    cnt = 0
    k = len(tangerine) - k
    for idx, val in enumerate(data):
        key, value = val
        k -= value
        if k == 0:
            return len(data) - idx - 1
        elif k < 0:
            return len(data) - idx
            
    return 0