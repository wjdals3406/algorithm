# -*- coding: utf-8 -*-
import sys
#���������� ����, �׳� i��° ���ں��� ���� ��� ������ ��ϵ��� ���ǹ�
# i��° ������ �������� ���� ����� ���� �� �ִ밪�� ���������� ���
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
dp[0] = data[0]
for i in range(1,n):
    dp[i] = max(dp[i-1] + data[i], data[i]) 
#�� ó���� max(dp[i-1] + data[i], dp[i-1])�̶�� ��������
print(max(dp))
