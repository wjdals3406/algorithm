# -*- coding: utf-8 -*-

import sys
n = int(input())
T = [] # ����� �Ϸ��ϴµ� �ɸ��� �Ⱓ
P = [] # ��� ���� ���� �� �ִ� �ݾ�
dp = [0] * (n+1) #���� ���ڱ����� �ִ� ����
max_value = 0

for _ in range(n):
    t, p = list(map(int,sys.stdin.readline().split()))
    T.append(t) 
    P.append(p) 
    
for i in range(n-1, -1, -1):
    time = T[i] + i
    
    #����� �Ⱓ �ȿ� ������ ���
    if time <= n:
        dp[i] = max(P[i] + dp[time], max_value)
        max_value = dp[i] #dp �߿����� max��
    
    else:
        dp[i] = max_value
        
print(dp)