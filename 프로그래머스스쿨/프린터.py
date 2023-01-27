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
        
#any(iterable) 함수는 인자로 받은 반복가능한 자료형(iterable)중 
#단 하나라도 참(True)이 있으면 참(True)를 반환하는 함수

print(solution([2, 1, 3, 2]	, 2))