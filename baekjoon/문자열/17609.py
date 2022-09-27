# -*- coding: utf-8 -*-
import sys
k = int(sys.stdin.readline())
for _ in range(k):
    word = sys.stdin.readline().rstrip()
    cnt = 0
    flag = 1
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            flag = 0
            #앞글자 제거
            remove_f = word[:i] + word[i+1:]
            if i == 0:
                remove_l = word[:-(i+1)] + word[:-i]
            else:
                remove_l = word[:-(i+1)] + word[-i:]
            if  remove_f == remove_f[::-1] or remove_l == remove_l[::-1]:
                print(1)
            else:
                print(2)
            break
                
    if flag:
        print(0)
