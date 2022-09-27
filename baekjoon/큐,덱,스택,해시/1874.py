# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
print_value = []
for i in range(1, data[0]+1): #data의 첫번째 수까지 push함
    print_value.append('+')
    stack.append(i)
print_value.append('-')
next_num = stack.pop() + 1 #stack에 넣을 다음 숫자
dindex = 1
flag = 1

while next_num <= n:
    if data[dindex] < next_num:
        if stack.pop() != data[dindex]:
            flag = 0
            print("NO")
            break     
        else:
            print_value.append('-')
            dindex += 1
    else:
        stack.append(next_num)
        print_value.append('+')
        next_num += 1
if flag:
    flag2 = 1
    while stack:
        if stack.pop() != data[dindex]:
            flag2 = 0
            print("NO")
            break
        else:
            dindex += 1
            print_value.append('-')
    if flag2:
        print('\n'.join(print_value))
            