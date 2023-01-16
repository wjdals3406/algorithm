# -*- coding: utf-8 -*-
import math

def solution(n, k):
    lst = [x for x in range(1, n+1)]
    answer = []
    k -= 1
    
    for _ in range(n, 0, -1):
        # #n-1���� ������ ��� �Ǵ��� 
        # [1,2,3] �迭�� ���� ��, [1,2]/[2,3]/[1,3]���� ���� �� �ִ� ���� �� = 3!//3 = (n-1)!
        rest_num = math.factorial(n-1) 
        index = k//rest_num # answer�� i��° ���� index
        answer.append(lst[index]) 
        lst.pop(index) #�ߺ� ���X
        
        # [1,2,3]���� 5��° ���� ���ϴ� ���� -> [1,2]���� k%rest_num = 1(5//2)��° ���ڸ� ���ϴ� ������ �ȴ�.
        n,k = n-1, k%rest_num 

    return answer

print(solution(3,5))