# -*- coding: utf-8 -*-
# 문자열을 그대로 두고 커서움직임 (일반적 생각) -> 시간초과로 문제해결이 되지 않는다 -> 발상의 전환이 필요함
# 커서는 움직이지않고 커서를 기준으로 왼쪽은 left라는 배열에, 오른쪽은 right라는 배열에 담아 배열2개를 활용하면 문제해결이 가능하다.
# https://esoongan.tistory.com/63
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    password = list(input().strip())
    left, right = [], []

    for j in password:
        if j == '<':
            if left:  # left가 비어있지 않으면 -> 커서가 이동가능하면 
                right.append(left.pop())
        elif j == '>':
            if right:  # 커서가 이동가능하면 
                left.append(right.pop())
        elif j == '-':
            if left:  # 삭제할 문제가 있으면 
                left.pop()
        else:
            left.append(j)

    left.extend(reversed(right)) # right배열은 실제 문자열과 반대정렬이므로 다시 원래대로돌림 

    print(''.join(left))