# -*- coding: utf-8 -*-
import sys
# 집의 개수 N과 공유기의 개수 C
n,c = map(int,sys.stdin.readline().split())
data = sorted([int(sys.stdin.readline()) for _ in range(n)])

res = 0
def binary_search(left, right):
    while left <= right:
        mid = (left+right)//2 #두 공유기 사이의 거리를 최대로 하는 거리
        cnt = 1
        before = data[0]
        for i in range(1,n):
            if before + mid <= data[i]:
                cnt += 1
                before = data[i]
                
        if cnt < c: #mid를 줄여야함
            right = mid - 1
        elif cnt >= c:
            global res
            res = mid
            left = mid + 1

binary_search(1,data[-1] - data[0])
# binary_search(data[1] - data[0],data[-1] - data[0])#이렇게 하면 안됨 -> data[1] - data[0] 이게 min gap이 아님!
print(res)