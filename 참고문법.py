# -*- coding: utf-8 -*-
reports = {x : 0 for x in [0,1,2]}
print(reports)

result = 0 #read�� �Ǵµ� write�� �ȵ�
def func():
    print(result)
    
func()

result = 0
def func():
    result += 1
    
func()


#����Ʈ �ε����� �� ����Ʈ ���̺��� ū �ε����� �����Ҷ� �ϸ� IndexError ������,
#list[10000:] �̷��� ū��: �ϸ� �����ȳ� 
a = [1,2,3,4,5]
print(a[10:]) #��� : []