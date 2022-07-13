# -*- coding: utf-8 -*-
# import sys
# import copy
# from itertools import combinations

# n = int(sys.stdin.readline())
# data = list(map(int,sys.stdin.readline().split()))
# # dp = [0 for _ in range(n)] #열외시켜야 하는 병사의 수가 인덱스, 남아 있는 병사의 수가 리스트 값
# cdata = sorted(data, reverse=True)
# index = [i for i in range(n) if data[i] != cdata[i]]

# flag = 1
# for i in range(n):
#     comb = list(combinations(index, i))
#     for j in comb:
#         rdata = [data[x] for x in range(n) if x not in j] #제거 / 중복 숫자 하나만 제거 -> 인덱스를 이용해 제거
#         if rdata != sorted(rdata, reverse=True): #내림차순인지 확인
#             continue
#         print(i)
#         flag = 0
#         break
#     if flag == 0:
#         break
    
#         # dp[i] = max(dp[i], sum(rdata))

# # print(dp.index(max(dp)))      

##가장 긴 증가하는 부분 수열(LIS) 알고리즘 사용하기
n = int(input())  # 수열의 길이
array = list(map(int, input().split()))  # 주어진 수열
array.reverse()

# DP 테이블 1로 초기화
dp = [1] * n #마지막 원소를 가지는 부분 수열의 최대 길이

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1) 

# 가장 긴 증가하는 부분 수열의 길이값
print(n - max(dp))