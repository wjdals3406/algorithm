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

#배열 바로 뒷 원소의 값을 비교할 때 zip함수 사용하면 좋음
def solution(phoneBook):
    phoneBook.sort()

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

#밑에 에러남 / 덱은 슬라이싱이 안됨!!
from collections import deque
a = deque([1,2,3,4])
print(a[2:])