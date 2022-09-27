# -*- coding: utf-8 -*-
# ���ڿ��� �״�� �ΰ� Ŀ�������� (�Ϲ��� ����) -> �ð��ʰ��� �����ذ��� ���� �ʴ´� -> �߻��� ��ȯ�� �ʿ���
# Ŀ���� ���������ʰ� Ŀ���� �������� ������ left��� �迭��, �������� right��� �迭�� ��� �迭2���� Ȱ���ϸ� �����ذ��� �����ϴ�.
# https://esoongan.tistory.com/63
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    password = list(input().strip())
    left, right = [], []

    for j in password:
        if j == '<':
            if left:  # left�� ������� ������ -> Ŀ���� �̵������ϸ� 
                right.append(left.pop())
        elif j == '>':
            if right:  # Ŀ���� �̵������ϸ� 
                left.append(right.pop())
        elif j == '-':
            if left:  # ������ ������ ������ 
                left.pop()
        else:
            left.append(j)

    left.extend(reversed(right)) # right�迭�� ���� ���ڿ��� �ݴ������̹Ƿ� �ٽ� ������ε��� 

    print(''.join(left))