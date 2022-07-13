# -*- coding: utf-8 -*-
# import sys
# import copy
# from itertools import combinations

# n = int(sys.stdin.readline())
# data = list(map(int,sys.stdin.readline().split()))
# # dp = [0 for _ in range(n)] #���ܽ��Ѿ� �ϴ� ������ ���� �ε���, ���� �ִ� ������ ���� ����Ʈ ��
# cdata = sorted(data, reverse=True)
# index = [i for i in range(n) if data[i] != cdata[i]]

# flag = 1
# for i in range(n):
#     comb = list(combinations(index, i))
#     for j in comb:
#         rdata = [data[x] for x in range(n) if x not in j] #���� / �ߺ� ���� �ϳ��� ���� -> �ε����� �̿��� ����
#         if rdata != sorted(rdata, reverse=True): #������������ Ȯ��
#             continue
#         print(i)
#         flag = 0
#         break
#     if flag == 0:
#         break
    
#         # dp[i] = max(dp[i], sum(rdata))

# # print(dp.index(max(dp)))      

##���� �� �����ϴ� �κ� ����(LIS) �˰��� ����ϱ�
n = int(input())  # ������ ����
array = list(map(int, input().split()))  # �־��� ����
array.reverse()

# DP ���̺� 1�� �ʱ�ȭ
dp = [1] * n #������ ���Ҹ� ������ �κ� ������ �ִ� ����

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1) 

# ���� �� �����ϴ� �κ� ������ ���̰�
print(n - max(dp))