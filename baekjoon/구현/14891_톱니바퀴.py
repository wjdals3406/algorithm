# -*- coding: utf-8 -*-
from collections import deque
import sys
data = deque([deque(input().rstrip()) for _ in range(4)]) #N���� 0, S���� 1
data.appendleft(0)
k = int(input()) #ȸ��Ƚ��
#������ 1 -> �ð� / -1 -> �ݽð�

for _ in range(k):
    check = [0] * 5
    wheel,dir = map(int, sys.stdin.readline().split())
    
    w = wheel
    d = dir
    flag = 0
    #��Ϲ����� ���� �̵�
    if w > 1:
        while w > 1:
            if data[w][6] == data[w-1][2]:
                if w != wheel:
                    data[w].rotate(d)
                flag = 1
                break
            else:
                if w != wheel:
                    data[w].rotate(d)
                d = d * (-1)
                w -= 1
        if not flag:
            data[w].rotate(d)
    
    w = wheel
    d = dir
    flag = 0
    #��Ϲ����� ������ �̵�
    if w < 4:
        while w < 4:
            if data[w][2] == data[w+1][6]:
                data[w].rotate(d)
                flag = 1
                break
            else:
                data[w].rotate(d)
                d = d * (-1)
                w += 1
                
        if not flag:
            data[w].rotate(d)
    else:
        data[wheel].rotate(dir)
        
res = 0
plist = [0,1,2,4,8]
for i in range(1,5):
    if data[i][0] == '1':
       res += plist[i]
       
print(res)

#�����ڵ�
# import sys
# from collections import deque
# # ������ ��� 1�� �ð����, -1�� �ݽð� �����̴�.
# # deque�� rotate = -1�� ��� �ݽð� ����, 1�� ��� �ð� �������� �����δ�.

# def check_right(start, dirs):
#     # �� �̻� ���簡 �Ұ����� ���
#     if start > 4 or gears[start-1][2] == gears[start][6]:
#         return

#     # ������ Ȯ��
#     if gears[start-1][2] != gears[start][6]:
#         # ������ ��Ϲ����� ȸ�� ������������ ���� �ľ��Ѵ�.
#         check_right(start + 1, -dirs)
#         # ȸ����Ų��.
#         gears[start].rotate(dirs)


# def check_left(start, dirs):
#     if start < 1 or gears[start][2] == gears[start+1][6]:
#         return
    
#     # ���� Ȯ��
#     if gears[start+1][6] != gears[start][2]:
#         check_left(start - 1, -dirs)
#         gears[start].rotate(dirs)
        
    

# gears = {}
# # ���� ��Ϲ����� ���� ��, ���ʰ� �´�� ������ idx 2, �������� 6�̴�.
# for i in range(1, 5):
#     gears[i] = deque(list(map(int, list(sys.stdin.readline().replace("\n","")))))
# n = int(sys.stdin.readline())

# for _ in range(n):
#     num, dirs = map(int, sys.stdin.readline().split())

#     # ���� ��Ϲ����� �־����� ��, ������ / ������ ȸ�� ���������� ���� Ȯ���ϰ� ȸ����Ų��.
#     check_right(num+1, -dirs)
#     check_left(num-1, -dirs)
#     # ���� ��Ϲ����� ȸ����Ų��.
#     gears[num].rotate(dirs)
    

# result = 0
# for i in range(4):
#     result += (2**i) * gears[i+1][0]
# print(result)