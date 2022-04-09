# -*- coding: utf-8 -*-
n = input()

count = 0
answer = ''

if n[0] == '0':
    answer = '1'
else:
    answer = '0'
    
for i in range(1, len(n)):
    if answer[i-1] == n[i]:
        answer += n[i]
        if n[i-1] != n[i]:
            count += 1
    elif n[i] == '0':
        answer += '1'
    
    elif n[i] == '1':
        answer += '0'
        
print(count)
        
