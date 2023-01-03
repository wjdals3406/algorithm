# -*- coding: utf-8 -*-
import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())
belt = deque(map(int, sys.stdin.readline().split())) #������
robot = deque([0] * n) 

def rotate_all(): 
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

def rotate_robot():
    for i in range(n-2,-1,-1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1]>=1: #�κ��� ������, �� ĭ�� �������� 1 �̻� ��������
            robot[i+1] = 1
            robot[i] = 0
            belt[i+1] -= 1 #������ ����
    robot[-1] = 0

def lift_robot():
    if belt[0] != 0 and robot[0] == 0 :
        robot[0] = 1
        belt[0] -= 1 #������ ����

res = 0
while belt.count(0) < k: #�������� 0�� ĭ�� ������ K�� �̻��̶�� ���� ����
    #1�ܰ�
    rotate_all()
    #2�ܰ�
    rotate_robot()
    #3�ܰ�
    lift_robot()
    res += 1
print(res)
