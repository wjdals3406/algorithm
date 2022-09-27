# -*- coding: utf-8 -*-
import sys
INF = int(1e9) # ������ �ǹ��ϴ� ������ 10���� ����
# ����� ���� �� ������ ������ �Է¹ޱ�
n,m  = map(int, sys.stdin.readline().split())
# 2���� ����Ʈ(�׷��� ǥ��)�� �����, ��� ���� �������� �ʱ�ȭ
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# �ڱ� �ڽſ��� �ڱ� �ڽ����� ���� ����� 0���� �ʱ�ȭ
for a in range(1, n + 1):
    graph[a][a] = 0

# �� ������ ���� ������ �Է� �޾�, �� ������ �ʱ�ȭ
for _ in range(m):
    # A���� B�� ���� ����� C��� ����
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, sys.stdin.readline().split())
# ��ȭ�Ŀ� ���� �÷��̵� ���� �˰����� ����
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
result = min(graph[1][v1] + graph[v1][v2] + graph[v2][n], graph[1][v2] + graph[v2][v1] + graph[v1][n])
if result == INF:
    print(-1)
else:
    print(result)
