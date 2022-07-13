# -*- coding: utf-8 -*- 
#�׽�Ʈ ���̽� �Ѱ� �ð��ʰ�
def binary_left_search(array, target, start, end): #ù��° ���� ?�� ��
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target: #?�̸�
            start = mid + 1
        else:
            value = mid
            end = mid - 1
    return value

def binary_right_search(array, start, end): #ù��° ���� ������ ��
    while start <= end:
        mid = (start + end) // 2
        if array[mid] >= 'a' and array[mid] <= 'z': #�����̸�
            start = mid + 1
        else:
            value = mid
            end = mid - 1
    return value

def solution(words, queries):
    result = []
    #ù �ܾ ?���� �ƴ���
    #?�� �ƴϸ�    
    #?�̸� ����Ž�� �ǽ��ؼ� mid�� ?�̸� �޺κп��� Ž���ǽ� / ������ �ܾ ?���� Ȯ��
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