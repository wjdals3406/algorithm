# -*- coding: utf-8 -*-
# ���߿� �� �ִ� �̳׶��� ���� �پ��ִ� �̳׶��� �����ϴ� �� -> bfs�� 
from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# �̳׶� ������ �� �ִ��� ĭ ����
def checkDownCnt(fallLst, check):
    downCnt, flag = 1, 0      # downCnt ũ�� 1�� �÷�����
    while True:
        for r, c in fallLst:
            if r+downCnt == R-1:        # ���� �����ų�
                flag = 1
                break
            if cave[r+downCnt+1][c] == 'x' and check[r+downCnt+1][c]:   # �ٸ� �̳׶� ������
                flag = 1
                break
        if flag:    # �� ���� ������ �� �ִ� �ִ� downCnt ��
            break
        downCnt += 1
    return downCnt

def checkLand():
    check = [[0] * C for _ in range(R)]
    # ���� �پ� �ִ� �̳׶� check �迭�� ǥ��
    for lc in range(C):
        if cave[R-1][lc] == "x" and not check[R-1][lc]:     # �̳׶��̸鼭 ù �湮�̸�
            check[R-1][lc] = 1
            Q = deque([(R-1, lc)])
            while Q:
                r, c = Q.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if not (0 <= nr < R and 0 <= nc < C):       # ���� ���̸�
                        continue
                    if cave[nr][nc] == "x" and not check[nr][nc]:   # �̳׶��̰ų� �湮�� �� ������
                        check[nr][nc] = 1
                        Q.append((nr, nc))
    return check


def breakMinerals(br, bc):
	# 2�ܰ� - ���� �پ� �ִ� �̳׶� 1�� ǥ�õǾ� �ִ� �� ����
    check = checkLand()

	# 3�ܰ� - ���߿� ���ִ� �̳׶� 2�� ǥ��, �������� �����
    minerals = []    # ���߿� ���ִ� �̳׶� ����Ʈ
    fallLst = []     # ������ �� �ִ� Ŭ�������� �Ʒ��κи� ����
    for nd in range(4):     # ���� �� �������� 4���� Ȯ��
        r = br + dr[nd]
        c = bc + dc[nd]
        if not (0 <= r < R and 0 <= c < C):
            continue

        # �̳׶��ε� ���� �پ� ���� �ʴٸ�(check �迭���� 0���� ǥ�õǾ� �ִٸ�) 2�� ǥ��
        if cave[r][c] == "x" and not check[r][c]:
            Q = deque([(r, c)])
            check[r][c] = 2
            minerals.append((r, c))
            cave[r][c] = "."
            while Q:
                r, c = Q.popleft()
                if cave[r+1][c] == ".":     # �ٷ� ���� �� ������ �̳׶�
                    fallLst.append((r, c))
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    if cave[nr][nc] == "x" and not check[nr][nc]:
                        check[nr][nc] = 2           # ���߿� ���ִ� �̳׶� Ŭ������ ǥ��
                        Q.append((nr, nc))
                        minerals.append((nr, nc))   # �̳׶� ��ġ ����Ʈ�� ���
                        cave[nr][nc] = "."          # �������� ���߿� �� �ִ� �̳׶� ����

    if fallLst:    # ���߿� ���ִ� �̳׶��� �ִٸ�
    	# 4�ܰ� - ������ �ִ� ĭ�� �� ����
        downCnt = checkDownCnt(fallLst, check)

        # 5�ܰ� - �̳׶� ������ ��ġ ������ �׸���
        for mr, mc in minerals:
            cave[mr+downCnt][mc] = "x"

# main
R, C = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(R)]
N = int(input())
heights = list(map(int, input().split()))

# 1�ܰ� - �¿쿡�� ����� ���� �̳׶� ����
for i in range(N):
    br = R - heights[i]
    if not i % 2:       # ���ʿ��� ��
        for bc in range(C):
            if cave[br][bc] == "x":
                cave[br][bc] = "."
                breakMinerals(br, bc)   # ���� ��ġ ���ڷ� �Ѱ� �̳׶� ����
                break
    else:               # �����ʿ��� ��
        for bc in range(C-1, -1, -1):
            if cave[br][bc] == "x":
                cave[br][bc] = "."
                breakMinerals(br, bc)
                break
    
# ���Ŀ� �°� ���
for row in cave:
    print(''.join(row))