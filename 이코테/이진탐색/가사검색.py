# -*- coding: utf-8 -*- 
#테스트 케이스 한개 시간초과
def binary_left_search(array, target, start, end): #첫번째 값이 ?일 때
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target: #?이면
            start = mid + 1
        else:
            value = mid
            end = mid - 1
    return value

def binary_right_search(array, start, end): #첫번째 값이 문자일 때
    while start <= end:
        mid = (start + end) // 2
        if array[mid] >= 'a' and array[mid] <= 'z': #문자이면
            start = mid + 1
        else:
            value = mid
            end = mid - 1
    return value

def solution(words, queries):
    result = []
    #첫 단어가 ?인지 아닌지
    #?가 아니면    
    #?이면 이진탐색 실시해서 mid가 ?이면 뒷부분에서 탐색실시 / 마지막 단어도 ?인지 확인
    qdic = dict()
    for q in queries:
        if q in qdic:
            result.append(qdic[q])
            continue
        if q[0] == '?':
            if q[-1] == '?':
                data = [w for w in words if len(q) == len(w)]
            else:
                index = binary_left_search(q, '?', 0, len(q) - 1)
                
                data = [q for w in words if len(q) == len(w) and w[index:] == q[index:]]
        else:
            index = binary_right_search(q, 0, len(q) - 1)
            data = [q for w in words if len(q) == len(w) and w[:index] == q[:index]]
            
        result.append(len(data))
        qdic[q] = len(data)        
    return result

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))