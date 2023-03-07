# -*- coding: utf-8 -*-
from collections import deque
import sys
data = deque([deque(input().rstrip()) for _ in range(4)]) #N극은 0, S극은 1
data.appendleft(0)
k = int(input()) #회전횟수
#방향이 1 -> 시계 / -1 -> 반시계

for _ in range(k):
    check = [0] * 5
    wheel,dir = map(int, sys.stdin.readline().split())
    
    w = wheel
    d = dir
    flag = 0
    #톱니바퀴의 왼쪽 이동
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
    #톱니바퀴의 오른쪽 이동
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

#개선코드
# import sys
# from collections import deque
# # 문제의 경우 1은 시계방향, -1은 반시계 방향이다.
# # deque의 rotate = -1일 경우 반시계 방향, 1일 경우 시계 방향으로 움직인다.

# def check_right(start, dirs):
#     # 더 이상 조사가 불가능한 경우
#     if start > 4 or gears[start-1][2] == gears[start][6]:
#         return

#     # 오른쪽 확인
#     if gears[start-1][2] != gears[start][6]:
#         # 인접한 톱니바퀴가 회전 가능한지부터 먼저 파악한다.
#         check_right(start + 1, -dirs)
#         # 회전시킨다.
#         gears[start].rotate(dirs)


# def check_left(start, dirs):
#     if start < 1 or gears[start][2] == gears[start+1][6]:
#         return
    
#     # 왼쪽 확인
#     if gears[start+1][6] != gears[start][2]:
#         check_left(start - 1, -dirs)
#         gears[start].rotate(dirs)
        
    

# gears = {}
# # 기준 톱니바퀴가 있을 때, 왼쪽과 맞닿는 지점은 idx 2, 오른쪽은 6이다.
# for i in range(1, 5):
#     gears[i] = deque(list(map(int, list(sys.stdin.readline().replace("\n","")))))
# n = int(sys.stdin.readline())

# for _ in range(n):
#     num, dirs = map(int, sys.stdin.readline().split())

#     # 기준 톱니바퀴가 주어졌을 때, 오른쪽 / 왼쪽이 회전 가능한지를 각각 확인하고 회전시킨다.
#     check_right(num+1, -dirs)
#     check_left(num-1, -dirs)
#     # 기준 톱니바퀴를 회전시킨다.
#     gears[num].rotate(dirs)
    

# result = 0
# for i in range(4):
#     result += (2**i) * gears[i+1][0]
# print(result)