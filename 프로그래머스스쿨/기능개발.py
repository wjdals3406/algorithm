# import math
# def solution(progresses, speeds):
#     res = []
#     answer = []
#     for i in range(len(speeds)):
#         answer.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
#     answer.reverse()
#     back = []
#     while answer:
#         num = answer.pop()
#         if not back:
#             back.append(num)
#         else:
#             if num <= back[0]:
#                 back.append(num)
#             else:
#                 res.append(len(back))
#                 back = [num]
#     if back:
#         res.append(len(back))
#     return res

import math


def solution(progresses, speeds):
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    answer = []
    front = 0
    print(progresses)

    for idx in range(len(progresses)):
        if progresses[idx] > progresses[front]:  
            print(progresses[idx], progresses[front])
            answer.append(idx - front)
            front = idx 
    answer.append(len(progresses) - front)  

    return answer
 