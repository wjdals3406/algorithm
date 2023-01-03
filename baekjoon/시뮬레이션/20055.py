# -*- coding: utf-8 -*-
import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())
belt = deque(map(int, sys.stdin.readline().split())) #내구도
robot = deque([0] * n) 

def rotate_all(): 
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

def rotate_robot():
    for i in range(n-2,-1,-1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1]>=1: #로봇이 없으며, 그 칸의 내구도가 1 이상 남아있음
            robot[i+1] = 1
            robot[i] = 0
            belt[i+1] -= 1 #내구도 감소
    robot[-1] = 0

def lift_robot():
    if belt[0] != 0 and robot[0] == 0 :
        robot[0] = 1
        belt[0] -= 1 #내구도 감소

res = 0
while belt.count(0) < k: #내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료
    #1단계
    rotate_all()
    #2단계
    rotate_robot()
    #3단계
    lift_robot()
    res += 1
print(res)
