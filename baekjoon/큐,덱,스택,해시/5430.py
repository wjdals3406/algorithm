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
    data = data.replace("[", "") #���ڿ� ���� �Լ� �ٽ� ���캸�� & �ܿ��
    data = data.replace("]", "") #�׳� data[1:-2]�ص���
    data= deque(data.split(","))
    flag = 0
    flag2 = 0
    for i in func:
        if i == 'R':
            flag2 += 1 #reverse �Լ� ����ϸ� �ð��ʰ� ��
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
            