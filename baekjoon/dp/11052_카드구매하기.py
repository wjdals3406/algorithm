# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split())) #ī�尡 i�� ���Ե� ī������ ������ Pi��
card = [0] + card
dp = card[:] #i��° ����, i��°������ �ִ�

# for i in range(1,n+1):
#     for j in range(i,n+1, i):
#         dp[j] = max(card[i] * (j//i), dp[j])

for i in range(2,n+1):
    for j in range(1,i//2+1):
        dp[i] = max(dp[j] + dp[i-j], dp[i])

print(dp[-1])
        
    

