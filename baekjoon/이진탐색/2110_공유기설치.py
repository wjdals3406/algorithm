# # -*- coding: utf-8 -*-
# import sys
# # 집의 개수 N과 공유기의 개수 C
# n,c = map(int,sys.stdin.readline().split())
# data = sorted([int(sys.stdin.readline()) for _ in range(n)])

# res = 0
# def binary_search(left, right):
#     while left <= right:
#         mid = (left+right)//2 #두 공유기 사이의 거리를 최대로 하는 거리
#         cnt = 1
#         before = data[0]
#         for i in range(1,n):
#             if before + mid <= data[i]:
#                 cnt += 1
#                 before = data[i]
                
#         if cnt < c: #mid를 줄여야함
#             right = mid - 1
#         elif cnt >= c:
#             global res
#             res = mid
#             left = mid + 1

# binary_search(1,data[-1] - data[0])
# # binary_search(data[1] - data[0],data[-1] - data[0])#이렇게 하면 안됨 -> data[1] - data[0] 이게 min gap이 아님!
# print(res)



#두번째 풀이 / 구현하는 데에 약 한시간 소요
# -*- coding: utf-8 -*-
import sys
# 집의 개수 N과 공유기의 개수 C
#가장 인접한 두 공유기 사이의 최대 거리 출력
n,c = map(int,sys.stdin.readline().split())
data = sorted([int(sys.stdin.readline()) for _ in range(n)])
# 1 6 9일때, 공유기 3개 설치한다면 두 공유기 사이의 최대 거리는 3


def binary_search(start, end, c): #인접한 거리 탐색 / 최댓값 : data[-1] - data[0]
    res = 0
    #거리의 중앙값
    while start <= end:
        mid = (start + end) // 2
        build = c
        pre = 0

        i = 1
        while i < len(data) and build > 0:
            if data[i] - data[pre] < mid: 
                i += 1
                continue
            
            #data[i] - data[pre] >= mid일 때
            #공유기 설치
            build -= 1
            pre = i
            i += 1
        if build > 0: # 공유기 다 설치 못함 -> 간격 줄이기
            end = mid - 1
        
        else:
            start = mid + 1
            res = max(res, mid) #이렇게 max 함수 하지 않고 그냥 res = mid 해주면 됨
    
    return res
        
        
c -= 1 # 맨 첫집에 공유기 설치함
print(binary_search(0, data[-1] - data[0], c))