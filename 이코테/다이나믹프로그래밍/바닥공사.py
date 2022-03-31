# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
m = n
# rec_list = [(2,2), (2,1), (2,2)] #첫번째꺼는 무조건 두 개 있어야 함
rec_list = [2, 1, 2] #n을 rec_list의 합으로 나타낸다.
rec_copy = rec_list.copy()
#i로 최대한 3에 가깝게 하고 -> 그 다음에 하나씩 줄여보고
count = 0
for height in rec_list:
    c = m // height
    
    #height를 뺀 나머지 -> 다른 리스트에 넣기
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
