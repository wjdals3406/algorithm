def solution(brown, yellow):
    total = brown+yellow
    
    #total�� ��� ã��
    for i in range(2, total+1):
        if total % i == 0:
            if (i - 2) * (total//i - 2) == yellow:
                return [total//i , i]
            