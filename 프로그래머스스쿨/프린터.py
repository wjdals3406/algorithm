from collections import deque
def solution(priorities, location):
    priorities = deque(zip([i for i in range(len(priorities))], priorities))
    cnt = 1
    while priorities:
        i,value = priorities.popleft()
        if len(priorities) > 0:
            if any([value < j[1] for j in priorities]):
                priorities.append((i,value))
            else:
                if i == location:
                    return cnt
                else:
                    cnt += 1
        else:
            return cnt
        
#any(iterable) �Լ��� ���ڷ� ���� �ݺ������� �ڷ���(iterable)�� 
#�� �ϳ��� ��(True)�� ������ ��(True)�� ��ȯ�ϴ� �Լ�

print(solution([2, 1, 3, 2]	, 2))