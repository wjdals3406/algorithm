# -*- coding: utf-8 -*-
reports = {x : 0 for x in [0,1,2]}
print(reports)

result = 0 #read는 되는데 write는 안됨
def func():
    print(result)
    
func()

result = 0
def func():
    result += 1
    
func()


#리스트 인덱싱할 때 리스트 길이보다 큰 인덱스를 접근할라 하면 IndexError 나지만,
#list[10000:] 이렇게 큰값: 하면 에러안남 
a = [1,2,3,4,5]
print(a[10:]) #결과 : []