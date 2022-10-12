# -*- coding: utf-8 -*-
import sys
# ���� ���� N�� �������� ���� C
n,c = map(int,sys.stdin.readline().split())
data = sorted([int(sys.stdin.readline()) for _ in range(n)])

res = 0
def binary_search(left, right):
    while left <= right:
        mid = (left+right)//2 #�� ������ ������ �Ÿ��� �ִ�� �ϴ� �Ÿ�
        cnt = 1
        before = data[0]
        for i in range(1,n):
            if before + mid <= data[i]:
                cnt += 1
                before = data[i]
                
        if cnt < c: #mid�� �ٿ�����
            right = mid - 1
        elif cnt >= c:
            global res
            res = mid
            left = mid + 1

binary_search(1,data[-1] - data[0])
# binary_search(data[1] - data[0],data[-1] - data[0])#�̷��� �ϸ� �ȵ� -> data[1] - data[0] �̰� min gap�� �ƴ�!
print(res)