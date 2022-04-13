def solution(food_times, k):
    answer = 0
    flag  = 0
    while True:
        for i in range(len(food_times)):
            if food_times[i] == 0 :
                continue
            if k == 0:
                flag = 1
                answer = i+1
                break
            
            food_times[i] -= 1
            k -= 1
        
        if flag == 1:
            break
    return answer


food_times = [3, 1, 2]
print(solution(food_times, 5))