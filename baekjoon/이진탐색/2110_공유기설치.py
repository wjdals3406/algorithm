# # -*- coding: utf-8 -*-
# import sys
# # ���� ���� N�� �������� ���� C
# n,c = map(int,sys.stdin.readline().split())
# data = sorted([int(sys.stdin.readline()) for _ in range(n)])

# res = 0
# def binary_search(left, right):
#     while left <= right:
#         mid = (left+right)//2 #�� ������ ������ �Ÿ��� �ִ�� �ϴ� �Ÿ�
#         cnt = 1
#         before = data[0]
#         for i in range(1,n):
#             if before + mid <= data[i]:
#                 cnt += 1
#                 before = data[i]
                
#         if cnt < c: #mid�� �ٿ�����
#             right = mid - 1
#         elif cnt >= c:
#             global res
#             res = mid
#             left = mid + 1

# binary_search(1,data[-1] - data[0])
# # binary_search(data[1] - data[0],data[-1] - data[0])#�̷��� �ϸ� �ȵ� -> data[1] - data[0] �̰� min gap�� �ƴ�!
# print(res)



#�ι�° Ǯ�� / �����ϴ� ���� �� �ѽð� �ҿ�
# -*- coding: utf-8 -*-
import sys
# ���� ���� N�� �������� ���� C
#���� ������ �� ������ ������ �ִ� �Ÿ� ���
n,c = map(int,sys.stdin.readline().split())
data = sorted([int(sys.stdin.readline()) for _ in range(n)])
# 1 6 9�϶�, ������ 3�� ��ġ�Ѵٸ� �� ������ ������ �ִ� �Ÿ��� 3


def binary_search(start, end, c): #������ �Ÿ� Ž�� / �ִ� : data[-1] - data[0]
    res = 0
    #�Ÿ��� �߾Ӱ�
    while start <= end:
        mid = (start + end) // 2
        build = c
        pre = 0

        i = 1
        while i < len(data) and build > 0:
            if data[i] - data[pre] < mid: 
                i += 1
                continue
            
            #data[i] - data[pre] >= mid�� ��
            #������ ��ġ
            build -= 1
            pre = i
            i += 1
        if build > 0: # ������ �� ��ġ ���� -> ���� ���̱�
            end = mid - 1
        
        else:
            start = mid + 1
            res = max(res, mid) #�̷��� max �Լ� ���� �ʰ� �׳� res = mid ���ָ� ��
    
    return res
        
        
c -= 1 # �� ù���� ������ ��ġ��
print(binary_search(0, data[-1] - data[0], c))