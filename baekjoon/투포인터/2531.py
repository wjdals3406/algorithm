# -*- coding: utf-8 -*-
import sys
n,d,k,c = map(int,sys.stdin.readline().split()) #������ ��,�ʹ��� ������,�����ؼ� �Դ� ������ ��,���� ��ȣ
data = [int(sys.stdin.readline()) for _ in range(n)] 
data = data * 2

s,e = 0,k
maxval = 0
for i in range(n):
    check = data[s:e]
    check_set = list(set(check))
    
    if c in check: #���� �ʹ� ����
        maxval = max(maxval, len(check_set))
    else:
        maxval = max(maxval, len(check_set)+1)
        if len(check) == len(check_set): #��ġ�� ������ ����, ���� �ʹ� �������� ���� �� -> ������ �ִ�
            break
    s += 1
    e += 1
print(maxval)
    
        
    