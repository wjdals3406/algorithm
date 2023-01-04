# -*- coding: utf-8 -*-
import sys
n,m = map(int, sys.stdin.readline().split())
mat_a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
mat_b = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

#mat_a를 mat_b에 맞게 바꾸기
cnt = 0
for r in range(n-2):
    for c in range(m-2):
        if mat_a[r][c] != mat_b[r][c]:
            cnt += 1
            for mr in range(3):
                for mc in range(3):
                    if mat_a[mr+r][mc+c] == '0':
                        mat_a[mr+r][mc+c] = '1'
                    else:
                        mat_a[mr+r][mc+c] = '0'
        if mat_a == mat_b:
            flag = 1
            break
    if mat_a == mat_b:
            flag = 1
            break

if mat_a != mat_b:
    print(-1)
else:
    print(cnt)