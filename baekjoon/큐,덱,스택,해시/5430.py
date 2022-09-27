# -*- coding: utf-8 -*-
import sys
import re
from collections import deque

n = int(sys.stdin.readline())
for _ in range(n):
    func = sys.stdin.readline().rstrip()
    _ = int(sys.stdin.readline())
    data = sys.stdin.readline().rstrip()
    # data = re.sub(r'[^\w]', "", data)
    data = data.replace("[", "") #문자열 제거 함수 다시 살펴보기 & 외우기
    data = data.replace("]", "") #그냥 data[1:-2]해도됨
    data= deque(data.split(","))
    flag = 0
    flag2 = 0
    for i in func:
        if i == 'R':
            flag2 += 1 #reverse 함수 사용하면 시간초과 남
        else:
            if not data or data[0] == '':
                print('error')
                flag = 1
                break
            else:
                if flag2 % 2 != 0:
                    data.pop()
                else:
                    data.popleft()
    if flag == 0:
        if flag2 % 2 == 0:
            result = ",".join(data)
            result = '[' + result + ']'
            print(result)
        else:
            data.reverse()
            result = ",".join(data)
            result = '[' + result + ']'
            print(result)
            