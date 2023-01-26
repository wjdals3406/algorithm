from collections import deque
def solution(s):
    answer = 0
    stack = []
    dic = {'(' : ')', '[':']', '{': '}'}
    s = deque(s)
    
    def check(s):
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                
                if dic[stack[-1]] == i:
                    stack.pop()
                else:
                    if i in ')]}':
                        return False
                    
        return len(stack) == 0
                    
   
    for _ in range(len(s)):
        s.rotate(-1)
        if check(s):
            answer += 1
               
    return answer



print(solution(	"}]()[{"))