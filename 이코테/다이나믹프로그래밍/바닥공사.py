# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
m = n
# rec_list = [(2,2), (2,1), (2,2)] #ù��°���� ������ �� �� �־�� ��
rec_list = [2, 1, 2] #n�� rec_list�� ������ ��Ÿ����.
rec_copy = rec_list.copy()
#i�� �ִ��� 3�� ������ �ϰ� -> �� ������ �ϳ��� �ٿ�����
count = 0
for height in rec_list:
    c = m // height
    
    #height�� �� ������ -> �ٸ� ����Ʈ�� �ֱ�
    rec_copy.remove(height) 
    while c > 0 and m > 0 :
        m = m - height * c 
        c2 = m // rec_copy[0]
        if m == 0:
            count += 1
        while c2 >= 0 and m > 0:
            m = m - rec_copy[0]* c2
            if m % rec_copy[1] == 0:
                count += 1
            m = m + rec_copy[0]* c2
            c2 -= 1
        m = m + height * c
        c -= 1
    
    m = n
    rec_copy = rec_list.copy()

print(count)
