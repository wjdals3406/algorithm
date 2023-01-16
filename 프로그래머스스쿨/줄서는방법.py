# -*- coding: utf-8 -*-
import math

def solution(n, k):
    lst = [x for x in range(1, n+1)]
    answer = []
    k -= 1
    
    for _ in range(n, 0, -1):
        # #n-1개의 묶음이 몇개가 되는지 
        # [1,2,3] 배열이 있을 때, [1,2]/[2,3]/[1,3]으로 만들 수 있는 가짓 수 = 3!//3 = (n-1)!
        rest_num = math.factorial(n-1) 
        index = k//rest_num # answer의 i번째 수의 index
        answer.append(lst[index]) 
        lst.pop(index) #중복 허용X
        
        # [1,2,3]에서 5번째 수를 구하는 문제 -> [1,2]에서 k%rest_num = 1(5//2)번째 숫자를 구하는 문제가 된다.
        n,k = n-1, k%rest_num 

    return answer

print(solution(3,5))